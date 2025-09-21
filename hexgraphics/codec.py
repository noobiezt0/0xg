from PIL import Image
from typing import BinaryIO, IO
from os import PathLike
import zlib

from .constants import colormap

class Codec0xg:
    def __init__(self, data: BinaryIO | bytes | bytearray) -> None:
        if isinstance(data, bytes | bytearray):
            self.file = data
        else:
            self.file = zlib.decompress(data.read())

        self.data = self.file.split(b'\x10')
        self.w = len(self.data[0])
        self.h = len(self.data)

    def save(self, fp):
        with open(fp, 'wb') as file:
            file.write(zlib.compress(b'\x10'.join(self.data)))

    def convert(
            self,
            fp: str | bytes | PathLike[str] | PathLike[bytes] | IO[bytes]
    ) -> None:
        image = Image.new('RGB', (self.w, self.h))

        for x in range(self.w):
            for y in range(self.h):
                image.putpixel((x, y), COLORMAP(self.data[y][x]))
        image.save(fp)
