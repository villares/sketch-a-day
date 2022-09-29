#! /usr/bin/python3
"""
Create GIF from PNG files in the current working directory!
"""
from pathlib import Path
from PIL import Image, GifImagePlugin

images = [Image.open(file_path) for file_path
          in sorted(Path.cwd().iterdir())
          if file_path.suffix.lower() == '.png']
 
if images:
    images[0].save(
        'output.gif',
        save_all=True, append_images=images[1:],
        optimize=True,
        duration=200,
        loop=0
        )
else:
    print('No PNG images found!')
