"""Grid study"""
shapes = []

def setup():
    size(500, 500)
    rectMode(CENTER)
    shapes.extend(grid(10, 12, 25, thing))
    
def draw():
    translate(width / 2, height / 2)
    rect(0, 0, 250, 300)
    for s in shapes:
        shape(s)
        
def grid(cols, rows, space, func):
    result = []
    half_w = -cols * space / 2.
    half_h = -rows * space / 2.
    for ix in range(cols):
        x = half_w + ix * space + space / 2
        for iy in range(rows):
            y = half_h + iy * space + space / 2
            result.append(func(x, y))
    return result
        
def thing(x=0, y=0, w=10, h=10):
    t = createShape(ELLIPSE, x, y, w, h)
    return t
