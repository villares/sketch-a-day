# Iscosahedron
import py5
from py5_tools import animated_gif
import numpy as np

sf = 2

def setup():
    py5.size(600, 600, py5.P3D)
    animated_gif('out.gif', duration=0.066,
                   frame_numbers=range(1, 361, 3))
    py5.hint(py5.ENABLE_STROKE_PERSPECTIVE)

def draw():
    global ang
    py5.translate(py5.width / 2, py5.height / 2, -py5.height)
    ang = py5.radians(py5.frame_count)
    py5.rotate_y(ang)
    py5.rotate_x(ang)
    py5.background(0, 0, 150)
    py5.no_fill()
    py5.stroke_weight(3 * sf)
    py5.stroke(0)
    icosahdron(py5.width / 3 * 2)
    # the numbered faces
    tris = sequence.reshape(20,3)
    face_centers = vs[tris].mean(axis=1)    
    py5.stroke(255, 0, 0)
    py5.stroke_weight(6 * sf)
    py5.fill(255)
    py5.text_size(50)
    py5.text_align(py5.RIGHT)
    for i, v in enumerate(face_centers):
        with py5.push_matrix():
            py5.translate(*v)
            py5.point(0, 0, -1)
            py5.rotate_x(-ang)
            py5.rotate_y(-ang)
            py5.text(i, -12, 12, -5)

def icosahdron(radius):
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
    with py5.begin_shape(py5.TRIANGLES):
         py5.vertices(vs[sequence])

    
py5.run_sketch(block=False)
