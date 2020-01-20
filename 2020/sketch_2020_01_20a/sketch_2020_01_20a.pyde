from __future__ import division

def setup():
    size(500, 500)
    pixelDensity(2)
    strokeWeight(2)
    smooth(8)
    
def draw():
    background(240, 250, 250)
    translate(width / 2, height / 2)
    num_points, radius = 360, 0 + mouseX
    n_scale = .01
    a = TWO_PI / num_points
    x_off, y_off = 100, 50
    beginShape()
    for i in range(num_points):
        ny = radius * sin(a * i) + x_off
        nx = radius * cos(a * i) + y_off
        r = radius * noise(nx * n_scale, ny * n_scale)
        y = r * sin(a * i)
        x = r * cos(a * i)
        vertex(x, y)
    endShape(CLOSE)
