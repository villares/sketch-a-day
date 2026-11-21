#!/home/villares/thonny-env/bin/python
"""
MP4 to GIF animation. Depends on moviepy 2.x and ffmpeg.

This script can be copied, modified and distributed without any restrictions.
I offer it with a "public domain dedication" / CC0.

Support my work! Alexandre B A Villares <abav.lugaralgum.com/sketch-a-day>
"""
import argparse

from moviepy import VideoFileClip, CompositeVideoClip

parser = argparse.ArgumentParser(prog='Create a GIF animation from a MP4 file. Depends on moviepy and ffmpeg.')
parser.add_argument('-i', '--input', help='Input .mp4 file.')
parser.add_argument('-o', '--output', default='output.gif', help='Optional output file name. The default is "output.gif"')
parser.add_argument('-r', '--fps', default=10, type=int, help='To chage the frame rate. The default is 10 FPS.')

args = parser.parse_args()

if str(args.input).lower().endswith('.mp4'):
    try:
        mp4_input = VideoFileClip(args.input) #.subclip(0,2)
        result = CompositeVideoClip([mp4_input])
        result.write_gif(args.output, fps=args.fps, program='ffmpeg')
    except Exception as error:
        print(error)
elif args.input is None:
    print('No input file provided. Use -h for usage help.')
else:
    print(f'{args.input}\nis not a valid input file.')
