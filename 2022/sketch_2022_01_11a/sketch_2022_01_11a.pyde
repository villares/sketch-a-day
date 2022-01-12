
from random import choice

modulor = [1, 2, 3, 5, 8, 13, 21]
strip_height = 8
strips = 10

def setup():
    size(1400, 800)
    colorMode(HSB)
    noLoop()
    
def draw():
    rects = []
    s = height / strips / strip_height
    for y in range(0, 800, strip_height * s):
        x = 0
        while x < width:
            h = strip_height * s
            w = choice(modulor) * s
            if x + w > width:
                continue
            rects.append((x, y, w, h))
            x += w
    
    for x, y, w, h in rects:
        fill((w / s * h / s) % 256, 200, 200)
        rect(x, y, w, h)

def keyPressed():
    redraw()
    
