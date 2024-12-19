# Dodecahedron

import py5
from py5_tools import animated_gif
import numpy as np

def setup():
    py5.size(600, 600, py5.P3D)
    animated_gif('out.gif', duration=0.1,
                 frame_numbers=range(1, 361, 15))

def draw():
    py5.background(0, 0, 100)
    py5.translate(py5.width / 2, py5.height / 2, -py5.height)
    py5.rotate_y(py5.radians(py5.frame_count))
    dodecahedron(300)

def dodecahedron(radius):
    a = radius / 1.618033989
    b = radius
    c = 0.618033989 * a
    verts = np.array([
        (a, a, a), (a, a, -a), (a, -a, a), (a, -a, -a), (-a, a, a),
        (-a, a, -a), (-a, -a, a), (-a, -a, -a), (0, c, b), (0, c, -b),
        (0, -c, b), (0, -c, -b), (c, b, 0), (c, -b, 0), (-c, b, 0),
        (-c, -b, 0), (b, 0, c), (b, 0, -c), (-b, 0, c), (-b, 0, -c),
        ])
    faces = np.array([
        (0, 16, 2, 10, 8), (0, 8, 4, 14, 12), (16, 17, 1, 12, 0),
        (1, 9, 11, 3, 17), (1, 12, 14, 5, 9), (2, 13, 15, 6, 10),
        (13, 3, 17, 16, 2), (3, 11, 7, 15, 13), (4, 8, 10, 6, 18),
        (14, 5, 19, 18, 4), (5, 19, 7, 11, 9), (15, 7, 19, 18, 6)
        ])
    for face in faces:
        with py5.begin_closed_shape():
            py5.vertices(verts[face])
            
py5.run_sketch(block=False)
