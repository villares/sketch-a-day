import functools

import py5
import trimesh # install manifold3d


def setup():
    global tri
    py5.size(800, 400, py5.P3D)
    #py5.no_stroke()
    py5.fill(200, 200, 0)
    tri = xyz_box(0, 0, 0, 400)
    hole = trimesh.creation.cylinder(190, 410)
    tri = tri.difference(hole)
    apply_rotation(hole, py5.PI / 2)
    tri = tri.difference(hole)
    apply_rotation(hole, py5.PI / 2, direction=(0, 0, 1))
    tri = tri.difference(hole)
    
    
    
def draw():
    py5.background(240)
    py5.lights()
    py5.translate(400, 200)
    py5.rotate_x(py5.radians(py5.mouse_y))
    py5.rotate_y(py5.radians(py5.mouse_x))
    py5.scale(0.6)
    
    pshape = convert_obj(tri)
    py5.shape(pshape, 0, 0)    

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
  
@functools.cache
def convert_obj(obj):
   return py5.convert_shape(obj)


py5.run_sketch(block=False)