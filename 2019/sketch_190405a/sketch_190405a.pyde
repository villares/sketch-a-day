"""
Terrain Box
"""

add_library('peasycam')
from third_point import third_point

L, H = 100, 100
A, B, C, D = H + 50, H + 0, H + 10, H + 20

def setup():
    global cam
    size(700, 500, P3D)
    cam = PeasyCam(this, 660)
    fill(255, 100)

def draw():
    background(200)
    # ortho()
    strokeWeight(2)
    stroke(0)
    translate(0, 0, -100)
    faces_3D()
    cam.beginHUD()
    translate(100, 50)
    top_2D()
    translate(0, 400)
    faces_2D()
    cam.endHUD()


def faces_3D():
    # floor
    beginShape()
    vertex(0, 0, 0)
    vertex(L, 0, 0)
    vertex(L, L, 0)
    vertex(0, L, 0)
    endShape(CLOSE)

    beginShape()
    vertex(0, 0, B)
    vertex(L, 0, C)
    vertex(L, 0, 0)
    vertex(0, 0, 0)
    endShape(CLOSE)

    beginShape()
    vertex(0, 0, B)
    vertex(0, L, A)
    vertex(0, L, 0)
    vertex(0, 0, 0)
    endShape(CLOSE)
    
    stroke(200, 200, 0)
    line(0, 0, B, L, L, D)
    stroke(0)
    line(L, 0, C, L, L, D)
    line(0, L, A, L, L, D)
    stroke(0, 0, 200)
    line(L, L, 0, L, L, D)

def faces_2D():
    beginShape()
    vertex(0, -B)
    vertex(L, -C)
    vertex(L, 0)
    vertex(0, 0)
    endShape(CLOSE)
    b = PVector(0, -B)
    c = PVector(L, -C)
    bc = PVector.dist(b, c) #(0, 0, -B, L, 0, -C)
    
    bd = dist(0, 0, B, L, L, D)
    cd = dist(L, 0, C, L, L, D)
    d = third_point(b, c, bd, cd)
    stroke(200, 200, 0)
    line(b.x, b.y, d.x, d.y)
    stroke(0)
    line(c.x, c.y, d.x, d.y)
                         
    ab = dist(0, A, L, B)
    ad = dist(0, A, L, D)
    a = third_point(b, d, ab, ad)
    stroke(0)
    line(b.x, b.y, a.x, a.y)
    line(d.x, d.y, a.x, a.y)

def top_2D():
    stroke(0)
    rect(0, 0, L, L)
    stroke(200, 200, 0)
    line(0, 0, B, L, L, D)
    stroke(0)
    line(L, 0, C, L, L, D)
    line(0, L, A, L, L, D)
    stroke(0)
    line(L, L, 0, L, L, D)
