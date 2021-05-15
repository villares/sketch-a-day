from itertools import product
from random import sample

elements = []

def setup():
    global grid
    size(700, 700)
    grid = list(product(range(100, width, 125), repeat=2))
    generate()

def generate():
    elements[:] = []
    for _ in range(20):
        a, b = sample(grid, 2)
        e = Element(a, b)
        elements.append(e)

        
def draw():
    background(240)
    for e in elements:
        e.display()

def keyPressed():
    generate()


class Element:
    
    def __init__(self, a, b):
        self.p1 = PVector(*a)
        self.p2 = PVector(*b)
        n = 20
        divs = lambda i:PVector.lerp(self.p1, self.p2,(i + 1.0)/(n + 1))
        self.points = [divs(i) for i in range(n)]
        
    def display(self):
        for e in reversed(elements):
            if e == self:
                break
            for p in self.points + [self.p1, self.p2]:
                fill(0)
                circle(p.x, p.y, 3)
                for ep in e.points:
                    if dist(p.x, p.y, ep.x, ep.y) < 75:
                        line(p.x, p.y, ep.x, ep.y) 
        
            
