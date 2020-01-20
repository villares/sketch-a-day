from __future__ import division

def setup():
    size(500, 500)
    pixelDensity(2)
    strokeWeight(2)
    smooth(8)
    
def draw():
    background(240, 250, 250)
    translate(width / 2, height / 2)
    n = 600
    a = TWO_PI / n
    r = 200
    for i in range(n):
        y = r * sin(a * i)
        x = r * cos(a * i)
        point(x, y)
