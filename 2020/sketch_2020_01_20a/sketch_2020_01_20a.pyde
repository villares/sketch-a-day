from __future__ import division

def setup():
    size(600, 600)
    pixelDensity(2)
    # strokeWeight(2)
    smooth(8)
    fill(255, 100)

def draw():
    background(240, 250, 250)
    translate(width / 2, height / 2)
    num_points = 360
    n_scale = .002
    a = TWO_PI / num_points
    x_off, y_off = mouseY, mouseX
    for radius in range(500, 10, -50):
        f = frameCount + radius
        beginShape()
        for i in range(num_points):
            ny = 300 * sin(a * i) + x_off
            nx = 300 * cos(a * i) + y_off
            r = radius * noise(nx * n_scale,
                               ny * n_scale,
                               f * n_scale)
            y = r * sin(a * i)
            x = r * cos(a * i)
            vertex(x, y)
        endShape(CLOSE)
