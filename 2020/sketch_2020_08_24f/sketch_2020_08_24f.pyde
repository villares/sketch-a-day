from villares.arcs import *


def setup():
    size(200, 200)
    translate(100, 100)
    tile(200)

def tile(s):
    push()
    translate(-s / 2, -s / 2)
    fill(0)
    beginShape()
    vertex(0, 0)
    bezierVertex(s / 6, s / 6, s / 2, s * 0.66, s / 2, s)
    b_arc(s, s, s, s, PI, PI + HALF_PI, 2)
    bezierVertex(s * 0.66, s / 2, s / 6, s / 6, 0, 0)
    endShape()
    pop()
