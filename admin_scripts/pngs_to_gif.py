#! /usr/bin/python3
"""
Create GIF from PNG files in a directory!
"""
from pathlib import Path
from PIL import Image, GifImagePlugin
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Input folder containing the PNG images')
parser.add_argument('--output', default='out.gif', help='Output GIF file name')
parser.add_argument('--duration', default=200, type=int, help='Frame duration in milliseconds')
args = parser.parse_args()

input_dir = Path(args.input or Path.cwd())
if input_dir.is_dir():
    images = [Image.open(file_path) for file_path
              in sorted(input_dir.iterdir())
              if file_path.suffix.lower() == '.png']
    if images:
        images[0].save(
            input_dir / args.output,
            save_all=True, append_images=images[1:],
            optimize=True,
            duration=args.duration,
            loop=0
            )
    else:
        print(f'No PNG images found at:\n{input_dir}')
else:
    print(f'{input_dir}\nis not a valid input dir.')

