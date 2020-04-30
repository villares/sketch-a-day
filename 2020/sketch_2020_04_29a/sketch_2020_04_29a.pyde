"""
https://discourse.processing.org/t/porting-a-3d-brownian-motion-to-python-mode/20144
"""

from collections import deque

add_library('GifAnimation')
from gif_animation_helper import gif_export

sketch_name = 'sketch_2020_04_28a'
points = deque(maxlen=200)
paused = False
DIM = 60

def setup():
    size(500, 500, P3D)
    colorMode(HSB)
    points.append((PVector(DIM, 0, 0), PVector(0, 0, DIM)))
    
def draw():
    background(0)
    translate(width / 2, height / 2)
    rotateY(frameCount / 100.)
    
    for i, (pa, pb) in enumerate(points):
        fill((frameCount + i) % 256, 255, 255)
        bar(pa.x, pa.y, pa.z, pb.x, pb.y, pb.z, 3)
        if i > 0:
            ppa, ppb = points[i - 1]
            bar(pa.x, pa.y, pa.z, ppa.x, ppa.y, ppa.z, 5)
            bar(pb.x, pb.y, pb.z, ppb.x, ppb.y, ppb.z, 5)
           
    if not paused:
        va, vb = points[-1]
        na = PVector()
        nb = PVector(DIM * 5, DIM * 5, DIM * 5)
        while PVector.dist(na, nb) > DIM * 2: 
            na = va + PVector.random3D() * DIM
            nb = vb + PVector.random3D() * DIM

        points.append((na, nb))
        for pair in points:
            pair[0].sub(na / 30)
            pair[1].sub(nb / 30)

        gif_export(GifMaker, sketch_name)
    
    
def mousePressed():
    global paused
    if mouseButton == RIGHT:
        points.clear()
        points.append((PVector(DIM, 0, 0), PVector(0, 0, DIM)))
    elif not paused:
        paused = True
        noLoop()
    else:
        paused = False
        loop() 

    if key == 'q':
        gif_export(GifMaker, "animation", finish=True)
        
        
def bar(x1, y1, z1, x2, y2, z2, weight=10):
    """Draw a box rotated in 3D like a bar/edge."""
    p1, p2 = PVector(x1, y1, z1), PVector(x2, y2, z2)
    v1 = p2 - p1
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi, the  = acos(v1.z / rho), atan2(v1.y, v1.x)
    v1.mult(0.5)
    pushMatrix()
    translate(x1 + v1.x, y1 + v1.y, z1 + v1.z)
    rotateZ(the)
    rotateY(phi)
    box(weight, weight, p1.dist(p2))
    popMatrix()
