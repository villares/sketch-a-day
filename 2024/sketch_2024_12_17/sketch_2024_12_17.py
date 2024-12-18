# Voronoi +   Delaunay play
from itertools import product

import py5
from scipy.spatial import Delaunay, Voronoi
import numpy as np

num_points = 200

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    new_points()
    
def new_points():
    global seed_points
    W = 60
    R = 20
    seed_points = []
    for i in range(1):
        seed_points.extend(
            (x + (i - 1) * py5.random(-R, R),
             y + i * py5.random(-R, R))
             for x, y in product(
                 range(0, py5.width + W, W),
                 range(0, py5.height+ W, W)))
    seed_points.extend(
        ((-py5.width, -py5.height),
         (py5.width * 2, -py5.height),
         (py5.width * 2, py5.height * 2),
         (-py5.width, py5.height * 2))
        )
    
def draw():
    py5.background(0)
    py5.translate(100, 100)
    py5.scale(400 / 600)
    py5.stroke_weight(3)
    py5.stroke(0, 255, 200)
    py5.no_fill()
    pts = np.array(seed_points)
    
    tri = Delaunay(pts)
    tri_pts = []
    for t in pts[tri.simplices]:
        tri_pts.extend(t)
    with py5.begin_closed_shape(py5.TRIANGLES):
        py5.vertices(tri_pts)
    py5.stroke(128, 255, 255)
    
    voronoi = Voronoi(pts)
    for vs in voronoi.regions:
        if vs and -1 not in vs:
           with py5.begin_closed_shape():
                py5.vertices(voronoi.vertices[index] for index in vs)
        
def key_pressed():
    if py5.key == ' ':
        new_points()
    elif str(py5.key).lower() == 's':
        py5.save_frame('out###.png')
     
            
py5.run_sketch(block=False)
