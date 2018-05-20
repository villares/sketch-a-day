# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s138"  # 180518 Revisitig ideas from sketch s071 180312

add_library('gifAnimation')
from gif_exporter import *


def setup():
    size(600, 600)
    noFill()

def draw():
    poly_shape(width / 2, height / 2, PI / 3, 4)
    if frameCount % 2 and frameCount > 255:
        gif_export(GifMaker, frames=256, filename=SKETCH_NAME)

def poly_shape(x, y, angle, D):
    rv = 3  # randomness added to vertex positions
    stroke(255 - frameCount % 256)  # white to black, jump to white
    with pushMatrix():
        translate(x, y)
        radius = D * 27
        # create a polygon on a ps PShape object
        ps = createShape()
        ps.beginShape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx + random(-rv, rv), sy + random(-rv, rv))
            a += angle
        ps.endShape(CLOSE)  # end of PShape creation
        shape(ps, 0, 0)  # Draw the PShape
        if D > 1:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.getVertexCount()):
                # for each vertex
                pv = ps.getVertex(i)  # gets vertex as a PVector
                # recusively call poly_shape with a smaller D
                poly_shape(pv.x, pv.y, angle, D - 1)
                
def keyPressed():
    loop()
