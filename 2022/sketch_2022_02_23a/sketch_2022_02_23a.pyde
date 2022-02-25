from itertools import product, permutations

quads = sorted(set(permutations([1, 0] * 4, 4)))

def setup():
    size(600, 600)
    print len(quads)
    for p in quads:
        print p
    a = Module(10, 10, (1, 2, 3, 4))
    a.plot()

class Module:
    q_size = 6
    
    def __init__(self, i, j, vals):
        self.i = i
        self.j = j
        self.vals = vals
        
    def plot(self):
        fill(0)
        stroke(255)
        textAlign(CENTER, CENTER)
        q = self.q_size
        pos = product((-q, q), repeat=2)
        x = self.i * q * 4
        y = self.j * q * 4
        vals = list(self.vals)
        line(x - q * 2, y, x + q * 2, y)
        line(x, y - q * 2, x, y + q * 2)
        for xi, yj in pos:
            text(vals.pop(), x + xi, y + yj)
        
        
        
        
        
        
        
