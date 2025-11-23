# from https://github.com/py5coding/python-brasil-2025/blob/main/prototypes/revolve.py

import facets
import numpy as np
import py5
from trimesh import creation
# check https://py5coding.org/how_tos/use_processing_libraries.html
from peasy import PeasyCam  

# pay attention to clockwise vs counterclockwise
linestring = np.array(
    [[0.0,     0.0], [50.0, -50.0], [100.0, 0.0],
     [100.0, 100.0], [50.0, 150.0], [0.0, 100.0],  
     [0.0, 0.0]
     ]
) + np.array([[50.0, 0.0]])

def setup():
    global shape
    py5.size(800, 800, py5.P3D)

    py5.fill(255, 200, 0)
    py5.stroke(0)
    py5.stroke_weight(3)
    cam = PeasyCam(py5.get_current_sketch(), 500)
    
    shape = py5.convert_shape(
        creation.revolve(
            linestring,
            angle=-py5.PI,
            sections=6,
            cap=True
            ),
        min_angle=0.1,
    )

def draw():
    py5.background(204, 100, 100)
    py5.lights()
    #py5.translate(py5.width / 2, py5.height / 2, -200)
    #py5.scale(2)
    py5.shape(shape)


py5.run_sketch(block=False)  # remove block=False on MacOS