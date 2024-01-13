import py5
from random import choice
#from villares.helpers import save_png_with_src

options = [8, 16, 24, 32, 64]

def make_nr_choice(collection, avoid_last_num=1):
    from collections import deque
    if len(set(collection)) <= avoid_last_num:
        raise ValueError(
            f'Number of unique items in collection ({len(set(collection))}) must be '
            f'bigger than number of previous items to avoid repeating ({avoid_last_num})')
    def nr_choice(memory=deque([], avoid_last_num)):
        options = list(set(collection) - set(memory))
        chosen = choice(options)
        memory.append(chosen)
        return chosen
    return nr_choice

def setup():
    global w, h
    py5.size(1000, 1000)
    py5.color_mode(py5.HSB)
    py5.no_stroke()
    py5.no_loop()
    w = py5.width / 3
    h = py5.height / 60


def draw():
    ca = make_nr_choice(options, 3)
    cb = make_nr_choice(options, 3)
 
    for xi in range(10):
        y = 0
        while y < py5.height:
            cca = ca()
            ccb = cb()
            for xx, cc in enumerate((cca, ccb, cca, ccb)):
                py5.fill(cc * 2, 200, 200)
                py5.rect(xi * w + xx * w / 4, y, w, h)
            y += h

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    #    save_png_with_src()
    py5.redraw()

py5.run_sketch()

