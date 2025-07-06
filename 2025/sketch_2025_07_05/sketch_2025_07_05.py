# Alexandre B A Villares -https://abav.lugaralgum.com/sketch-a-day

from itertools import product

import py5
from py5_tools import animated_gif
import numpy as np

A, B, C = 4, 4, 2

def setup():
    global vs, faces
    py5.size(500, 500, py5.P3D)
    position_map = {
        (i, j, k): n for n, (i, j, k)
        in enumerate(product(range(A), range(B), range(C)
        ))
    }
    W = 90
    m = (py5.width - W * A) / 2
    vs = np.array([
        (m + i * W + W / 2, m + j * W + W / 2, k * W - W / 2 + py5.random(-20, 20))
        for i, j, k in product(range(A), range(B), range(C))
    ])
    faces =[]
    for i, j in product(range(A), range(B)):
        for k in range(C):
            if (i + 1, j + 1, k) in position_map:
                faces.append([
                    position_map[i, j, k],
                    position_map[i + 1, j, k],
                    position_map[i + 1, j + 1, k],
                    position_map[i, j + 1, k]
                    ])
    faces = np.array(faces)
    animated_gif('out.gif', duration=5/60, frame_numbers=range(1, 361, 5))
    
def draw():
    py5.background(0, 100, 0)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.radians(py5.frame_count))
    py5.translate(-py5.width / 2, -py5.height / 2)
    py5.stroke_weight(1)
    py5.stroke(0)
    py5.fill(240)
    for face in faces:
        with py5.begin_closed_shape():
            py5.vertices(vs[face])
    py5.stroke_weight(5)
    py5.stroke(0, 0, 200)
    py5.points(vs)

py5.run_sketch(block=False)
