"""
Using "orthogonal" projection. A grid of 25 yellow cubes with circular holes on every face,
on a black background. They start rotating and then stop.
"""

from itertools import product

import py5
from py5_tools import animated_gif
import trimesh # install manifold3d


def setup():
    global shp
    py5.size(800, 800, py5.P3D)
    #py5.no_stroke()
    py5.fill(200, 200, 0)
    tri = xyz_box(0, 0, 0, 200)
    hole = trimesh.creation.cylinder(90, 210)
    tri = tri.difference(hole)
    apply_rotation(hole, py5.PI / 2)
    tri = tri.difference(hole)
    apply_rotation(hole, py5.PI / 2, direction=(0, 0, 1))
    tri = tri.difference(hole)
    py5.no_stroke()
    shp = py5.convert_cached_shape(tri)
#    animated_gif('out.gif', duration=0.066, frame_numbers=range(1, 361, 4))


def draw():
    py5.background(0)
    py5.ortho()
    #py5.lights()
    py5.directional_light(255, 255, 255, 0, 0, -1)
    py5.random_seed(1)
    ra = (0, py5.PI / 2, py5.PI / 3, py5.PI / 4, py5.PI / 6)
    for x, y in product(range(100, py5.width, 150),  range(100, py5.width, 150)):
        with py5.push_matrix():
            py5.translate(y, x)
            py5.scale(0.4)
            f = py5.frame_count
            a = py5.radians(f) if f > 180 else 0
            py5.rotate_x(py5.random_choice(ra) + a)
            py5.rotate_y(py5.random_choice(ra) + a)
            py5.shape(shp, 0, 0)    
    if f == 1:
        py5.save('static.gif')


def key_pressed():
    py5.save(__file__[:-2] + 'png')

def xyz_box(x, y, z, w, h=None, d=None):
    h = w or h
    d = d or h
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c
  
def apply_rotation(obj, angle, direction=[1, 0, 0], center=[0, 0, 0]):
    rot_matrix = trimesh.transformations.rotation_matrix(angle, direction, center)
    obj.apply_transform(rot_matrix)
  



py5.run_sketch(block=False)