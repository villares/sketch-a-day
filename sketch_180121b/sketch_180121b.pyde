"""
s18020b - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Slider code by Peter Farell (slight style mod by me)
"""
from __future__ import division
from slider import Slider

r1 = Slider(0,500,100)
r2 = Slider(0,500,200)
np = Slider(3,50,10)


def setup():
    size(500, 500, P2D)
    colorMode(HSB)
    background(0)
    r1.position(20, 20)
    r2.position(20, 60)
    np.position(20, 100)


def draw():
    background(0)
    colorMode(HSB)
    npoints, rad1, rad2 = np.val, r1.val, r2.val  # I wanted to draw the star before the sliders
    with pushMatrix():
        translate(width / 2, height / 2)
        angle = TWO_PI / npoints
        h_angle = angle / 2.
        beginShape()
        #vertex(0, 0)
        a = 0
        while a < TWO_PI:
            sx = cos(a) * rad2
            sy = sin(a) * rad2
            cor = map(a, 0, TWO_PI, 0, 255)
            fill(cor, 255, 255)
            vertex(sx, sy)
            sx = cos(a + h_angle) * rad1
            sy = sin(a + h_angle) * rad1
            fill(cor, 255, 255)
            vertex(sx, sy)
            a += angle
        endShape(CLOSE)
    npoints, rad1, rad2 = np.value(), r1.value(), r2.value()  # this is the usual way to get values & draw the sliders
    if not frameCount % 10 and frameCount < 500:
        saveFrame("###.tga")
