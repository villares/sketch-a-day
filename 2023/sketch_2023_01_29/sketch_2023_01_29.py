# Kate Rose Morley's palette
# https://iamkate.com/data/12-bit-rainbow/

from random import sample
from itertools import product

palette = (
    '#817', '#a35', '#c66', '#e94',
    '#ed0', '#9d5', '#4d8', '#2cb',
    '#0bc', '#09c', '#36b', '#639'
    )

def setup():
    global palavras
    size(800, 800)
    no_loop()
    rect_mode(CENTER)
    no_stroke()

def draw():
    w = 100
    for x, y in product(range(0, width, w), repeat=2):
        d = width // w
        cores = sample(palette, d)
        for z in range(d):
            fill(cores[z])
            square(w / 2 + x, w / 2 + y, w / (z / 2 + 1))
        
def key_pressed():
    redraw()