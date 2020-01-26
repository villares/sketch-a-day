from __future__ import division
add_library('VideoExport')

def setup():
    size(720, 720, P2D)
    global videoExport
    videoExport = VideoExport(this)
    videoExport.startMovie()
    videoExport.setFrameRate(15)
    # frameRate(30)
    colorMode(HSB)
    noFill()
    # strokeWeight(5)
    noiseSeed(20200122)

def draw():
    background(240)
    translate(width / 2, height / 2)
    num_points = 360
    n_scale = .005
    a = TWO_PI / num_points
    x_off = y_off = z_off = width
    for radius in range(360, 6, -6):
        f = radians(frameCount - radius / 2)
        beginShape()
        for i in range(num_points):
            ny = 100 * sin(f - a * i) + x_off
            nx = 100 * cos(f + a * i) + y_off
            nz = 100 * sin(f)
            r = 2*radius * noise(nx * n_scale,
                                   ny * n_scale,
                                   nz * n_scale)
            y = r * sin(a * i)
            x = r * cos(a * i)
            stroke(map(r, 6, radius*1.5, 0, 255),
                 200, 200)
            vertex(x, y)
        endShape(CLOSE)

    videoExport.saveFrame()
    if frameCount == 360:
        videoExport.endMovie()
        exit()
