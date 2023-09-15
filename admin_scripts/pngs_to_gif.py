#!/home/villares/miniconda3/bin/python
"""
Create GIF from PNG files in a directory!
"""
from pathlib import Path
import argparse

import imageio

parser = argparse.ArgumentParser(
    prog='PNG frames to GIF animation'
    )
parser.add_argument(
    '-i', '--input',
    help='Input folder containing the PNG images'
    )
parser.add_argument(
    '-o', '--output', default='output.gif',
    help='Output GIF file name'
    )
parser.add_argument(
    '-d', '--duration', default=200, type=int,
    help='Frame duration in milliseconds',
    )
parser.add_argument(
    '-l', '--loop', default=0, type=int,
    help='Number of loops (default=0, keep looping)',
    )

args = parser.parse_args()

input_dir = Path(args.input or Path.cwd())

if input_dir.is_dir():
    images = [imageio.v3.imread(file_path)
              for file_path in sorted(input_dir.iterdir())
              if file_path.suffix.lower() == '.png']
    if images:
        output_path = input_dir / args.output
        imageio.v3.imwrite(
            output_path,
            images,
            duration=int(args.duration) / 1000,
            loop=args.loop,
            )
        print(f'Animation saved at:\n' f'{output_path}\n')
    else:
        print(f'No PNG images found at:\n{input_dir}')
else:
    print(f'{input_dir}\nis not a valid input dir.')

