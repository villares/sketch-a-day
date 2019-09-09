from __future__ import division

def setup():
    size(600, 600)
    rectMode(CENTER)
    fill(0)
    noStroke()
    rec_grid(width / 2, height / 2, 4, 580)
    
def rec_grid(x, y, n, tw):
    pushMatrix()
    translate(x, y)
    cw = tw / n
    margin = (cw - tw) / 2
    for i in range(n):
        nx = cw * i + margin
        for j in range(n):
            ny = cw * j + margin
            if cw > 5 and random(10) < 9:
                rec_grid(nx, ny, 2, cw)
            else:
                square(nx, ny, cw - 2)
    popMatrix()
    
    
    
    
    
    
    
