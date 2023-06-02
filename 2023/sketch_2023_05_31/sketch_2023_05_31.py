# https://twitter.com/ntsutae/status/1521190629769826304?s=20

import numpy as np
import py5

power = 55

def setup():
    global color_map, x, y, t
    py5.size(512, 512)
    py5.no_smooth()
    py5.color_mode(py5.HSB)

    color_map = np.array([[0, 0, 0]] + [
        [py5.red(py5.color(i * 4, 255, 255)),
         py5.green(py5.color(i * 4, 255, 255)),
         py5.blue(py5.color(i * 4, 255, 255))]
        for i in range(64)])
    x, y = np.meshgrid(np.arange(0, py5.width), np.arange(0, py5.height))

def draw():
    f =  py5.frame_count
    pattern = func(x, y, f)
    py5.set_np_pixels(color_map[pattern], 'RGB')
    py5.window_title(f'{py5.get_frame_rate():.2f}')
    if f <= 256:
        py5.save_frame('###.png', use_thread=True)
    
@np.vectorize
def func(x, y, t): 
    value =  int((t + ((x ^ y) ** (power / 10))) % 256)
    return value if value < 32 else 0


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

