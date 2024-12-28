# Delaunay play
from itertools import product

import py5
from shapely import Polygon
from scipy.spatial import Delaunay
import numpy as np

num_points = 200
seed = 0

def setup():
    py5.size(600, 600, py5.P2D)
    py5.color_mode(py5.HSB)
    new_points()
    
def new_points():
    global seed_points, tris
    W = 60
    R = 20
    py5.random_seed(seed)
    seed_points = []
    for i in range(2):
        seed_points.extend((x + (i - 1) * py5.random(-R, R),
                            y + i * py5.random(-R, R)) for x, y
                            in product(range(0, py5.width + W, W),
                                      range(0, py5.height+ W, W)))
    pts = np.array(seed_points)
    tri = Delaunay(seed_points)
    tris = pts[tri.simplices]
    
def draw():
    py5.random_seed(seed)
    py5.background(0)
    py5.translate(50, 50)
    py5.scale(500 / 600)
#     for vs in tris:
#         with py5.begin_closed_shape():
#               py5.vertices(vs)
    shp = py5.create_shape()
    with shp.begin_closed_shape(py5.TRIANGLES):
          shp.vertices(tris.reshape(tris.shape[0] * 3, 2))  
    shp.set_fills(py5.color(py5.random(255), py5.random(255), 255) for _ in range(tris.shape[0] * 3))
    py5.shape(shp)

    
def key_pressed():
    global seed
    if py5.key == ' ':
        seed += 1
        new_points()
    elif str(py5.key).lower() == 's':
        py5.save_frame('out###.png')
    
            
py5.run_sketch(block=False)