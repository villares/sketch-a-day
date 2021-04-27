from __future__ import division

add_library('gifAnimation')
from villares.gif_export import gif_export

def setup():
    size(600, 600)
    noStroke()
    
def draw():
    background(0)
    grid_elem = 10
    spacing = width / (grid_elem - 4)
    r = spacing * (sqrt(3) / 2)
    hl = r * sqrt(3) / 2  # half-L meio lado
    for ix in range(-1, grid_elem + 1):
        for iy in range(-1, grid_elem + 1):
            if iy % 2:
                x = hl + ix * hl
            else:
                x = ix * hl
            if ix % 2:
                y = iy * 3 * r / 2
                rot = PI * cos(radians(frameCount))
            else:
                y = iy * 3 * r / 2 - r / 2
                rot = PI * sin(radians(frameCount))
            fill(255 , 64 + (rot / PI) * 64)    
            hexagon(x, y, r, rot)
    
    if frameCount % 2:
        gif_export(GifMaker, "filename")
    if frameCount > 360:
        gif_export(GifMaker, finish=True)
            
def tri(x, y, r, rot=0):
    ang = -HALF_PI + rot
    with pushMatrix():
        translate(x, y)
        beginShape()
        for i in range(3):
            sx = cos(i * TWO_PI / 3 + ang) * r 
            sy = sin(i * TWO_PI / 3 + ang) * r
            vertex(sx, sy)
        endShape(CLOSE)
            
def hexagon(x, y, r, rot=0):
    with pushMatrix():
        translate(x, y)
        beginShape()
        for i in range(6):
            sx = cos(i * TWO_PI / 6 + HALF_PI * rot) * r 
            sy = sin(i * TWO_PI / 6 + HALF_PI * rot) * r
            vertex(sx, sy)
        endShape(CLOSE)
        
