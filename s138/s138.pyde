# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
from __future__ import division

SKETCH_NAME = "s138"  # 1805168

"""
Revisitig sketch 71 180312 
"""



def setup():
    size(600, 600)
    noFill()

def draw():
    poly_shape(width / 2, height / 2, PI/3, 3, 2, PI/2)

def poly_shape(x, y, angle, D, sat, rotation):
    K = 5 # randomness added to vertex positions
    stroke(frameCount % 256) #black to white, jump to black
    with pushMatrix():
        translate(x, y)
        rotate(rotation)
        radius = D * 40
        # create a polygon on a ps PShape object
        ps = createShape()
        ps.beginShape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx + random(-K, K), sy + random(-K, K))
            a += angle
        ps.endShape(CLOSE)  # end of PShape creation
        shape(ps, 0, 0)  # Draw the PShape
        if D > 1:  # if the recursion 'distance'/'depth' allows...
            for i in range(ps.getVertexCount()):
                # for each vertex
                pv = ps.getVertex(i)  # gets vertex as a PVector
                # recusively call poly_shape with a smaller D
                poly_shape(pv.x, pv.y, angle, D - 1, sat, rotation)
    
