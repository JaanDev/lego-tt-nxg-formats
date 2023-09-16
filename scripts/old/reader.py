# Beware of the spaghetti code!
# Please dont read this code!
# You have been warned

import sys
from pathlib import Path
import re

import bin_utils


def getVar(scope: list[dict[str, any]], name: str, depth: int):
    if depth < len(scope):
        d = depth
        while d >= 0:
            if name in scope[d]:
                return scope[d][name]
            d -= 1

    return None


def getVal(r: bin_utils.BinReader, t: str):
    if 'byte' in t:
        print(t)
        count = re.search(r"(\d+)", t).group(1)
        raw = r.raw(int(count))
        return raw, ' '.join([f'{x:02X}' for x in raw])
    
    realVal = None
    val = None
    match t:
        case '4CC':
            realVal = r.u32()
            val = f'{hex(realVal)} ({bytes.fromhex(hex(realVal)[2:]).decode()})'
        case 'u32':
            realVal = r.u32()
            val = f'{realVal} ({hex(realVal)})'
        case 'STR32':
            l = r.u32()
            realVal = val = r.raw(l)
        case 'u8':
            realVal = r.u8()
            val = f'{realVal} ({hex(realVal)})'
        case 'f32':
            realVal = val = r.f32()

    return realVal, val


def calc_expr(scope, depth, src) -> tuple[str, any]:
    expr_replaced = src
    pattern = re.compile(r'\w+')
    for m in pattern.findall(expr_replaced):
        value = getVar(scope, m, depth)
        if value is not None:
            expr_replaced = expr_replaced.replace(m, str(value))
    result = eval(expr_replaced)

    return expr_replaced, result


def read(script: Path, name: Path, out_path: Path):
    with open(script, 'r') as f:
        lines = [x for x in f.read().splitlines() if x.strip()]

    out = open(out_path, 'w')

    scriptName = lines.pop(0)[2:]
    print(f"- Script name: {scriptName}", file=out)

    endianness = lines.pop(0).split()[1]
    print(f"- Endianness: {endianness}", file=out)
    with open(name, 'rb') as f:
        data = f.read()
        r = bin_utils.BinReader(data, endianness.lower())

    # skip until the main part
    while lines.pop(0) != "## Main":
        pass

    # aaa = lines[0]
    # fourcc = aaa[2:].replace('`', '').split(': ')[0]
    # addr = data.find(fourcc.encode())
    # print(f'{scriptName} found at 0x{addr:X}')
    # r.goto(addr)

    x = 0
    i = 0
    l = lines[i]
    name, t = l.split('.')[0][2:].replace("`", "").split(": ")
    while t != '4CC':
        i += 1
        x += 4  # uhh ig should be ok as there are only u32 before 4cc sometimes
        l = lines[i]
        name, t = l.split('.')[0][2:].replace("`", "").split(": ")

    print(name)
    addr = data.find(name.encode())
    addr -= x
    print(f'{scriptName} found at 0x{addr:X}')
    r.goto(addr)

    print('- ', file=out)

    scope = []
    depth = 0
    maxDepth = -1  # for conditionals
    curLine = 0
    loops = []  # .0 = times left .1 = start line .2 = depth .3 = iter
    curLoop = -1

    while 1:
        if curLine >= len(lines):  # reached max line
            if curLoop == -1:
                break
            else:
                if loops[curLoop][0] == 0:
                    break
                else:
                    curLine = loops[curLoop][1]
                    loops[curLoop][0] -= 1
                    loops[curLoop][3] += 1  # iter += 1
                    print(
                        f'{"    " * (loops[curLoop][2] - 1) + "  "}- iter {loops[curLoop][3]}:', file=out)
                    continue

        l_ = lines[curLine]
        l = l_.lstrip()
        depth = (len(l_) - len(l)) // 4

        if maxDepth != -1:
            if depth > maxDepth:
                continue

        if curLoop != -1:
            if loops[curLoop][0] == 0:
                del loops[curLoop]
                curLoop -= 1
            else:
                if depth < loops[curLoop][2]:
                    curLine = loops[curLoop][1]  # change to loop start
                    loops[curLoop][0] -= 1  # decrement the remaining count
                    loops[curLoop][3] += 1  # iter += 1
                    print(
                        f'{"    " * (loops[curLoop][2] - 1) + "  "}- iter {loops[curLoop][3]}:', file=out)
                    continue

        if len(scope) <= depth:
            scope.append({})
        vars = scope[depth]

        print(f"{'    ' * depth + '- '}", end='', file=out)

        if not l.startswith('* '):
            print('error', l_)
            break

        l = l[2:]  # remove `* `

        if l.startswith('if'):
            expr = l.replace(' ', '')[3:-2]
            expr_replaced, result = calc_expr(scope, depth, expr)
            print(
                f'Expression "{expr}" => "{expr_replaced}" returns {result}', file=out)
            if not result:
                maxDepth = depth
            else:
                maxDepth = -1

            curLine += 1
            continue
        elif l.endswith('times:'):
            expr = re.search(r"`(.+)` times:", l).group(1)
            expr2, result = calc_expr(scope, depth, expr)
            print(f'{result} times:', file=out)
            if result == 0:
                maxDepth = depth
            else:
                curLoop += 1
                loops.append([result-1, curLine+1, depth+1, 0])
                maxDepth = -1
                print(f'{"    " * depth + "  "}- iter 0:', file=out)

            curLine += 1
            continue

        name, t = l.split('.')[0].replace("`", "").split(": ")

        if '[' in t:  # list
            t, count_expr = t.replace(']', '').split('[')
            _, count = calc_expr(scope, depth, count_expr)
            vals = [getVal(r, t) for _ in range(count)]
            vars[name] = [x[0] for x in vals]
            print(
                f'{name}: {t} x "{count_expr}" ({count}) = [{", ".join([str(x[1]) for x in vals])}]', end='', file=out)
        else:  # plain value
            realVal, val = getVal(r, t)

            print(f'{name}: {t} = {val}', end='', file=out)

            vars[name] = realVal

        print(file=out)

        curLine += 1

    print(scope)

    out.close()


if __name__ == "__main__":
    script = Path(sys.argv[1])
    for arg in sys.argv[2:]:
        out = Path(arg + "_" + script.stem + ".txt")
        arg = Path(arg)
        print(f"Processing {arg} -> {out} with {script}")
        read(script, arg, out)
