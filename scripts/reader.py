from pathlib import Path
import re
import argparse
from glob import glob
import itertools

import bin_utils


class Block():
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f'<Block start={self.start} end={self.end}>'

    def __repr__(self) -> str:
        return str(self)


class Loop():
    def __init__(self, start_line, depth, times_left, iter) -> None:
        self.start_line = start_line
        self.depth = depth
        self.times_left = times_left
        self.iter = iter


class Scope():
    def __init__(self) -> None:
        self.scope = []

    def check_depth(self, depth):
        if depth >= len(self.scope):
            d = depth
            while d >= len(self.scope):
                self.scope.append({})

    def get(self, name, depth):
        self.check_depth(depth)

        if depth < len(self.scope):
            d = depth
            while d >= 0:
                if name in self.scope[d]:
                    return self.scope[d][name]
                d -= 1

        return None

    def set(self, name, depth, val):
        self.check_depth(depth)

        self.scope[depth][name] = val


class Reader():
    def __init__(self, script) -> None:
        with open(script, 'r') as f:
            self.lines = [x for x in f.read().splitlines() if x.strip()]

        self.depth = 0
        self.endianness = ''
        self.blocks = {}
        self.r = None
        self.scope = Scope()
        self.base_depth = 0

    def write_addr(self):
        print(f'[{self.r.pos:08X}] ', end='', file=self.f)

    def write_line(self, line):
        self.f.write('    ' * (self.depth + self.base_depth) +
                     '- ' + line + '\n')

    def process_header(self, path):
        # script name
        line = self.lines.pop(0)
        if not line.startswith("# "):
            raise ValueError("The file should start with the '# SCRIPTNAME'")

        script_name = line[2:]
        print('[00000000] ', end='', file=self.f)
        self.write_line(f'Script: {script_name}')

        # endianness
        line = self.lines.pop(0)
        if not line.startswith("Endianness: "):
            raise ValueError("The 2nd line should contain the endianness")

        self.endianness = line.strip().replace("Endianness: ", "").lower()
        print('[00000000] ', end='', file=self.f)
        self.write_line(f'Endianness: {self.endianness}')

        skip = 0

        # skip bytes count (for data before 4CC)
        if self.lines[0].startswith("Skip"):
            skip = int(self.lines[0].lower().replace(' ', '')[4:])

        # open the binary reader
        with open(path, 'rb') as f:
            data = f.read()
        self.r = bin_utils.BinReader(data, self.endianness)
        addr = data.find(script_name[::-1].encode())
        if addr == -1:
            print(f'Could not find the script data in the file!')
            return False
        self.r.goto(addr - skip)
        print('[00000000] ', end='', file=self.f)
        self.write_line(f'Start at 0x{addr - skip:X}')

        # skip to the block start
        while not self.lines[0].startswith("##"):
            del self.lines[0]

        return True

    def read_blocks(self):
        start = 0
        has_block = False
        name = ''

        for i, l in enumerate(self.lines):
            if l.startswith("##"):
                if has_block:
                    self.blocks[name] = Block(start, i-1)
                name = l[3:]
                has_block = True
                start = i

        self.blocks[name] = Block(start, len(self.lines) - 1)

    def get_value(self, type):
        val = None
        valStr = ''

        match type:
            case 'u32':
                val = self.r.u32()
                valStr = f'{val} (0x{val:X})'
            case 'u16':
                val = self.r.u16()
                valStr = f'{val} (0x{val:X})'
            case '4CC':
                val = self.r.u32()
                valStr = f'0x{val:X} ("{bytes.fromhex(hex(val)[2:]).decode()}")'
            case 'STR32':
                l = self.r.u32()
                val = valStr = self.r.raw(l)
            case 'STR16':
                l = self.r.u16()
                val = valStr = self.r.raw(l)
            case 'u8':
                val = self.r.u8()
                valStr = f'{val} (0x{val:X})'
            case 'f32':
                val = valStr = self.r.f32()
            case 'DDS texture file':
                val = None
                valStr = '<raw data>'
            case 'ATTRIBS':
                nb = self.r.u32()
                for _ in range(nb):
                    t = self.r.u8()
                    var_type = self.r.u8()
                    offset = self.r.u8()
                valStr = "<data>"
            case _:
                if 'bytes' in type:
                    expr = type.replace(' ', '').replace('bytes', '')
                    _, l = self.eval_expr(expr)
                    val = self.r.raw(l)
                    valStr = ' '.join([f'{x:02X}' for x in val])
                else:
                    print(f'Unhandled type {type}')

        return val, valStr

    def read_value(self, name, type):
        val = None
        valStr = ''

        if '[' in type:
            arr_type, count_expr = type[:-1].split('[')
            _, count = self.eval_expr(count_expr)
            if arr_type in self.blocks.keys():
                self.write_line(f'{name}: {arr_type} x {count}:')
                d = self.depth + self.base_depth
                for i in range(count):
                    self.write_addr()
                    print("    " * d + f"  - item {i}:", file=self.f)
                    self.process_block(arr_type, d + 1)
            else:
                values = [self.get_value(arr_type) for _ in range(count)]

                val = [x[0] for x in values]
                valStr = f'[{", ".join([str(x[1]) for x in values])}]'
                type = f'{arr_type} x {count}'

                self.scope.set(name, self.depth + self.base_depth, val)
                self.write_line(f'{name}: {type} = {valStr}')
        else:
            if type in self.blocks.keys():
                self.write_line(f'{name}: {type}:')
                self.process_block(type, self.depth + 1)
            else:
                val, valStr = self.get_value(type)

                self.scope.set(name, self.depth + self.base_depth, val)
                self.write_line(f'{name}: {type} = {valStr}')

    def eval_expr(self, expr):
        expr_replaced = expr.replace("&&", " and ").replace("||", " or ")
        pattern = re.compile(r'\w+')
        for m in pattern.findall(expr_replaced):
            value = self.scope.get(m, self.depth + self.base_depth)
            if value is not None:
                expr_replaced = expr_replaced.replace(m, str(value))
        result = eval(expr_replaced)

        return expr_replaced, result

    def process_block(self, name, depth):
        block: Block = self.blocks[name]
        # print(f'Processing block {name} (lines {block.start} - {block.end})')

        bd = self.base_depth

        self.base_depth = depth

        max_depth = -1

        loops: list[Loop] = []
        cur_loop = -1

        conditional_results = []

        i = block.start + 1
        while True:
            if i > block.end:  # reached max line
                if cur_loop == -1:
                    break
                else:
                    loop = loops[cur_loop]
                    if loop.times_left == 0:
                        break
                    else:
                        i = loop.start_line
                        loop.times_left -= 1
                        loop.iter += 1
                        self.write_addr()
                        print(
                            f'{"    " * (loop.depth - 1 + self.base_depth) + "  "}- iter {loop.iter}:', file=self.f)

            # remove comments (they start with .)
            raw_l = self.lines[i].split(';')[0].rstrip()
            l = raw_l.lstrip()
            # count spaces at the beginning of the line, divide by 4 (indentation)
            self.depth = (len(raw_l) - len(l)) // 4
            l = l[2:]  # remove the '* '

            if not l:
                i += 1
                continue

            if max_depth != -1 and self.depth > max_depth:
                i += 1
                continue

            if max_depth != -1 and self.depth <= max_depth:
                max_depth = -1

            if cur_loop != -1:
                loop = loops[cur_loop]
                if loop.times_left == 0:
                    del loops[cur_loop]
                    cur_loop -= 1
                else:
                    if self.depth < loop.depth:
                        i = loop.start_line
                        loop.times_left -= 1
                        loop.iter += 1
                        self.write_addr()
                        print(
                            f'{"    " * (loop.depth - 1 + self.base_depth) + "  "}- iter {loop.iter}:', file=self.f)
                        continue

            # print(f'Line {i}: "{raw_l}" => "{l}"')

            if l.startswith('if'):
                # has a condition
                expr = l.replace(' ', '')[3:-2]
                expr_replaced, result = self.eval_expr(expr)
                if self.depth >= len(conditional_results):
                    conditional_results.extend(
                        [False] * (self.depth - len(conditional_results) + 1))
                conditional_results[self.depth] = result
                self.write_addr()
                self.write_line(
                    f'Condition "{expr}" => "{expr_replaced}" evaluates to {result}{":" if result else ""}')
                if result:
                    max_depth = -1
                else:
                    max_depth = self.depth
            elif l.startswith("else"):
                if not conditional_results[self.depth]:
                    self.write_addr()
                    self.write_line("Else:")
                    max_depth = -1
                else:
                    max_depth = self.depth
            elif l.startswith('elif'):
                if not conditional_results[self.depth]:
                    expr = l.replace(' ', '').replace('`', '')[4:-1]
                    # print("elif not handled i dont care", expr)
                    # print("elif not handled i dont care", file=self.f)
                    expr2, result = self.eval_expr(expr)
                    self.write_addr()
                    self.write_line(
                        f'Elif "{expr}" => "{expr2}" returned {result}{":" if result else ""}')
                    if result:
                        max_depth = -1
                    else:
                        max_depth = self.depth
                else:
                    max_depth = self.depth
            elif l.endswith('times:'):
                expr = l.replace(' ', '')[:-6].replace('`', '')
                _, count = self.eval_expr(expr)
                if count == 0:
                    max_depth = self.depth
                    self.write_addr()
                    self.write_line(
                        f'Loop ("{expr}" => 0 iterations, ignoring)')
                else:
                    loops.append(Loop(i + 1, self.depth + 1, count - 1, 0))
                    max_depth = -1
                    cur_loop += 1
                    self.write_addr()
                    self.write_line(f'Loop ("{expr}" => {count} iterations):')
                    self.write_addr()
                    print(
                        f'{"    " * (self.depth + self.base_depth)  + "  "}- iter 0:', file=self.f)
            elif ' = ' in l:
                name, val = l.replace('`', '').split(' = ')
                val = int(val)
                self.scope.set(name, self.depth + self.base_depth, val)
            else:
                self.write_addr()
                if l.endswith(':'):
                    self.write_line(l[1:-2] + ':')
                else:
                    name, t = [x.replace('`', '') for x in l.split(': ')]
                    self.read_value(name, t)

            i += 1

        self.base_depth = bd

    def process(self, file, out):
        # 1. read the header (script name, endianness)
        # 2. read all the blocks
        # 3. process main block

        self.f = open(out, 'w')

        # assuming the file starts with the header (# NAME, Endianness: ..., etc)
        if not self.process_header(file):
            print("[00000000] - Failed to find the block in the file!", file=self.f)
            self.f.close()
            return

        # read blocks
        self.read_blocks()

        print('[00000000]', file=self.f)

        # start by processing the main block
        self.process_block('Main', 0)
        self.write_addr()
        print("- Finished!", file=self.f)

        self.f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--scripts', nargs='+',
                        help='Specify script .md file(s). Supports glob expressions.')
    parser.add_argument('-i', '--input', nargs='+',
                        help='Specify input file(s). Supports glob expressions.')
    args = parser.parse_args()

    exclusions = ['MESH', 'TANB', 'IVL4']  # scripts it cant read

    # only use 4 letter named scripts to avoid confusion
    scripts = [x for x in list(itertools.chain(
        *[glob(x) for x in args.scripts])) if len(Path(x).stem) == 4 and not Path(x).stem in exclusions]
    inputs = list(itertools.chain(*[glob(x) for x in args.input]))

    for s in scripts:
        print(f'Using script {s}')
        r = Reader(s)
        for i in inputs:
            out = f'{i}_{Path(s).stem}.txt'
            print(f'Processing {i} => {out}')
            r.process(i, out)
