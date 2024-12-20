# Octahedron

import py5
from py5_tools import animated_gif
import numpy as np

def setup():
    py5.size(600, 600, py5.P3D)
    animated_gif('out.gif', duration=0.1,
                 frame_numbers=range(1, 361, 3))

def draw():
    py5.background(0, 0, 100)
    py5.translate(py5.width / 2, py5.height / 2, -py5.height)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.rotate_x(py5.radians(py5.frame_count * 2))
    octahedron(400)

def octahedron(radius):
    a = radius
    vs = np.array([(a, 0, 0), (0, a, 0), (0, 0, a), (-a, 0, 0), (0, -a, 0), (0, 0, -a)])
    with py5.begin_shape(py5.TRIANGLE_FAN):
        sequence = np.array([4, 0, 2, 3, 5, 0])
        py5.vertices(vs[sequence])
    with py5.begin_shape(py5.TRIANGLE_FAN):
        sequence = np.array([1, 0, 2, 3, 5, 0])
        py5.vertices(vs[sequence])


py5.run_sketch(block=False)
