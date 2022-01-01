# https://genuary.art/prompts#jan1
# Draw 10000 of something.

from itertools import product

grid = product(range(100), repeat=2)

def element(pos, step=8):
    i, j = pos
    line(4+ i * step, j * step,
        i * step, j * step + random(i * -j / 100.0))

def setup():
    size(900, 900)
    translate(50, 50)
    map(element, grid)
        
