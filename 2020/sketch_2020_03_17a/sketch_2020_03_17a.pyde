"""
PythagorasTree
https://rosettacode.org/wiki/Pythagoras_tree#Processing
Processing 3.5.4
2016-06-08 Trizen
2020-03-02 da8
2020-03-17 Alexandre Villares (Python Mode)

Task: Construct a Pythagoras tree of order 7 using only vectors (no rotation or trigonometric functions).

Related tasks
 
Fractal tree (https://rosettacode.org/wiki/Fractal_tree)
"""

def setup():
    size(800, 400)
    background(255)
    stroke(0, 255, 0)
    tree(width / 2.3, height, width / 1.8, height, 10)
    save_image()

def tree(x1, y1, x2, y2, depth):
    if depth <= 0: return
    dx = (x2 - x1)
    dy = (y1 - y2)

    x3 = (x2 - dy)
    y3 = (y2 - dx)
    x4 = (x1 - dy)
    y4 = (y1 - dx)
    x5 = (x4 + 0.5 * (dx - dy))
    y5 = (y4 - 0.5 * (dx + dy))

    # square
    beginShape()
    fill(0.0, 255.0 / depth, 0.0)
    vertex(x1, y1)
    vertex(x2, y2)
    vertex(x3, y3)
    vertex(x4, y4)
    vertex(x1, y1)
    endShape()

    # triangle
    beginShape()
    fill(0.0, 255.0 / depth, 0.0)
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
    saveFrame(name + '.png')
