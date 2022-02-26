from itertools import product, permutations
from random import shuffle

patterns = [  # TL, BL, TR, BR
#(1, 2, 3, 4),
(1, 1, 1, 1),
(1, 1, 0, 0),
(0, 0, 1, 1),
(1, 0, 0, 0),
(0, 1, 0, 0),
(0, 0, 1, 0),
(0, 0, 0, 1),
(0, 0, 0, 0), 
]

SPACING = 1
MARGIN = 50
M_SIZE = 15
TL, TR, BL, BR = (-1, -1), (1, -1), (1, -1), (1, 1)

NBS = (
(-1, -1), (-1, 0), (-1, 1),
( 0, -1),          ( 0, 1),
( 1, -1), ( 1, 0), ( 1, 1)
)

def setup():
    size(400, 400)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    positions = product(range(10), repeat=2) 
    
    modules = []
    for i, j in positions:
        #if patterns:
            #m = Module(i, j, [patterns.pop()])
            ptts = patterns[:]; shuffle(ptts)
            m = Module(i, j, ptts)
            m.plot()
            modules.append(m)

class Module:
    
    def __init__(self, i, j, vals):
        self.i = i
        self.j = j
        self.vals = vals
        
    def plot(self):
        stroke(128)
        ms = M_SIZE
        positions = product((ms / 2, -ms / 2), repeat=2)
        x = ms + self.i * ms * 2 * SPACING + MARGIN
        y = ms + self.j * ms * 2 * SPACING + MARGIN
        vals = list(self.vals[0])
        for xi, yj in positions:
            v = vals.pop()
            if v == 0:
                fill(0)
            elif v == 1:
                fill(255)
            else:
                fill(v * 32)
            square(x + xi, y + yj, ms)
            fill(255, 0, 0)
            #text(v, x + xi, y + yj)
        
        
        
        
        
        
        
