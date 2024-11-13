import py5
import trimesh
import numpy as np

    
def setup():
    py5.size(500, 500, py5.P3D)
    py5.background(0)
    py5.lights()
    mesh = create_trimesh_surface(8, 6, 50)
    shp = py5.convert_shape(mesh)
    py5.translate(250, 250)
    py5.rotate_x(py5.radians(45))
    py5.shape_mode(py5.CENTER)
    py5.shape(shp, 0, 0)
    py5.save_frame('out.png')

def create_trimesh_surface(rows, cols, spacing):
    w = spacing
    grid = {}
    vs = []
    i = 0
    for row in range(rows):
        for col in range(cols):
            grid[col, row] = i
            vs.append((col * w, row * w, py5.random(1) * w))
            i += 1
    faces = []
    for row in range(rows - 1):
        for col in range(cols - 1):
            a = grid[col, row]
            b = grid[col + 1, row]
            c = grid[col + 1, row + 1]
            d = grid[col, row + 1]            
            faces.append((a, b, c))
            faces.append((a, c, d))
    print(vs, faces)
    mesh = trimesh.Trimesh(vertices=vs, faces=faces)
    return mesh


#mesh.show()
py5.run_sketch(block=False)