# https://genuary.art/prompts#jan2
# Dithering

from itertools import product

grid = product(range(200), repeat=2)

def element(pos, step=4):
    i, j = pos
    h = int(random(i * j / 100.0))
    if h < 20 or i % 2 and j % 2:
        fill(0)
        rect(i * step, j * step,
          step, step / 2)
    elif h < 50:
        fill(255)
        rect(i * step, j * step,
          step / 2, step)
    elif  i % 2 or j % 2:
        fill(0)
        rect(i * step, j * step,
          step, step)

def setup():
    size(900, 900)
    background(0, 0, 200)
    noStroke()
    translate(50, 50)
    map(element, grid)
        
