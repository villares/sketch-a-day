import py5
import trimesh
import numpy as np

w = 10  # cols
h = 12  # rows
D = 100

def setup():
    global shp, mesh
    py5.size(500, 500, py5.P3D)
    py5.fill(255, 100)
    mesh = create_mesh(w, h, 50)
    shp = py5.convert_shape(mesh)
    
def draw():
    py5.background(0)
    py5.lights()
    py5.translate(250, 250, -500)
    py5.rotate_y(py5.radians(-45))
    py5.rotate_x(py5.radians(-45))
    py5.translate(-250, -250)
    
    # top mesh
    py5.shape(shp, 0, 0)
    
    py5.stroke(0, 0, 255)
    xa, ya, _ = vs[0]
    xb, yb, _ = vs[w-1]
    xd, yd, _ = vs[-w]
    xc, yc, _ = vs[-1]

    s0 = vs[:w]
    draw_poly([(xa, ya, D)] + s0 + [(xb, yb, D)]) 
    
    s1 = vs[::w]
    draw_poly([(xa, ya, D)] + s1 + [(xd, yd, D)]) 

    s2 = vs[-w:]
    draw_poly([(xd, yd, D)] + s2 + [(xc, yc, D)]) 
    
    s3 = vs[w-1::w]
    draw_poly([(xb, yb, D)] + s3 + [(xc, yc, D)]) 
    
    # floor
    draw_poly([(xa, ya, D), (xb, yb, D),
               (xc, yc, D), (xd, yd, D)]) 
     
   
def key_pressed():
    py5.save_frame('out.png')

def create_mesh(cols, rows, w):
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
    mesh = trimesh.Trimesh(vertices=vs, faces=faces)
    return mesh

def draw_poly(pts):
    with py5.begin_closed_shape():
        py5.vertices(pts) 
    

py5.run_sketch(block=False)