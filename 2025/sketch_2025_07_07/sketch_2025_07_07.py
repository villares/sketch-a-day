# Alexandre B A Villares -https://abav.lugaralgum.com/sketch-a-day

from itertools import product

import py5
from py5_tools import animated_gif
import trimesh
import numpy as np

A, B, C = 30, 30, 2
W = 10

def setup():
    global mesh
    py5.size(500, 500, py5.P3D)
    position_map = {
        (i, j, k): n for n, (i, j, k)
        in enumerate(product(range(A), range(B), range(C)
        ))
    }
    m = (py5.width - W * A) / 2
    vs = np.array([(m + i * W + W / 2,
         m + j * W + W / 2,
         k * W  + py5.cos(py5.dist(i, j, A // 2, B // 2)) * W)
        for i, j, k in product(range(A), range(B), range(C))
    ])
    faces =[]
    for i, j in product(range(0, A, 2), range(0, B, 2)):
        for k in range(C):
            if (i + 2, j + 2, k) in position_map:
                va = position_map[i, j, k]
                vb = position_map[i + 2, j, k]
                vc = position_map[i + 2, j + 2, k]
                vd = position_map[i, j + 2, k]
                ve = position_map[i + 1, j + 1, k]
                faces.append([va, vb, ve])
                faces.append([vb, vc, ve])
                faces.append([vc, vd, ve])
                faces.append([vd, va, ve])
        
            if (i == 0 or i == A - 2) and (i, j + 2, k + 1) in position_map:
                va = position_map[i, j, k]
                vb = position_map[i, j + 2, k]
                vc = position_map[i, j + 2, k + 1]
                vd = position_map[i, j, k + 1]
                faces.append([va, vb, vc])
                faces.append([va, vc, vd])
            if (j == 0 or j == B - 2) and (i + 2, j, k + 1) in position_map:
                va = position_map[i, j, k]
                vb = position_map[i + 2, j, k]
                vc = position_map[i + 2, j, k + 1]
                vd = position_map[i, j, k + 1]
                faces.append([va, vb, vc])
                faces.append([va, vc, vd])
                
    faces = np.array(faces)
    mesh = trimesh.Trimesh(vertices=vs, faces=faces)
    
    animated_gif('out.gif', duration=5/60, frame_numbers=range(1, 361, 5))
    
def draw():
    py5.background(0, 100, 0)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.radians(py5.frame_count))
    py5.rotate_y(py5.radians(45))
    py5.translate(-py5.width / 2, -py5.height / 2)
    py5.fill(240)
    py5.shape(mesh)
    
py5.run_sketch(block=False)
