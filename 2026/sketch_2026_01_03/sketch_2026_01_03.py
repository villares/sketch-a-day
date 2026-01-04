from collections import deque

import py5
import py5_tools

squares = deque(maxlen = 100)
squares.extend([
    (10, 10, 10),
    (10, 20, 10),
    ])

def setup():
    py5.size(990, 614)

def add_square():
    ax, ay, aw = squares[-2]
    bx, by, bw = squares[-1]
    cw = aw + bw
    if ay + aw == by + bw:
        cx = ax
        cy = ay + aw
    else:
        cx = ax + aw
        cy = ay
    squares.append((cx, cy, cw))
    print(cw)
    
def draw():
    py5.background(0)
    py5.no_fill() 
    py5.stroke_weight(2)
    py5.stroke(255)    
    _, _, w0 = squares[-1]
    py5.scale(1 / 10)
    py5.stroke_weight(10)
    if py5.frame_count % 10 == 0 and w0 < py5.width * 10:
        add_square()
    for x, y, w in squares:
        py5.square(x, y, w)

py5.run_sketch(block=False)

