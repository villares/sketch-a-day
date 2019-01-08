# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "sketch_190106a" 

from arcs import *

def setup():
    size(400, 400)
    noFill()
    background(200)
    strokeWeight(3)
    
    stroke(255)
    ellipse(100, 100, 30, 30)
    ellipse(100, 300, 30, 30)
    ellipse(150, 100, 30, 30)
    ellipse(200, 100, 30, 30)
    ellipse(50, 100, 30, 30)

    stroke(0)
    bar(100, 100, 100, 300, thickness=40)
    bar(150, 100, 150, 300, ends=(0,1))
    bar(200, 100, 200, 300, 10, ends=(1,0))
    bar(50, 100, 350, 300)
    
    saveFrame(SKETCH_NAME + ".png")

def bar(x1, y1, x2, y2, thickness=None, shorter=0, ends=(1,1)):
    """
    O código para fazer as barras, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    """
    L = dist(x1, y1, x2, y2)
    if not thickness:
        thickness = max(L / 10, 10)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        line(thickness/2, offset, thickness/2, L - offset)
        line(-thickness/2, offset, -thickness/2, L - offset)
        if ends[0]:
            half_circle(0, offset, thickness/2, UP)
        if ends[1]:
            half_circle(0,  L - offset, thickness/2, DOWN)
