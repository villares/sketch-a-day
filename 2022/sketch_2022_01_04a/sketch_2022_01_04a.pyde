# https://genuary.art/prompts#jan4

from itertools import product

grid = product(range(200),
               repeat=2)

def element(pos, step=3):
    i, j = pos
    spacing = (i * j) // 100
    randomSeed(spacing)
    s = step + random(-2, 2) 
    stroke(16 + random(8) * 16, 200, 200)
    point(i * s, j * s)

def setup():
    size(900, 900)
    background(240)
    colorMode(HSB)
    translate(50, 50)
    strokeWeight(5)
    map(element, grid)
        
