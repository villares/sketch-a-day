import trimesh
from trimesh.transformations import translation_matrix

import numpy as np
import py5  # check out https://github.com/py5coding 
from py5_tools import animated_gif


def setup():   # py5 will call this once to set things up
    global shp, e
    py5.size(600, 600, py5.P3D)
    ca = trimesh.primitives.Cylinder(radius=100, height=200, sections=32)
    cb = ca.copy()
    cb.apply_translation([50, 50, 50])
    cc = ca.union(cb)
    shp = py5.create_shape(py5.GROUP)
    xmin, xmax = cc.bounds[:, 0]
    ymin, ymax = cc.bounds[:, 1]
    slices_2d = cc.section_multiplane(
        (0, 0, 0), (1, 0, 0), np.linspace(2 * xmin, 2 * xmax, num=30)
    )
    for s, z in zip(slices_2d, np.linspace(2 * xmin, 2 * xmax, num=30)):
        if s is not None:
            t = translation_matrix([0, 0, z])
            e = s.extrude(5)
            e.apply_transform(t)
            py5.stroke(255, 0, 0)
            c = py5.convert_shape(e)
            shp.add_child(c)           
#     slices_2d = cc.section_multiplane(
#         (0, 0, 0), (1, 0, 1), np.linspace(2 * ymin, 2 * ymax, num=30)
#     )
#     for s, z in zip(slices_2d, np.linspace(2 * ymin, 2 * ymax, num=30)):
#         if s is not None:
#             t = translation_matrix([0, 0, z])
#             e = s.extrude(5)
#             e.apply_transform(t)
#             py5.stroke(0, 255, 0)
#             c = py5.convert_shape(e)
#             shp.add_child(c)           

    #shp.disable_style()
    


def draw():   # py5 will call this in a loop
    py5.background(0)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.shape(shp)

    
def key_pressed():   # py5 will call this when a key is pressed
    if py5.key == 's':
        f = py5.frame_count
        animated_gif('out3.gif', frame_numbers=range(f + 1, f + 361, 4), duration=0.075) 
        
py5.run_sketch(block=False)
        
        



