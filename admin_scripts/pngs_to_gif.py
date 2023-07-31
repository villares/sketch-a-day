#!/usr/bin/env python
"""
Create GIF from PNG files in a directory!
"""
from pathlib import Path
from PIL import Image, GifImagePlugin
import argparse

parser = argparse.ArgumentParser(prog='PNG frames to GIF animation')
parser.add_argument('-i', '--input', help='Input folder containing the PNG images')
parser.add_argument('-o', '--output', default='output.gif', help='Output GIF file name')
parser.add_argument('-d', '--duration', default=200, type=int, help='Frame duration in milliseconds')
parser.add_argument('-NO', '--no-optimization', action='store_true', help='Turn off optimization')
parser.add_argument('-l', '--loop', default=0, type=int, help='Number of loops (default=0, keep looping)')

args = parser.parse_args()

input_dir = Path(args.input or Path.cwd())
if input_dir.is_dir():
    images = [Image.open(file_path) for file_path
              in sorted(input_dir.iterdir())
              if file_path.suffix.lower() == '.png']
    if images:
        output_path = input_dir / args.output
        images[0].save(
            output_path,
            save_all=True, append_images=images[1:],
            optimize=not args.no_optimization,
            duration=args.duration,
            loop=args.loop
            )
        print(f'Animation saved at:\n'
              f'{output_path}\n'
              #f'Optimization: {not args.no_optimization}'
              )
    else:
        print(f'No PNG images found at:\n{input_dir}')
else:
    print(f'{input_dir}\nis not a valid input dir.')

