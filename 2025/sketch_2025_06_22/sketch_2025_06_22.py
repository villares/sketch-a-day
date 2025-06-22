import py5
import numpy as np
import trimesh

def setup():
    global mesh
    py5.size(400, 400, py5.P3D)

    x = np.linspace(-1, 1, 10) * 50
    y = np.linspace(-1, 1, 10) * 50
    x, y = np.meshgrid(x, y)
    z = (np.sin(py5.radians(x) * 5) + np.cos(py5.radians(y) * 5)) * 10 
    vs = np.column_stack((x.flatten(), y.flatten(), z.flatten()))
    faces = []
    for i in range(10 - 1):
        for j in range(10 - 1):
            v1 = i * 10 + j
            v2 = (i + 1) * 10 + j
            v3 = (i + 1) * 10 + (j + 1)
            v4 = i * 10 + (j + 1)
            faces.append([v1, v2, v3])
            faces.append([v1, v3, v4])
    #vs2d = np.column_stack((x.flatten(), y.flatten()))
    #mesh = trimesh.creation.extrude_triangulation(vs2d, faces, 50)
    mesh = trimesh.Trimesh(vertices=vs, faces=faces)

def draw():
    py5.background(0, 200, 200)
    py5.translate(200, 200, 200)
    py5.rotate_x(py5.PI / 6)
    py5.shape(mesh)

py5.run_sketch(block=False)
