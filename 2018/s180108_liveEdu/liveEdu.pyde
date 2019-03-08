
from PlatonicSolids import *

def setup():
    global s1, s2
    size(500, 500, P3D)
    s1 = Icosahedron(100)
    s2 = Dodecahedron(80)
    noFill()
    stroke(255)
    strokeWeight(5)
    
def draw():
    background(0)
    with pushMatrix():
        translate(250, 250)
        rotateX(radians(mouseY))
        s1.create()
    
    with pushMatrix():
        translate(100, 100)
        rotateX(radians(mouseX))
        s2.create()