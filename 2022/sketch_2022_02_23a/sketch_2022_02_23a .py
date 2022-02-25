from itertools import product, permutations

quads = sorted(set(permutations([1, 0] * 4, 4)))

SPACING = 1.5
MARGIN = 50

def setup():
    size(200, 200)
    print(len(quads))
    positions = product(range(4), repeat=2)
    modules = []
    for i, j in positions:
        m = Module(i, j, quads.pop())
        m.plot()
        modules.append(m)

class Module:
    q_size = 6
    
    def __init__(self, i, j, vals):
        self.i = i
        self.j = j
        self.vals = vals
        
    def plot(self):
        fill(0)
        stroke(255)
        text_align(CENTER, CENTER)
        q = self.q_size
        positions = product((q, -q), repeat=2)
        x = self.i * q * 4 * SPACING + MARGIN
        y = self.j * q * 4 * SPACING + MARGIN
        vals = list(self.vals)
        line(x - q * 2, y, x + q * 2, y)
        line(x, y - q * 2, x, y + q * 2)
        for xi, yj in positions:
            text(vals.pop(), x + xi, y + yj)
        
        
        
        
        
        
        
