from __future__ import division

def setup():
    size(600, 600);
    background(240, 240, 240)
    noFill()
    
    s = 20 # must be int
    stroke(0, 100, 0)
    for x in range(s // 2, width, s):
        for y in range(s // 2, height, s):
            circle(x, y, s)
            # point(x, y)

    stroke(0, 0, 100)
    s = 22 # could be float
    cols, rows = int(width / s), int(height / s)
    for ix in range(cols):
        x = s / 2 + ix * s
        for iy in range(rows):
            y = s / 2 + iy * s
            circle(x, y, s)
            # point(x, y)
            
    # saveFrame('a.png')
