from itertools import product, permutations

msuads = sorted(set(permutations([1, 0] * 4, 4)))

SPACING = 1.5
MARGIN = 25
M_SIZE = 12
TL, TR, BL, BR = (-1, -1), (1, -1), (1, -1), (1, 1)
NBS = (
(-1, -1), (-1, 0), (-1, 1),
( 0, -1),          ( 0, 1),
( 1, -1), ( 1, 0), ( 1, 1)
)

def setup():
    size(200, 200)
    rect_mode(CENTER)
    positions = product(range(4), repeat=2)
    modules = []
    for i, j in positions:
        m = Module(i, j, [msuads.pop()])
        m.plot()
        modules.append(m)

class Module:
    
    def __init__(self, i, j, vals):
        self.i = i
        self.j = j
        self.vals = vals
        
    def plot(self):
#         text_align(CENTER, CENTER)
        stroke(128)
        ms = M_SIZE
        positions = product((ms / 2, -ms / 2), repeat=2)
        x = ms + self.i * ms * 2 * SPACING + MARGIN
        y = ms + self.j * ms * 2 * SPACING + MARGIN
        vals = list(self.vals[0])
#         line(x - ms, y, x + ms, y)
#         line(x, y - ms, x, y + ms)
        for xi, yj in positions:
            if vals.pop():
                fill(0)
            else:
                fill(255)
            square(x + xi, y + yj, ms)
            #text(vals.pop(), x + xi, y + yj)
        
        
        
        
        
        
        
