from __future__ import division
add_library('VideoExport')

def setup():
    size(600, 600)
    global videoExport
    videoExport = VideoExport(this)
    videoExport.startMovie()    
    smooth(8)
    colorMode(HSB)
    
def draw():
    background(240)
    translate(width / 2, height / 2)
    num_points = 360
    n_scale = .005
    a = TWO_PI / num_points
    x_off = y_off = width
    for radius in range(500, 10, -30):
        f = frameCount + radius / 2
        fill(radius / 2, 200, 200, 100)

        beginShape()
        for i in range(num_points):
            ny = 100 * sin(a * i) + x_off
            nx = 100 * cos(a * i) + y_off
            r = radius - radius * noise(nx * n_scale,
                               ny * n_scale,
                               f * n_scale)
            y = r * sin(a * i)
            x = r * cos(a * i)
            vertex(x, y)
        endShape(CLOSE)
        
    videoExport.saveFrame()
    
def keyPressed():        
    if key == 's':
        saveFrame("s####.png")
    if key == 'q':
        videoExport.endMovie()
        exit()
