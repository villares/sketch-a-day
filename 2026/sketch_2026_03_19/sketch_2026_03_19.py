# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

import py5
from py5_tools import animated_gif
import numpy as np

# https://en.wikipedia.org/wiki/Melencolia_I
# João @introsocopia sent me the vertex data :)

ds = """o Durers_Solid 
v 0.000000 -0.719944 0.347016
v 0.000000 -0.411397 0.644458
v -0.356280 0.205698 0.644458
v -0.623490 0.359972 0.347016
v -0.623490 -0.359972 -0.347016
v 0.000000 0.719944 -0.347016
v 0.000000 0.411397 -0.644458
v -0.356280 -0.205698 -0.644458
v 0.623490 -0.359972 -0.347016
v 0.356280 -0.205698 -0.644458
v 0.623490 0.359972 0.347016
v 0.356280 0.205698 0.644458
s 0
f 3 4 5 1 2
f 8 5 4 6 7
f 7 6 11 9 10
f 2 1 9 11 12
f 10 9 1 5 8
f 12 11 6 4 3
f 8 7 10
f 12 3 2
"""

vs = []
faces = []
for li in ds.splitlines():
    match li.split():        
        case 'v', *tail:
            vs.append([float(n) for n in tail]) # or tuple(map(float, tail))
        case 'f', *tail:
            faces.append(np.array([int(i) - 1 for i in tail]))
vs = np.array(vs) 

def setup():
    py5.size(600, 600, py5.P3D)
    animated_gif('out.gif', duration=0.06, frame_numbers=range(1, 361, 4))

def draw():
    py5.background(0, 0, 100)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.scale(200)
    py5.stroke_weight(1/100)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.rotate_x(py5.radians(110))
    for f in faces:
        with py5.begin_closed_shape():
            py5.vertices(vs[f])
            
py5.run_sketch(block=False)
