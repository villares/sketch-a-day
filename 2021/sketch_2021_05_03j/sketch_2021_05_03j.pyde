# Linear IntERPolation - LERP
from __future__ import division

def setup():
    global cor_a, cor_b
    size(600, 600)
    cor_a = color(0, 0, 200)
    cor_b = color(0, 200, 0)
    
def draw():
    background(200)
    for i in range(0, 600, 10):
        t = i / width
        nova_cor = lerpColor(cor_a, cor_b, t)
        stroke(nova_cor)
        noFill()
        strokeWeight(2)
        ax, ay = 100, 100
        bx, by = mouseX, mouseY
        # cx = lerp(ax, bx, t)
        # cy = lerp(ay, by, t)
        noFill()
        cp1x, cp1y =  300, 100
        cp2x, cp2y =  300, 500
        if mousePressed:
            bezier(ax, ay, cp1x, cp1y, cp2x, cp2y, bx, by)
            circle(cp1x, cp1y, 10)
            circle(cp2x, cp2y, 10)
        cx = bezierPoint(ax, cp1x, cp2x, bx, t)
        cy = bezierPoint(ay, cp1y, cp2y, by, t)
        circle(cx, cy, 200)
