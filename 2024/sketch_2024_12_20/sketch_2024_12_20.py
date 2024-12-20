# Tetrahedron
import py5
from py5_tools import animated_gif
import numpy as np

def setup():
    py5.size(600, 600, py5.P3D)
    animated_gif('out.gif', duration=0.05,
                 frame_numbers=range(1, 361, 3))

def draw():
    py5.background(0, 0, 100)
    py5.translate(py5.width / 2, py5.height / 2, -py5.height)
    py5.rotate_y(py5.radians(py5.frame_count))
    tetrahdron(300)

def tetrahdron(radius):
    a = radius / 3 * 2
    vs = np.array([(a,  a,  a), (-a, -a,  a),
                   (-a, a, -a), ( a, -a, -a)])
    sequence = np.array([0, 1, 2, 3, 0, 1, 3, 2, 1])
    with py5.begin_shape(py5.TRIANGLE_STRIP):
        py5.vertices(vs[sequence])
                        
py5.run_sketch(block=False)
