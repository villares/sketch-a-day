# py5 imported mode sketch <py5coding.org>

import shapely

def setup():
    size(800, 800)
    background(200, 240, 200)
    for _ in range(300):
        x, y = random(width), random(height)
        ca = shapely.Point(x, y).buffer(50)
        cb = ca.buffer(-20)
        cc = ca - cb
        fill(255)
        shape(cc)
    save('out.png')