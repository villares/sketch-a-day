#!/home/villares/thonny-env/bin/python
"""
GIF to MP4 conversion. Depends on moviepy 2.x and ffmpeg.

This script can be copied, modified and distributed without any restrictions.
I offer it with a "public domain dedication" / CC0.

Support my work! Alexandre B A Villares <abav.lugaralgum.com/sketch-a-day>
"""
import argparse

from moviepy import VideoFileClip  # moviepy 2.x

parser = argparse.ArgumentParser(prog='Create a MP4 video from a GIF animation. Depends on moviepy and ffmpeg.')
parser.add_argument('-i', '--input', help='Input .gif file.')
parser.add_argument('-o', '--output', default='output.mp4', help='Optional output file name. The default is "output.mp4"')
parser.add_argument('-r', '--fps', default=None, type=int, help="To change the frame rate. Input GIF's frame rate used by default, or 10 FPS if it can't be read.")

args = parser.parse_args()

if args.input is None:
    print('No input file provided. Use -h for usage help.')
elif str(args.input).lower().endswith('.gif'):
    try:
        gif_input = VideoFileClip(args.input)
        # H.264 with yuv420p needs even width and height
        w, h = gif_input.size
        if w % 2 or h % 2:
            gif_input = gif_input.resize(newsize=(w - w % 2, h - h % 2))
        fps = args.fps or gif_input.fps or 10
        gif_input.write_videofile(
            args.output,
            fps=fps,
            codec='libx264',
            audio=False,  # GIFs have no sound
            ffmpeg_params=['-pix_fmt', 'yuv420p'],
        )
        gif_input.close()
    except Exception as error:
        print(error)
else:
    print(f'{args.input}\nis not a valid input file.')
