import py5
from random import choice
#from villares.helpers import save_png_with_src

options = [8, 16, 24, 32, 48]

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
    py5.size(1000, 1000)
    py5.color_mode(py5.HSB)
    py5.no_stroke()
    py5.no_loop()

def draw():
    w = py5.width / 10
    ca = make_nr_choice(options, 4)
    cb = make_nr_choice(options, 4)

    for xi in range(10):
        ch = cb
        if xi % 2:
            ch = ca
        y = 0
        while y < py5.height:
            c = ch()
            print(c)
            py5.fill(c * 2, 200, 150 + c * 2)
            py5.rect(xi * w, y, w, (c + 8))
            y += c
        c = cb()
        py5.fill(c * 2, 200, 150 + c * 2)
        py5.rect(xi * w, 0, (c + 8)/2, py5.height)
        
def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')
    #    save_png_with_src()
    py5.redraw()

py5.run_sketch()

