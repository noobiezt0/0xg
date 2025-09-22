from PIL import Image
from typing import BinaryIO
from os import PathLike
import zlib

from .constants import COLORMAP

class Codec:
    def __init__(self, data: BinaryIO | bytes | bytearray) -> None:
        if isinstance(data, bytes | bytearray):
            self.data = data
        else:
            self.data = zlib.decompress(data.read())
        self.mode = self.data[0]
        self.width = self.data[1]
        self.height = self.data[2]
        self.data = self.data[3:]
        self.image = [self.data[i:i + self.width] for i in range(0, len(self.data), self.width)]

    def convert(self) -> Image:
        if self.mode == 0:
            image = Image.new('RGB', (self.width, self.height))
        else:
            image = Image.new('L', (self.width, self.height))
        for y, r in enumerate(self.image):
            for x, c in enumerate(r):
                if self.mode == 0:
                    color = COLORMAP[c]
                else:
                    color = c
                image.putpixel((x, y), color)
        return image

    def __bytes__(self):
        return zlib.compress(bytes([self.width, self.height]) + self.data)
