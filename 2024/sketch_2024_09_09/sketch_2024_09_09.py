import random
import py5
import numpy as np

# def random_walk(n):
#     from itertools import accumulate
#     # Only available from Python 3.6
#     steps = random.choices([-1,+1], k=n)
#     return [0]+list(accumulate(steps))

def random_walk(n=1000):
    # not returning the initial 0 :(
    steps = np.random.choice([-1,+1], n)
    return np.cumsum(steps)

def setup():
    py5.size(1000, 1000)
    py5.no_loop()
    
def draw():
    global walk
    py5.background(200, 200, 240)
    py5.no_fill()
    py5.stroke(0,10)
    for _ in range(1000):
        walk = random_walk(1000)
        py5.begin_shape()
        py5.vertex(0, py5.height / 2) # fix for the lack o initial 0
        for i, y in enumerate(walk):
            py5.vertex(2 + i * 2, y * 2 + py5.height / 2)
        py5.end_shape()
        #print(walk[-1])

def key_pressed():
    if py5.key == ' ':
        py5.save_frame('out2.png')
        py5.redraw()

py5.run_sketch(block=False)
    
