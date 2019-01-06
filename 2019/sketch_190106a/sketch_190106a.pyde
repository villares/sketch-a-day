# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "sketch_190106a" 

from arcs import *

def setup():
    size(400, 400)
    noFill()

    
def draw():
    background(200)
    strokeWeight(map(mouseX, 0, width, 1, 10))
    stroke(255)
    ellipse(100, 100, 30, 30)
    ellipse(100, 300, 30, 30)
    ellipse(150, 100, 30, 30)
    ellipse(200, 100, 30, 30)
    ellipse(50, 100, 30, 30)

    stroke(0)
    bar(100, 100, 100, 300, shorter=30, thickness=30)
    bar(150, 100, 150, 300)
    bar(200, 100, 200, 300, 10, 10)
    bar(50, 100, 350, 300)

def bar(x1, y1, x2, y2, shorter=0, thickness=None):
    """
    O código para fazer as barras, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    """
    L = dist(x1, y1, x2, y2)
    if not thickness:
        thickness = max(L / 10, 10)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        strokeCap(ROUND)
        strokeCap(SQUARE)
        line(thickness/2, offset, thickness/2, L - offset)
        line(-thickness/2, offset, -thickness/2, L - offset)
        half_circle(0, offset, thickness/2, UP)
        half_circle(0,  L - offset, thickness/2, DOWN)
