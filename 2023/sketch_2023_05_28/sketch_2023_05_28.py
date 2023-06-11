# based on https://botsin.space/@bitartbot/110448213578682186

import numpy as np
import py5

order = 500

def setup():
    py5.size(1000, 1000)
    py5.no_smooth()
    x, y = np.meshgrid(np.arange(0, order), np.arange(0, order))

    pattern = func(x, y)
    #print(pattern)
    img = py5.create_image_from_numpy(pattern * 255, 'L')
    py5.image(img, 0, 0, py5.width, py5.height)
    py5.save('out.png')

@np.vectorize
def func(x, y):
    try:
        return (~(int((x & y) / (x ^ 8)) | ((y * 10) % (~x)))) % 3 > 0
    except ZeroDivisionError:
        return 0

py5.run_sketch(block=False)
