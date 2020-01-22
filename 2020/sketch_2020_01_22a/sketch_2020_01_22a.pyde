from __future__ import division
add_library('VideoExport')

def setup():
    size(600, 600)
    global videoExport
    videoExport = VideoExport(this)
    videoExport.startMovie()
    smooth(8)
    colorMode(HSB)
    frameRate(30)

def draw():
    background(240)
    translate(width / 2, height / 2)
    num_points = 360
    n_scale = .005
    a = TWO_PI / num_points
    x_off = y_off = z_off = width
    for radius in range(600, 10, -30):
        f = radians(frameCount + radius / 3)
        fill(radius / 2, 100)

        beginShape()
        for i in range(num_points):
            ny = 100 * sin(-f + a * i) + x_off
            nx = 100 * cos(f + a * i) + y_off
            nz = 100 * sin(f)
            r = radius / 2 - radius / 2 * noise(nx * n_scale,
                                        ny * n_scale,
                                        nz * n_scale)
            y = r * sin(a * i)
            x = r * cos(a * i)
            vertex(x, y)
        endShape(CLOSE)

    # videoExport.saveFrame()
    if frameCount == 360:
        videoExport.endMovie()
        exit()

def keyPressed():
    if key == 's':
        saveFrame("s####.png")
    if key == 'q':
        videoExport.endMovie()
        exit()
