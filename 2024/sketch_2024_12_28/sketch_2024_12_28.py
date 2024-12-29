# Delaunay play
from itertools import product

import py5
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
    shp = py5.create_shape()
    num_vertices = tris.shape[0] * 3
    vs = tris.reshape(num_vertices, 2)
    with shp.begin_closed_shape(py5.TRIANGLES):
          shp.vertices(vs)  
    shp.set_fills(noise_colors(vs))
    py5.shape(shp)
#     f = py5.frame_count
#     if f < 361 and f % 5 == 0:
#         py5.save_frame('###.png')


    
def noise_colors(vs):
    step = py5.TAU / len(vs)
    colors = []
    for i, (xo, yo) in enumerate(vs):
        a = i * step + py5.radians(py5.frame_count)
        x = py5.cos(a) + xo / 10
        y = py5.sin(a) + yo / 10  
        h = 255 * (1 + py5.os_noise(x, y, 100)) / 2
        s = 255 * (1 + py5.os_noise(x, y, 1000)) / 2
        b = 255 #* (1 + py5.os_noise(x, y, 10000)) / 2
        colors.append(py5.color(h, s, b))
    return colors
    
def key_pressed():
    global seed
    if py5.key == ' ':
        seed += 1
        new_points()
    elif str(py5.key).lower() == 's':
        py5.save_frame('out###.png')
    
            
py5.run_sketch(block=False)