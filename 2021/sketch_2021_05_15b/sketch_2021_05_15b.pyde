from itertools import product
from random import sample

elements = []

def setup():
    global grid
    size(600, 600)
    grid = list(product(range(100, width, 200), repeat=2))
    generate()

def generate():
    elements[:] = []
    for _ in range(10):
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
        n = int(PVector.dist(self.p1, self.p2) // 20)
        divs = lambda i:PVector.lerp(self.p1, self.p2,(i + 1.0)/(n + 1))
        self.points = [self.p1] + [divs(i) for i in range(n)] + [self.p2]
        
    def display(self):
        for e in reversed(elements):
            if e == self:
                break
            for p in self.points :
                fill(0)
                circle(p.x, p.y, 3)
                for ep in e.points:
                    d = dist(p.x, p.y, ep.x, ep.y)
                    if  d < 100:
                        stroke(0, d + 155)
                        line(p.x, p.y, ep.x, ep.y) 
        
            
