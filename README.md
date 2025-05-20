# hexgraphics

aka 0xg


## installation

`pip install hexgraphics`


## usage

```
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
```

```python
import hexgraphics.hexgraphics as hg

with open('example.0xg', 'wb') as f:
    example = bytearray(
        [
            0x0e, 0x0e, 0x0e, 0x10,
            0x0e, 0x0b, 0x0e, 0x10,
            0x0e, 0x0e, 0x0e, 0x10,
            0x0a, 0x0a, 0x0a,
        ]
    )
    hg.Image0xg(f)

with open('example.0xg', 'rb') as f:
    hg.Image0xg(f).save_png('example.png')
```
