#!/home/villares/thonny-env/bin/python
"""
Create a GIF animation from PNG files in a directory!

This script can be copied, modified and distributed without any restrictions.
I offer it with a "public domain dedication" / CC0.

Support my work! Alexandre B A Villares <abav.lugaralgum.com/sketch-a-day>
"""
from pathlib import Path
import argparse

import imageio                   # `pip install imageio`
from pygifsicle import gifsicle  # `pip install pygifsicle`


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
parser.add_argument(
    '-c', '--colors', default=0, type=int,
    help='Optimize with gifsicle (default=0, will not run gifsicle)',
    )

args = parser.parse_args()

input_dir = Path(args.input or Path.cwd())
if not input_dir.is_dir():
    print(f'{input_dir}\nis not a valid input dir.')
    exit()
    
try:
    images = [imageio.v3.imread(file_path)
              for file_path in sorted(input_dir.iterdir())
              if file_path.suffix.lower() == '.png']
    if images:
        output_path = input_dir / args.output
        imageio.v3.imwrite(
            output_path,
            images,
            duration=int(args.duration),
            loop=args.loop,
            )
        print(f'Animation saved at:\n{output_path}\n')
        if args.colors:
            gifsicle(
                sources=output_path,
                # destination=optimized_file,  # replacing in place!
                optimize=True, # Whether to add the optimize flag or not
                colors=args.colors, # Number of colors to use
                # options=["--verbose"]
            )
            print(f'Optimized with gifscile for {args.colors} colors.')
    else:
        print(f'No PNG images found at:\n{input_dir}')
except Exception as e:
    if str(e).startswith('all input arrays'):
        print('Select only images of same size.')
    else:    
        print(str(e))


