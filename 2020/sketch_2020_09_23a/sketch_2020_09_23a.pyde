from random import sample
from itertools import product
from villares.line_geometry import * # github.com/villares/villares
from arc_filleted_poly import arc_filleted_poly 
from ponto import Ponto

BORDER = 50
SIZE = 150
r_list = [10, 20, 30, 40, -10, -20, -30, -40]
p_list = []
dragg = []

def setup():
    global grid
    size(400, 400)
    grid = list(product(range(BORDER, height - BORDER + 1, SIZE),
                        range(BORDER, height - BORDER + 1, SIZE)))
    make_points(len(r_list))

def draw():
    background(200)

    noFill()
    strokeWeight(1)
    stroke(255)
    poly(p_list)

    stroke(0)
    fill(100, 100)
    arc_filleted_poly(p_list, map(abs, r_list))
                        
    for p in p_list:
        if len(dragg) == 2:
            if area(p, dragg[0], dragg[1]) > 0:
                p.f = color(255, 0, 0)
            else:
                p.f = color(0, 0, 255)
        else:
            p.f = 255
        p.draw()

    if len(dragg) == 2:   
        d_line = Line(*dragg)
        strokeWeight(0.5)
        d_line.draw() 
        lines = inter_lines(d_line, p_list)
        for inter_line in lines:
            strokeWeight(2)
            inter_line.draw()

        
def keyPressed(): 
    if key == ' ':
        make_points(len(r_list))
        # saveFrame("###.png")  
                        
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

def make_points(num):
    p_list[:] = []
    for x, y in sample(grid, num):
        p_list.append(Ponto(x, y))
        
