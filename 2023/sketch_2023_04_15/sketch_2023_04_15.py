import py5
from random import choice
#from villares.helpers import save_png_with_src

options = [5, 12.5, 20, 27.5, 35]

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
    py5.stroke_weight(0.5)
    py5.no_loop()

def draw():
    h = py5.height / 5
    for nr in range(5):
        if nr == 0:
            nr_choice = lambda : choice(options)
        else:
            nr_choice = make_nr_choice(options, nr)
        x = 0
        while x < py5.width:
            c = nr_choice()
            py5.fill(c * 5, 200, 200)
            py5.rect(x, nr * h, c, h)
            x += c

def key_pressed():
    #save_png_with_src()
    py5.redraw()

py5.run_sketch()
