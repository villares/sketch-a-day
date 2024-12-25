import py5
from py5_tools import animated_gif
import numpy as np

def setup():
    global icosa
    py5.size(600, 600, py5.P3D)
#     animated_gif('out.gif', duration=0.1,
#                    frame_numbers=range(1, 361, 4),
#                    optimize=False)
    icosa = icosahedron(250)    
    #icosa.set_stroke(False)
    icosa.set_fills(random_color() for _ in range(60))


def draw():
    global ang
    ang = py5.radians(py5.frame_count)
    py5.background(0, 0, 150)
    #py5.lights()
    py5.directional_light(255, 255, 255, 1, 1, -2)
    py5.stroke_weight(2)
    py5.translate(py5.width / 2, py5.height / 2)
    ang = py5.radians(py5.frame_count)
    py5.rotate_y(ang)
    py5.rotate_x(ang)
    
    #icosa.set_fill(random_color())
    py5.shape(icosa, 0, 0)

def random_color():
    return py5.color(py5.random_int(255), py5.random_int(255), py5.random_int(255))

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
# 
# def tetrahedron(radius):
#     a = radius / 3 * 2
#     vs = np.array([(a,  a,  a), (-a, -a,  a),
#                    (-a, a, -a), ( a, -a, -a)])
#     sequence = np.array([0, 1, 2, 3, 0, 1, 3, 2, 1])
#     with py5.begin_shape(py5.TRIANGLE_STRIP):
#         py5.vertices(vs[sequence])
#  
# def dodecahedron(radius):
#     a = radius / 1.618033989
#     b = radius
#     c = 0.618033989 * a
#     vs = np.array([
#         (a, a, a), (a, a, -a), (a, -a, a), (a, -a, -a), (-a, a, a),
#         (-a, a, -a), (-a, -a, a), (-a, -a, -a), (0, c, b), (0, c, -b),
#         (0, -c, b), (0, -c, -b), (c, b, 0), (c, -b, 0), (-c, b, 0),
#         (-c, -b, 0), (b, 0, c), (b, 0, -c), (-b, 0, c), (-b, 0, -c),
#         ])
#     faces = np.array([
#         (0, 16, 2, 10, 8), (0, 8, 4, 14, 12), (16, 17, 1, 12, 0),
#         (1, 9, 11, 3, 17), (1, 12, 14, 5, 9), (2, 13, 15, 6, 10),
#         (13, 3, 17, 16, 2), (3, 11, 7, 15, 13), (4, 8, 10, 6, 18),
#         (14, 5, 19, 18, 4), (5, 19, 7, 11, 9), (15, 7, 19, 18, 6)
#         ])
#     for face in faces:
#         with py5.begin_closed_shape():
#             py5.vertices(vs[face])
#  
# def octahedron(radius):
#     a = radius
#     vs = np.array([(a, 0, 0), (0, a, 0), (0, 0, a), (-a, 0, 0), (0, -a, 0), (0, 0, -a)])
#     with py5.begin_shape(py5.TRIANGLE_FAN):
#         sequence = np.array([4, 0, 2, 3, 5, 0])
#         py5.vertices(vs[sequence])
#     with py5.begin_shape(py5.TRIANGLE_FAN):
#         sequence = np.array([1, 0, 2, 3, 5, 0])
#         py5.vertices(vs[sequence])
# 
# def octahedron(radius):
#     a = radius
#     vs = np.array([(a, 0, 0), (0, a, 0), (0, 0, a), (-a, 0, 0), (0, -a, 0), (0, 0, -a)])
#     with py5.begin_shape(py5.TRIANGLE_FAN):
#         sequence = np.array([4, 0, 2, 3, 5, 0])
#         py5.vertices(vs[sequence])
#     with py5.begin_shape(py5.TRIANGLE_FAN):
#         sequence = np.array([1, 0, 2, 3, 5, 0])
#         py5.vertices(vs[sequence])
# 
# 
# def hexahedron(radius):
#     a = radius / py5.sqrt(3)  # hald the side
#     vs = np.array([
#         (-a, -a,  a), (-a,  a,  a), (a,  a,  a), (a, -a,  a),
#         (-a, -a, -a), (-a,  a, -a), (a,  a, -a), (a, -a, -a),
#         ])
#     sequence = np.array([0, 1, 2, 3, 4, 5, 6, 7,
#                          0, 1, 5, 4, 2, 3, 7, 6,
#                          0, 4, 7, 3, 1, 5, 6, 2])
#     with py5.begin_shape(py5.QUADS):
#         py5.vertices(vs[sequence])
# 

py5.run_sketch(block=False)
