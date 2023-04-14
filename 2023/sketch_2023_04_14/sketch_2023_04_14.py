import py5
from random import choice

options = [10, 35, 50, 65, 80]

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
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
    nr_choice = make_nr_choice(options, 3)
    x = 0
    while x < py5.width:
        c = nr_choice()
        py5.fill(c * 3, 200, 200)
        py5.rect(x, 0, c, py5.height)
        x += c

py5.run_sketch()
