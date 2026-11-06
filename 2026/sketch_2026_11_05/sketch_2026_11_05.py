# The kal function is inspired by @introscopia's code

import numpy as np
import py5
from py5_tools import animated_gif

N = 6 # the kal number of axis control 

def setup():
    global img
    py5.size(800, 800)
    img = py5.load_image('a.png')
    img.load_np_pixels()
    animated_gif('out.gif',
                 frame_numbers=range(1, 361, 4),
                 duration=0.2
                 )

def draw():
    # calculating the kalidoscopic source positions
    w, h = py5.width, py5.height
    xs = np.linspace(-w / 2, w / 2, w)
    ys = np.linspace(-h / 2, h / 2, h)
    X, Y = np.meshgrid(xs, ys)
    kx, ky = kal(X, Y, N)
    # "circular" offsets to add to the source positions
    f = py5.radians(py5.frame_count)
    xo = 600 + int(py5.cos(f) * 200)
    yo = 600 + int(py5.sin(f) * 200)
    # limit to source size
    ix = np.clip(kx.astype(int) + xo, 0, img.width - 1)
    iy = np.clip(ky.astype(int) + yo, 0, img.height - 1)
    # getting the pixels!
    mapped_pixels = img.np_pixels[iy, ix]
    py5.set_np_pixels(mapped_pixels)
#    out = py5.create_image_from_numpy(mapped_pixels, 'ARGB')
#    py5.image(out, 0, 0)

def kal(x, y, N):
    r = np.hypot(x, y)
    angle = py5.atan2(y, x) % py5.TWO_PI
    theta = py5.TWO_PI / (2 * N)
    slice_num = np.floor(angle / theta).astype(int)
    angle = np.where(
        slice_num % 2,
        (slice_num + 1) * theta - angle,
        angle - slice_num * theta
    )
    return r * np.cos(angle), r * np.sin(angle)

def key_pressed():
    py5.save_frame('out.png')

py5.run_sketch()
