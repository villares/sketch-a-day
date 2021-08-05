from itertools import product
from random import sample
change_b = False
num_points = 24

def setup():
    global grid, points_a, points_b
    size(600, 600, P3D)
    grid = list(product(range(100, width, 100), repeat=3))
    points_a = sample(grid, num_points)
    points_b = sample(grid, num_points)
    for _ in range(num_points // 2):
        Element()

def draw():    
    global change_b
    ortho()
    background(240)
    t = brutal_sigmoid(radians(millis() / 200.0 % 360))
    
    translate(width / 2, height / 2,  -height )
    rotateX(TWO_PI * t)
    rotateY(radians(millis() / 50))
    translate(-width / 2, -height / 2, -height / 2)
    
    points = iter(lerp_tuple(points_a, points_b, t))        
    for e in Element.elements:
        e_start, e_end = next(points), next(points)
        e.update(e_start, e_end)            
    for e in Element.elements:
        e.display()

    if t == 0 and change_b:
        points_b[:] = sample(grid, num_points)
        change_b = False
    elif t == 1: 
        points_a[:] = sample(grid, num_points)
        change_b = True
 
class Element:

    elements = []
    
    def __init__(self):
        self.elements.append(self)
        
    def update(self, e_start, e_end, divisions=16):
        self.points = [lerp_tuple(e_start, e_end, i / float(divisions))
                       for i in range(divisions)] + [e_end]
        
    def display(self):
        for self_p in self.points :
            for other in reversed(self.elements):
                if other == self:
                    break
                for other_p in other.points:
                    d = dist(self_p[0], self_p[1], other_p[2], 
                             other_p[0], other_p[1], other_p[2])
                    if  d <= 100:
                        stroke(0, 0, d, 155 - d)
                        line(self_p[0], self_p[1], self_p[2], 
                             other_p[0], other_p[1], other_p[2]) 
            push()
            fill(0)
            noStroke()
            translate(0, 0, self_p[2])
            circle(self_p[0], self_p[1], 4)
            pop()
       
def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))

def brutal_sigmoid(angle):
    m = cos(angle) * 10
    r = 1 / (1 + exp(-m))            
    if r < 0.001: return 0
    elif r > 0.999: return 1
    else: return r
