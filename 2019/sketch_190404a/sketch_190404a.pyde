"""
Terrain Box
"""

add_library('peasycam')

L, H = 100, 100
A, B, C, D = H + 50, H + 0, H + 10, H + 20

def setup():
    size(700, 500, P3D)
    cam = PeasyCam(this, 660)
    fill(255, 100)

def draw():
    background(200)
    # ortho()
    strokeWeight(2)
    stroke(0)

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
    stroke(0, 200, 200)
    line(L, 0, C, L, L, D)
    line(0, L, A, L, L, D)
    stroke(0, 0, 200)
    line(L, L, 0, L, L, D)
