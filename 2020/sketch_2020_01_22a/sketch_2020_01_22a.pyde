from __future__ import division
# add_library('VideoExport')

def setup():
    size(600, 600)
    # global videoExport
    # videoExport = VideoExport(this)
    # videoExport.startMovie()
    # videoExport.setFrameRate(30)
    frameRate(30)
    noiseSeed(20200122)

def draw():
    background(240)
    translate(width / 2, height / 2)
    num_points = 360
    n_scale = .005
    a = TWO_PI / num_points
    x_off = y_off = z_off = width
    for radius in range(800, 10, -25):
        f = radians(frameCount + radius / 5)
        fill(255 - radius / 3, 100)
        beginShape()
        for i in range(num_points):
            ny = 100 * sin(f - a * i) + x_off
            nx = 100 * cos(f + a * i) + y_off
            nz = 100 * sin(f)
            r = radius / 2 * noise(nx * n_scale,
                                   ny * n_scale,
                                   nz * n_scale)
            y = r * sin(a * i)
            x = r * cos(a * i)
            vertex(x, y)
        endShape(CLOSE)

    # videoExport.saveFrame()
    if frameCount == 360:
        # videoExport.endMovie()
        exit()
