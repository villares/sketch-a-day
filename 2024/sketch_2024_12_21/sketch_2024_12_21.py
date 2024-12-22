# Iscosahedron
import py5
from py5_tools import animated_gif
import numpy as np

def setup():
    py5.size(600, 600, py5.P3D)
    animated_gif('out.gif', duration=0.05,
                 frame_numbers=range(1, 361, 3))

def draw():
    global ang
    py5.background(0, 0, 100)
    py5.translate(py5.width / 2, py5.height / 2, -py5.height)
    ang = py5.radians(py5.frame_count)
    py5.rotate_y(ang)
    py5.rotate_x(py5.radians(15))
    icosahdron(300)

def icosahdron(radius):
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
        0, 1, 2, 3,
        4, 5, 6, 7,
        8, 9, 10, 11,
    ])
    py5.no_fill()
    py5.stroke_weight(2)
    #py5.circle(0, 0, radius * 2)
    py5.stroke(0)
    with py5.begin_shape(py5.QUADS):
         py5.vertices(vs[sequence])
    py5.stroke(255, 0, 0)
    py5.stroke_weight(6)
    py5.fill(255)
    py5.text_size(50)
    py5.text_align(py5.RIGHT)
    for i, v in enumerate(vs):
        with py5.push_matrix():
            py5.translate(*v)
            py5.point(0, 0, 0)
            py5.rotate_x(py5.radians(-15))
            py5.rotate_y(-ang)
            py5.text(i, -12, 12, 0)
            
py5.run_sketch(block=False)
