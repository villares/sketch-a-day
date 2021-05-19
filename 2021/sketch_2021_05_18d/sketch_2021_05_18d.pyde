from itertools import product
from random import sample, seed

def setup():
    global grid, points_a, points_b
    size(700, 700)
    grid = list(product(range(100, width, 125), repeat=2))
    seed(1)
    points_a = sample(grid, 24)
    points_b = sample(grid, 24)

def draw():
    background(240)
    t = sigmoid_easing((1 - cos(radians(frameCount))) / 2)
    points = lerpPoints(points_a, points_b, t)
    elements = Element.generate(points)
    for e in elements:
        e.display(elements)
    # if frameCount < 360:
    #     if frameCount % 3 == 0:
    #         saveFrame("###.png")

def keyPressed():
    if key  == 's':
        saveFrame(str(frameCount) + '.png')
    points_a[:] = sample(grid, 24)

def lerpPoints(points_a, points_b, t):
    return [(lerp(a[0], b[0], t), lerp(a[1], b[1], t))
            for a, b in zip(points_a, points_b)]

class Element:
    
    def __init__(self, a, b):
        self.p1 = PVector(*a)
        self.p2 = PVector(*b)
        n = 16 
        divs = lambda i: PVector.lerp(self.p1, self.p2, i / float(n))
        self.points = [divs(i) for i in range(n)] + [self.p2]
        
    def display(self, elements):
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

    @classmethod
    def generate(cls, points):
        points = iter(points)
        return [cls(a, next(points)) for a in points]
  
def sigmoid_easing(p):
    m = lerp(-10, 10, p)
    r = 1 / (1 + exp(-m))            
    if r < 0.001: return 0
    elif r > 0.999: return 1
    else: return r
