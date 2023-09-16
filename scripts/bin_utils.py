import struct
from typing import Literal


class BinReader():
    def __init__(self, binary: bytes, byteorder: Literal['big', 'little']) -> None:
        self.pos = 0
        self.binary = binary
        self.byteorder = byteorder  # endianness

    def goto(self, val: int) -> None:
        self.pos = val

    # increase the current position
    def skip(self, val: int) -> None:
        self.pos += val

    def i32(self) -> int:
        ret = int.from_bytes(
            self.binary[self.pos:self.pos+4], self.byteorder, signed=True)
        self.skip(4)
        return ret

    def u32(self) -> int:
        ret = int.from_bytes(
            self.binary[self.pos:self.pos+4], self.byteorder, signed=False)
        self.skip(4)
        return ret

    def i16(self) -> int:
        ret = int.from_bytes(
            self.binary[self.pos:self.pos+2], self.byteorder, signed=True)
        self.skip(2)
        return ret

    def u16(self) -> int:
        ret = int.from_bytes(
            self.binary[self.pos:self.pos+2], self.byteorder, signed=False)
        self.skip(2)
        return ret

    def i64(self) -> int:
        ret = int.from_bytes(
            self.binary[self.pos:self.pos+8], self.byteorder, signed=True)
        self.skip(8)
        return ret

    def u64(self) -> int:
        ret = int.from_bytes(
            self.binary[self.pos:self.pos+8], self.byteorder, signed=False)
        self.skip(8)
        return ret

    def i8(self) -> int:
        ret = int.from_bytes([self.binary[self.pos]],
                             self.byteorder, signed=True)
        self.skip(1)
        return ret

    def u8(self) -> int:
        ret = int.from_bytes([self.binary[self.pos]],
                             self.byteorder, signed=False)
        self.skip(1)
        return ret

    def f32(self) -> float:
        [ret] = struct.unpack('>f' if self.byteorder ==
                              'big' else '<f', self.binary[self.pos:self.pos + 4])
        self.skip(4)
        return ret

    def raw(self, len: int) -> bytes:
        ret = self.binary[self.pos:self.pos+len]
        self.pos += len
        return ret

    def string(self, len_: int, strip_null_byte: bool = True) -> str:
        val = self.raw(len_)
        if 0x0 in val and strip_null_byte:
            val = val[:val.find(0x0)]
            # self.pos -= (len_ - len(val))
        return val.decode()

    def length(self) -> int:
        return len(self.binary)
