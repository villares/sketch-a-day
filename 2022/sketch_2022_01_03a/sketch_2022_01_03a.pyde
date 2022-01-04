# https://genuary.art/prompts#jan3
# Space

from itertools import product

grid = product(range(200),
               repeat=2)

def element(pos, step=2):
    i, j = pos
    spacing = (i * j) // 400
    s = step + spacing
    point(i * s, j * s)

def setup():
    size(900, 900)
    background(0)
    stroke(0, 0, 200)
    translate(50, 50)
    map(element, grid)
        
