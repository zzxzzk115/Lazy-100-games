#!/usr/bin/env python3
"""Extract the plain-text .lz100 cart hidden inside a .lz100.png cartridge.

The cart PNG (see Lazy-100's cartpng) stores: magic 'LZ1P' + rawLen + rleLen + RLE bytes,
one byte per pixel in the low 2 bits of each RGBA channel. This mirrors the C++ decoder so a
GitHub Action can post a cart's real source on a PR without building the console.

    python3 scripts/lz100png_decode.py games/<id>/<id>.lz100.png
"""
import sys
from PIL import Image

MAGIC = b"LZ1P"


def _byte(rgba, i):
    o = i * 4
    return (rgba[o] & 3) | ((rgba[o + 1] & 3) << 2) | ((rgba[o + 2] & 3) << 4) | ((rgba[o + 3] & 3) << 6)


def _rle_decode(data, raw_len):
    out = bytearray()
    i, n = 0, len(data)
    while i < n:
        c = data[i]; i += 1
        if c == 0:  # 0x00, byte, lo, hi  ->  byte repeated (lo | hi<<8) times
            if i + 3 > n:
                break
            b = data[i]; cnt = data[i + 1] | (data[i + 2] << 8); i += 3
            out.extend(bytes([b]) * cnt)
        else:
            out.append(c)
    return bytes(out[:raw_len])


def decode(path):
    rgba = Image.open(path).convert("RGBA").tobytes()
    total = len(rgba) // 4
    if total < 12:
        raise ValueError("image too small to hold a cart")
    header = bytes(_byte(rgba, i) for i in range(12))
    if header[0:4] != MAGIC:
        raise ValueError("not a lazy-100 cart PNG (bad magic)")
    raw_len = int.from_bytes(header[4:8], "little")
    rle_len = int.from_bytes(header[8:12], "little")
    if 12 + rle_len > total:
        raise ValueError("truncated payload")
    rle = bytes(_byte(rgba, 12 + i) for i in range(rle_len))
    text = _rle_decode(rle, raw_len)
    if len(text) != raw_len:
        raise ValueError("length mismatch (corrupt payload)")
    return text.decode("utf-8", errors="replace")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: lz100png_decode.py <cart.lz100.png>")
    sys.stdout.write(decode(sys.argv[1]))
