import py5
import numpy as np

def setup():
    global icosa
    py5.size(600, 600, py5.P3D)
    icosa = icosahedron(250)    
    icosa.set_fills(random_color() for _ in range(60))

def draw():
    py5.background(0)
    if py5.frame_count > 100:
        icosa.set_fills(random_color() for _ in range(60))
    py5.translate(py5.width / 2, py5.height / 2)
    py5.shape(icosa, 0, 0)

def random_color():
    return py5.color(py5.random_int(255), py5.random_int(255), py5.random_int(255))

def key_pressed():
    print(py5.key)
    if py5.key == 'a':
        icosa.set_fills(random_color() for _ in range(60))
    elif py5.key == 'b':
        icosa.set_fill(random_color())

def icosahedron(radius):
    global vs, sequence
    f = (radius / 2) # / 0.95 # aprox. ?
    phi = (py5.sqrt(5) + 1) / 2
    a = phi * f
    b = 1 * f
    vs = np.array([
        (a,  b,  0),
        (a,  -b,  0),
        (-a,  -b,  0),
        (-a,  b,  0),
        (b,  0, a),
        (-b,  0, a),
        (-b,  0, -a),
        (b, 0, -a),
        (0, a, b),
        (0, a, -b),
        (0, -a, -b),
        (0, -a, b),
    ])
    sequence = np.array([
        2, 11, 5, 2, 5, 3, 5, 8, 3, 4, 8, 5, 11, 4, 5,
        10, 2, 6, 2, 3, 6, 3, 9, 6, 3, 8, 9, 2, 10, 11,
        1, 4, 11, 1, 0, 4, 7, 0, 1, 10, 1, 11, 0, 8, 4,
        0, 9, 8, 7, 9, 0, 1, 10, 7, 10, 6, 7, 6, 9, 7,  
    ])
    shp = py5.create_shape()
    shp.begin_shape(py5.TRIANGLES)
    shp.vertices(vs[sequence])
    shp.end_shape()
    return shp

py5.run_sketch(block=False)
