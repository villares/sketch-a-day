import py5
import numpy as np
import trimesh

def setup():
    global mesh, faces, vs, x, y, z
    py5.size(400, 400, py5.P3D)
    cols = 15
    rows = 15
    vs = []
    faces = []
    w = 8
    for i in range(rows):
        for j in range(cols):
            x = j * w - (w * cols) / 2
            y = i * w - (w * rows) / 2
            z = py5.sin(py5.dist(x, y, 0, 0) / w) * w
            vs.append((x, y, z))
    for i in range(rows - 1):
        for j in range(cols - 1):
            v1 = i * cols + j
            v2 = (i + 1) * cols + j
            v3 = (i + 1) * cols + (j + 1)
            v4 = i * cols + (j + 1)
            faces.append([v1, v2, v3])
            faces.append([v1, v3, v4])

    mesh = trimesh.Trimesh(vertices=vs, faces=faces)

def draw():
    py5.background(0, 200, 200)
    py5.lights()
    py5.translate(200, 200, 200)
    py5.rotate_x(py5.PI / 6)
    py5.shape(mesh)

py5.run_sketch(block=False)
