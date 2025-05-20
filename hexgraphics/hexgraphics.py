from PIL import Image
from typing import BinaryIO
from os import PathLike

class Image0xg:
    def __init__(self, file: BinaryIO):
        self.file = file
        self.data = self.file.read().split(b'\x10')
        self.w = len(self.data[0])
        self.h = len(self.data)
        self._colormap = {
            0x00: (0, 0, 0),
            0x01: (128, 0, 0),
            0x02: (0, 128, 0),
            0x03: (128, 128, 0),
            0x04: (0, 0, 128),
            0x05: (128, 0, 128),
            0x06: (0, 128, 128),
            0x07: (192, 192, 192),
            0x08: (128, 128, 128),
            0x09: (255, 0, 0),
            0x0a: (0, 255, 0),
            0x0b: (255, 255, 0),
            0x0c: (0, 0, 255),
            0x0d: (255, 0, 255),
            0x0e: (0, 255, 255),
            0x0f: (255, 255, 255),
        }

    def save_png(self, out: str | PathLike[str]) -> None:
        image = Image.new('RGB', (self.w, self.h))
        pixels = image.load()
        for x in range(self.w):
            for y in range(self.h):
                pixels[x, y] = self._colormap.get(self.data[y][x], (0, 0, 0))
        image.save(out)
