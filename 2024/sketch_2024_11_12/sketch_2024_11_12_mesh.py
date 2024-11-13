from random import random
import trimesh

def create_trimesh_surface(vs, rows, cols):
    if len(vs) != rows * cols:
        raise ValueError("Number of points doesn't match rows * columns")
    faces = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            k = i * cols + j
            faces.append([k, k + cols, k + 1])
            faces.append([k + 1, k + cols, k + cols + 1])
    mesh = trimesh.Trimesh(vertices=vs, faces=faces)
    return mesh

rows, cols = 6, 8 
pts = [(x, y, x + y + random()) for x in range(rows) for y in range(cols)]
mesh = create_trimesh_surface(pts, rows, cols)
mesh.show()
