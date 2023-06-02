import numpy as np
import py5

order = 500
power = 59

def setup():
    global color_map, x, y
    py5.size(1000, 1000)
    py5.no_smooth()
    
    color_map = np.array([
        [py5.red(hsb(i)), py5.green(hsb(i)), py5.blue(hsb(i))]
        for i in range(256)])
    x, y = np.meshgrid(np.arange(0, order), np.arange(0, order))

def draw():
    py5.background(0)
    pattern = func(x, y)
    img = py5.create_image_from_numpy(color_map[pattern], 'RGB')
    py5.image(img, 0, 0, py5.width, py5.height)

def hsb(h, sat=255, bri=255):
    py5.color_mode(py5.HSB)
    return py5.color(h, sat, bri)

@np.vectorize
def func(x, y):
    return int((x ^ y) ** (power / 10)) % 256

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

