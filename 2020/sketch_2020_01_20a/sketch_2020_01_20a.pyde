from __future__ import division

def setup():
    size(500, 500)
    pixelDensity(2)
    strokeWeight(2)
    smooth(8)
    
def draw():
    background(240, 250, 250)
    translate(width / 2, height / 2)
    num_points, radius = 360, 200
    n_scale = .01
    a = TWO_PI / n
    x_off, y_off = 100, 50
    for i in range(num_points):
        r = radius * noise(x * n_scale, y * n_scale)
        y = r * sin(a * i) + x_off
        x = r * cos(a * i) + y_off
        point(x, y)
