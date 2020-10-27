from __future__ import division
from villares.arcs import quarter_circle

N = 10
rotations = [0] * N * N
variations = [0] * N * N


def setup():
    global w
    size(500, 500)
    w = width / N
    rectMode(CENTER)
    strokeWeight(3)
    stroke(255)
    noFill()
    
def draw():
    background(0, 0, 100)
    for i in range(N):
        x = w / 2 + i * w
        for j in range(N):
            y = w / 2 + j * w
            push()
            translate(x, y)
            r = rotations[i + j * N]
            rotate(HALF_PI * r)
            if variations[i + j * N] == 0:
                module0(w)
            else:
                module1(w)
            pop()

def module0(w):
    translate(-w / 2, -w / 2)
    r = w / 2.
    ri = w / 2.
    q = w / 4.
    d = w / 6.
    line(r, 0, r, ri)
    line(ri, r, w, r)
    line(0, r, d, r)
    circle(d + d / 2, w / 2, d)
    line(r, r - q, 2 * q - d, r - q)
    circle(d + d / 2, w / 2 - q, d)
    line(r, w, r, w - d)
    circle(w / 2, w - (d + d / 2.0), d)

def module1(w): 
    translate(-w / 2.0, -w / 2.0)
    r = w / 2.
    quarter_circle(0, 0, r, BOTTOM + RIGHT)
    quarter_circle(w, w, r, TOP + LEFT)
 
def keyPressed():
    if key == 'r':
        for i in range(N * N):
            rotations[i] = int(random(4))
    if key == 'R':
        for i in range(N * N):
            rotations[i] = 0
    if key == 'v':
        for i in range(N * N):
            variations[i] =  int(random(2))
    if key == 'V':
        for i in range(N * N):
            variations[i] = 0
