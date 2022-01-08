from itertools import product
from random import sample

points, white_lines = [], []
margin = 100

def setup():
    size(600, 600)
    create_points()
    
def create_points():
    points[:] = []
    white_lines[:] = []
    grid = list(product(range(margin, width, margin), repeat=2))
    points.extend(sample(grid, 10))
    for p in points:
        for other in reversed(points):
            if p is other: 
                break
            xa, ya = p
            xb, yb = other
            if xa == xb or ya == yb:
                white_lines.append((xa, ya, xb, yb))

def draw():
    background(240)                    
    stroke(255)
    strokeWeight(3)
    for xa, ya, xb, yb in white_lines:
        line(xa, ya, xb, yb)
    stroke(0)
    strokeWeight(1)
    noFill()
    beginShape()
    curveVertex(*points[-1])
    for x, y in points:
        curveVertex(x, y)
    curveVertex(*points[0])
    curveVertex(*points[1])
    endShape(CLOSE)
            
def keyPressed():
    create_points()
