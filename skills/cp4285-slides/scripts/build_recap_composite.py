#!/usr/bin/env python3
"""Build one outlined 2×2 recap composite from four 16:9 slide captures."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image

PURPLE = (92, 45, 145)  # #5C2D91


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Combine four 16:9 slide captures into one outlined 2×2 recap image."
    )
    parser.add_argument("output", type=Path, help="Output PNG path")
    parser.add_argument(
        "inputs",
        nargs=4,
        type=Path,
        metavar="SLIDE",
        help="Four source slide capture paths in reading order",
    )
    parser.add_argument("--width", type=int, default=1920, help="Output width in pixels")
    parser.add_argument("--height", type=int, default=1080, help="Output height in pixels")
    parser.add_argument(
        "--outline-px",
        type=int,
        default=1,
        help="Purple outline thickness around each quadrant in pixels",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.width <= 0 or args.height <= 0 or args.width % 2 or args.height % 2:
        raise ValueError("Output width and height must be positive, even integers.")
    if args.outline_px < 0:
        raise ValueError("Outline thickness cannot be negative.")

    quadrant_width = args.width // 2
    quadrant_height = args.height // 2
    usable_width = quadrant_width - 2 * args.outline_px
    usable_height = quadrant_height - 2 * args.outline_px
    if usable_width <= 0 or usable_height <= 0:
        raise ValueError("Outline thickness is too large for the requested output size.")

    for source in args.inputs:
        if not source.is_file():
            raise FileNotFoundError(f"Source image not found: {source}")

    canvas = Image.new("RGB", (args.width, args.height), PURPLE)
    positions = [
        (0, 0),
        (quadrant_width, 0),
        (0, quadrant_height),
        (quadrant_width, quadrant_height),
    ]
    for source, (x, y) in zip(args.inputs, positions):
        with Image.open(source) as image:
            slide = image.convert("RGB").resize(
                (usable_width, usable_height), Image.Resampling.LANCZOS
            )
            canvas.paste(slide, (x + args.outline_px, y + args.outline_px))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, quality=95)
    print(f"Wrote {args.output} ({canvas.width}×{canvas.height})")


if __name__ == "__main__":
    main()
