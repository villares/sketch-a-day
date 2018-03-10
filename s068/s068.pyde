"""
sketch 67 180308 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
from __future__ import division
from slider import Slider

i = Slider(PI / 6, TWO_PI / 3, QUARTER_PI)
j = Slider(1, 4, 2)
k = Slider(10, 50, 25)

I, J, K = 1, 1, 1 # dummy initial slider values


def setup():
    size(600, 600)
    colorMode(HSB)
    noFill()
    i.position(20, 20)
    j.position(20, 60)
    k.position(20, 100)

def draw():
    global I, J, K
    background(0)
    poly_shape(width / 2, height/2, I, J, K)
    # Read and update sliders
    I = i.value()  # from PI/6 to TWO_PI/3
    j.high = 3 + I * 1.5 # change J's upper limit
    J = j.value()  # 1 to 3 + I * 1.5 
    K = k.value()  # 10 to 50
    #if not frameCount % 100: saveFrame("s####.tga")

def poly_shape(x, y, angle, D, offset):
    stroke((frameCount / 2 * D) % 256, 255, 255, 255)
    strokeWeight(D)
    with pushMatrix():
        translate(x, y)
        # rotate(radians(30))
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
