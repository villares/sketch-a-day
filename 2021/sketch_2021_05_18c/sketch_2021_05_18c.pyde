from itertools import product
from random import sample


def setup():
    global grid, elements
    size(700, 700)
    grid = list(product(range(100, width, 125), repeat=2))
    elements = generate()

def generate():
    elements = []
    points = set()
    while len(points) < 24:
        a, b = sample(grid, 2)
        if a not in points and b not in points:
            points.add(a)
            points.add(b)
            elements.append(Element(a, b))
    return elements
       
def draw():
    background(240)
    for e in elements:
        e.display()

def keyPressed():
    if key  == 's':
        saveFrame(str(frameCount) + '.png')
    elements[:] = generate()

class Element:
    
    def __init__(self, a, b):
        self.p1 = PVector(*a)
        self.p2 = PVector(*b)
        n = 16 
        divs = lambda i: PVector.lerp(self.p1, self.p2, i / float(n))
        self.points = [divs(i) for i in range(n)] + [self.p2]
        
    def display(self):
        for p in self.points :
            for e in reversed(elements):
                if e == self:
                    break
                for ep in e.points:
                    d = dist(p.x, p.y, ep.x, ep.y)
                    if  d <= 125:
                        stroke(0, 0, d, 155 - d)
                        line(p.x, p.y, ep.x, ep.y) 
            fill(0)
            noStroke()
            circle(p.x, p.y, 4)
            
