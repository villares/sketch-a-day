# https://twitter.com/ntsutae/status/1521190629769826304?s=20

import numpy as np
import py5

order = 500
power = 59
img = None

def setup():
    global x, y
    py5.size(1000, 1000)
    py5.no_smooth()
    x, y = np.meshgrid(np.arange(0, order), np.arange(0, order))

def draw():
    global img
    pattern = func(x, y, py5.frame_count / 2)
    img = py5.create_image_from_numpy(pattern * 255, 'L', dst=img)
    py5.image(img, 0, 0, py5.width, py5.height)
    py5.window_title(f'{py5.get_frame_rate():.2f}')


@np.vectorize
def func(x, y, t):
    return int((t + ((x ^ y) ** (power / 10))) % 256)  > 32

def key_pressed():
    global power
    if py5.key_code == py5.UP:
        power += 1
    elif py5.key_code == py5.DOWN:
        power = max(power - 1, 1)
    elif py5.key == 's':
        py5.save_frame(f'out{order}-{power}.png')
    print(power)

py5.run_sketch(block=False)

