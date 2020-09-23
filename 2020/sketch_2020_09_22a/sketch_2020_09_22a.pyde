from random import sample
from itertools import product

from villares.line_geometry import * # github.com/villares/villares

from ponto import Ponto

BORDER = 100
SIZE = 50

pontos = []
dragg = []

def setup():
    global grid
    size(400, 400)
    grid = list(product(range(BORDER, height - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))

    make_points()



def draw():
    background(200)
    
    if len(dragg) == 2:   
        d_line = Line(*dragg)
        strokeWeight(0.5)
        d_line.draw() 
        lines = inter_lines(d_line, pontos)
        for inter_line in lines:
            strokeWeight(2)
            inter_line.draw()


    noFill()
    strokeWeight(1)
    beginShape()
    for p in pontos:
        vertex(p.x, p.y)
    endShape(CLOSE)

                        
    for p in pontos:
        if len(dragg) == 2:
            if area(p, dragg[0], dragg[1]) > 0:
                p.f = color(255, 0, 0)
            else:
                p.f = color(0, 0, 255)
        else:
            p.f = 255
        p.draw()
  
        
def keyPressed(): 
    if key == ' ': make_points()  
    if key == 'm': move_points()  
                        
def mousePressed():
    dragg[:] = [(mouseX, mouseY)]
    
def mouseDragged():
    if len(dragg) == 1:
        dragg.append((mouseX, mouseY))
    else:
        dragg[1] = (mouseX, mouseY)

def area(p0, p1, p2):
    a = (p1[0] * (p2[1] - p0[1]) +
         p2[0] * (p0[1] - p1[1]) +
         p0[0] * (p1[1] - p2[1]))
    return a

# def mouseReleased():
#     dragg[:] = []

def make_points():
    pontos[:] = []
    for x, y in sample(grid, 6):
        pontos.append(Ponto(x, y))
        
