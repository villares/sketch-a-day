#!/home/villares/thonny-env/bin/python
"""
MP4 to GIF animation. Depends on moviepy and ffmpeg.
"""
import argparse

from moviepy.editor import *

parser = argparse.ArgumentParser(prog='Create a GIF animation from a MP4 file. Depends on moviepy and ffmpeg.')
parser.add_argument('-i', '--input', help='Input .mp4 file.')
parser.add_argument('-o', '--output', default='output.gif', help='Optional output file name. The default is "output.gif"')
parser.add_argument('-r', '--fps', default=10, type=int, help='To chage frame rate. The default is 10 FPS')

args = parser.parse_args()

if str(args.input).lower().endswith('.mp4'):
    try:
        my_clip = VideoFileClip(args.input) #.subclip(0,2)
        result = CompositeVideoClip([my_clip])
        result.write_gif(args.output, fps=args.fps, program='ffmpeg')
    except Exception as error:
        print(error)
elif args.input is None:
    print('No input file provided. Use -h for usage help.')
else:
    print(f'{args.input}\nis not a valid input file.')
