"""
sketch 67 180308 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
from __future__ import division
from slider import Slider

i = Slider(PI / 6, TWO_PI / 3, QUARTER_PI)
j = Slider(1, 4, 2)
k = Slider(1, 50, 25)

I, J, K = 3, 3, 3


def setup():
    size(600, 600)
    colorMode(HSB)
    strokeWeight(5)
    noFill()
    i.position(20, 20)
    j.position(20, 60)
    k.position(20, 100)

def draw():
    global I, J, K
    background(0)
    poly_shape(width / 2, height / 2, I, J, K)

    I = i.value()  # PI/6, TWO_PI/3
    J = j.value()  # 0 , 4
    K = k.value()  # 1, 50
    # if not frameCount % 10: saveFrame("s####.tga")

def poly_shape(x, y, angle, D, offset):
    stroke((frameCount / 2 * D) % 256, 255, 255, 100)
    with pushMatrix():
        translate(x, y)
        radius = D * offset
        ps = createShape()
        ps.beginShape()
        a = 0
        while a < TWO_PI:
            sx = cos(a) * radius
            sy = sin(a) * radius
            ps.vertex(sx, sy)
            a += angle
        ps.endShape(CLOSE)
        shape(ps, 0, 0)
        if D > 1:
            for i in range(ps.getVertexCount()):
                pv = ps.getVertex(i)  # PVector
                poly_shape(pv.x, pv.y, angle, D - 1, offset)
