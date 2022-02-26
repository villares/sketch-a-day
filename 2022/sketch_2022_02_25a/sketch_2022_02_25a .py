from itertools import product
from random import shuffle

patterns = [  # TL, BL, TR, BR (1, 2, 3, 4),
(1, 1, 1, 1), (1, 1, 0, 0), (0, 0, 1, 1), (1, 0, 0, 0),
(0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 0, 0), 
]

SPACING, MARGIN = 0.90, 50
M_SIZE = 22
TL, TR, BL, BR = (-1, -1), (1, -1), (1, -1), (1, 1)
modules = {}

def setup():
    size(500, 500)
    rect_mode(CENTER)
    text_align(CENTER, CENTER)
    positions = product(range(10), repeat=2) 
    for pos in positions:
            ptts = patterns[:]; shuffle(ptts)
            m = Module(pos, ptts)
            m.plot()
            modules[pos] = m

class Module:
    
    def __init__(self, p, vals):
        self.p = p
        self.vals = vals
        
    def plot(self):
        stroke(128)
        ms = M_SIZE
        corners = product((ms / 2, -ms / 2), repeat=2)
        x = ms + self.p[0] * ms * 2 * SPACING + MARGIN
        y = ms + self.p[1] * ms * 2 * SPACING + MARGIN
        vals = list(self.vals[0])
        for i, j in corners:
            v = vals.pop()
            fill(v * 255, 150)
            square(x + i, y + j, ms)
            fill(255, 0, 0)
            #text(v, x + i, y + j)
        
NBS = (
(-1, -1), (-1, 0), (-1, 1),
( 0, -1),          ( 0, 1),
( 1, -1), ( 1, 0), ( 1, 1)
)       
        
        
        
        
        
