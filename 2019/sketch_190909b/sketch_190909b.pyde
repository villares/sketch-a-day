from __future__ import division

def setup():
    size(600, 600)
    rectMode(CENTER)
    noStroke()
    noLoop()
    
def draw():
    background(0)
    rec_grid(width / 2, height / 2, 2, 580)
    
def rec_grid(x, y, n, tw):
    pushMatrix()
    translate(x, y)
    cw = tw / n
    margin = (cw - tw) / 2
    for i in range(n):
        nx = cw * i + margin
        for j in range(n):
            ny = cw * j + margin
            if cw > 6 and random(10) < 8.5:
                rec_grid(nx, ny, 2, cw)
            else:
                colorMode(HSB)
                c = map(cw, 5, width / 4, 0, 250)
                fill(c, 255, 255)
                square(nx, ny, cw - 2)
    popMatrix()
    
def keyPressed():
    saveFrame("####.png")
    redraw()
    
    
    
