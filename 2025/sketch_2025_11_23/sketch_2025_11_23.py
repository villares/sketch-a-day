# This code is an example of py5 <py5coding.org> in module mode
# based on https://github.com/py5coding/python-brasil-2025/blob/main/prototypes/sweep.py

import py5
import numpy as np
import trimesh
from shapely import Polygon

# # check https://py5coding.org/how_tos/use_processing_libraries.html
# import py5_tools
# py5_tools.processing.download_library("PeasyCam")
from peasy import PeasyCam  # the cool & easy Processing orbit camera cam

import facets  # the beautiful edge filtering feature, soon on a py5 release!

R = 40
V = 16
section = Polygon([
    ((R if i % 2 else R * 0.75) * py5.cos(i * py5.TWO_PI / V), 
     (R if i % 2 else R * 0.75) * py5.sin(i * py5.TWO_PI / V))
     for i in range(V)
]) 
N = 180
angles = np.linspace(0, py5.PI, N)
section = section - section.buffer(-R/4)
path = np.array(
    [
        [0.0, 0.0, 0.0],
        [100.0, 0.0, 0.0],
        [100.0, 100.0, 0.0],
       # [50.0, 250.0, 0.0],
        [0.0, 100.0, 0.0],
    ]
) - np.array([[50.0, 50.0, 0.0]])
trimesh_path = trimesh.path.simplify.resample_spline(
    path,
    smooth=0.2,
    count=N
)

def setup():
    global shape
    py5.size(800, 800, py5.P3D)

    py5.fill(200, 255, 0)
    py5.stroke(0)
    py5.stroke_weight(3)
    cam = PeasyCam(py5.get_current_sketch(), 500)
    shape = py5.convert_shape(
        trimesh.creation.sweep_polygon(
            section, trimesh_path,
            cap=True,
            angles=angles,
        ),
        min_angle=1,
    )

def draw():
    py5.background(100, 100, 205)
    py5.lights()
    # py5.translate(py5.width / 2, py5.height / 2, -200) # not needed with PeasyCam
    py5.shape(shape)

py5.run_sketch(block=False)  # remove block=False on MacOS