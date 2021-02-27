from random import choice
from collections import deque

walkers = deque([[0, 0]], maxlen=20)

def setup():
    size(600, 600)
    background(0)
    colorMode(HSB)
    
def draw():
    translate(width / 2, height / 2)
    for x, y in reversed(walkers):
        if random(100) > 99:
            walkers.append([x, y])
        
    for i, w in enumerate(walkers):
        stroke(i * 16 % 255, 200, 200)    
        x, y = w
        circle(x, y, 3)
        w[0] += choice((-10, 0, 10))
        w[1] += choice((-10, 0, 10))
        line(x, y, w[0], w[1])
    
