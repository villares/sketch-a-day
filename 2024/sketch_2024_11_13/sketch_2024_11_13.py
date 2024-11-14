import py5
import trimesh
import numpy as np

def setup():
    global shp, mesh
    py5.size(500, 500, py5.P3D)
    mesh = create_mesh(10, 10, 50)
    shp = py5.convert_shape(mesh)
    
def draw():
    py5.background(0)
    py5.lights()
    py5.translate(250, 250, -250)
    py5.rotate_x(py5.radians(py5.mouse_y))
    py5.translate(-250, -125)
    py5.shape(shp, 0, 0)
    py5.stroke_weight(10)
    py5.stroke(255, 0, 0)
    py5.translate(0, 0, -6)
    s0 = vs[:10]
    py5.points(s0)
    py5.points(vs[-10:])
    py5.stroke(0, 255, 0)
    py5.translate(0, 0, 3)
    py5.points(vs[::10])
    py5.points(vs[10-1::10])
    py5.stroke(0, 0, 255)
    py5.stroke_weight(2)
    x0, y0, _ = vs[0]
    x9, y9, _ = vs[10-1]
    py5.point(x0, y0, 100)
    py5.point(x9, y9, 100)
    py5.begin_shape()
    py5.vertices([(x0, y0, 100)] + s0 + [(x9, y9, 100)]) 
    py5.end_shape(py5.CLOSE)
    
def key_pressed():
    py5.save_frame('out.png')

def create_mesh(rows, cols, w):
    global vs
    def pos(col, row):
        return col + row * cols
    vs = []
    i = 0
    for row in range(rows):
        for col in range(cols):
            vs.append((col * w, row * w, py5.random(1) * w))
            i += 1
    faces = []
    for row in range(rows - 1):
        for col in range(cols - 1):
            a = pos(col, row)
            b = pos(col + 1, row)
            c = pos(col + 1, row + 1)
            d = pos(col, row + 1)            
            faces.append((a, b, c))
            faces.append((a, c, d))
    print(vs, faces)
    mesh = trimesh.Trimesh(vertices=vs, faces=faces)
    return mesh


py5.run_sketch(block=False)