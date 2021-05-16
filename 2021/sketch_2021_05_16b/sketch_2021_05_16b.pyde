from itertools import product
from random import sample

elements = []

def setup():
    global grid
    size(700, 700)
    grid = list(product(range(100, width, 250), repeat=2))
    generate()

def generate():
    pairs = set()
    while len(pairs) < 10:
        pair = tuple(sample(grid, 2))
        if pair not in pairs:
            pairs.add(pair)
    elements[:] = [Element(*pair)
                   for pair in pairs]
        
def draw():
    background(240)
    for e in elements:
        e.display()

def keyPressed():
    if key  == 's':
        saveFrame(str(frameCount) + '.png')
    generate()

class Element:
    
    def __init__(self, a, b):
        self.p1 = PVector(*a)
        self.p2 = PVector(*b)
        n = 20 
        divs = lambda i: PVector.lerp(self.p1, self.p2, i / float(n))
        self.points = [divs(i) for i in range(n)] + [self.p2]
        
    def display(self):
        for e in reversed(elements):
            if e == self:
                break
            for p in self.points :
                fill(0)
                noStroke()
                circle(p.x, p.y, 4)
                for ep in e.points:
                    d = dist(p.x, p.y, ep.x, ep.y)
                    if  d < 150:
                        stroke(0, 0, 255 - d, 255 - d)
                        line(p.x, p.y, ep.x, ep.y) 
        
            
