"""
https://discourse.processing.org/t/porting-a-3d-brownian-motion-to-python-mode/20144
"""

from collections import deque

add_library('GifAnimation')
from gif_animation_helper import gif_export

sketch_name = 'sketch_2020_04_28a'
points = deque(maxlen=200)
paused = False
DIM = 30

def setup():
    size(300, 300, P3D)
    colorMode(HSB)
    noFill()
    strokeWeight(2)
    points.append((PVector(DIM, 0, 0), PVector(0, 0, DIM)))
    
def draw():
    background(0)
    translate(width / 2, height / 2)
    rotateY(frameCount / 100.)
    
    for i, (pa, pb) in enumerate(points):
        stroke((frameCount + i) % 256, 255, 255)
        line(pa.x, pa.y, pa.z, pb.x, pb.y, pb.z)
    
    beginShape()
    for i, (pa, pb) in enumerate(points):
        stroke(255, 100) #((frameCount + i) % 256, 255, 255)
        curveVertex(pa.x, pa.y, pa.z) #, pb.x, pb.y, pb.z)
    endShape()

    beginShape()
    for i, (pa, pb) in enumerate(points):
        stroke(255, 100) #((frameCount + i) % 256, 255, 255)
        curveVertex(pb.x, pb.y, pb.z) #, pb.x, pb.y, pb.z)
    endShape()
   
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
