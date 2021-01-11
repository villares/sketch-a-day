"""
Based on PythagorasTree Task: Construct a Pythagoras tree of order 7
using only vectors (no rotation or trigonometric functions). 
https://rosettacode.org/wiki/Pythagoras_tree#Processing
Related task: Fractal tree (https://rosettacode.org/wiki/Fractal_tree)
2016-06-08 Trizen
2020-03-02 da8
2020-03-17 Alexandre Villares (porting to Python Mode)
"""

def setup():
    size(800, 400)
    background(0)
    tree(width / 2.3, height, width / 1.8, height, 10)
    save_image()

def tree(x1, y1, x2, y2, depth):
    r = lambda: random(-3, 3)
    
    if depth <= 0:
        return
    
    dx = (x2 - x1) + r()
    dy = (y1 - y2) + r()

    x3 = (x2 - dy) + r()
    y3 = (y2 - dx) + r()
    x4 = (x1 - dy) + r()
    y4 = (y1 - dx) + r()
    x5 = (x4 + 0.5 * (dx - dy)) + r()
    y5 = (y4 - 0.5 * (dx + dy)) + r()

    fill(100, 255.0 / depth, 100, 128 + 128.0 / depth)
    noStroke()

    # square
    beginShape()
    vertex(x1, y1)
    vertex(x2, y2)
    vertex(x3, y3)
    vertex(x4, y4)
    vertex(x1, y1)
    endShape()

    # triangle
    beginShape()
    vertex(x3, y3)
    vertex(x4, y4)
    vertex(x5, y5)
    vertex(x3, y3)
    endShape()

    tree(x4, y4, x5, y5, depth - 1)
    tree(x5, y5, x3, y3, depth - 1)


def save_image():
    from os import path
    sketch = sketchPath()
    name = path.basename(sketch)
    print(name)
    saveFrame('{}.png'.format(name))
