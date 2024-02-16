import functools

import py5
import trimesh # pip install trimesh[all]

meshes = []

def setup():
    global tri
    py5.size(600, 600, py5.P3D)
    #py5.no_stroke()
    py5.no_stroke()
    
    for x in range(-500, 501, 50):
        b = xyz_box(x, 0, 0, 40, 400, 40)
        mesh_rotate(b, py5.radians(x/10), axis=0)
        b.visual.face_colors[:] = x % 255, 255 - (x % 255), 255, 255
        meshes.append(b)
#     for y in range(-500, 501, 50):
#         b = xyz_box(0, y, 0, 45, 45, 45)
#         b.visual.face_colors[:] = 0, 255, 0, 255
#         meshes.append(b)
#     for z in range(-500, 501, 50):
#         b = xyz_box(0, 0, z, 35, 35, 35)
#         b.visual.face_colors[:] = 0, 0, 255, 255
#         meshes.append(b)
 

def draw():
    py5.background(240)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.radians(py5.mouse_y))
    py5.rotate_y(py5.radians(py5.mouse_x))
    py5.scale(0.6)
    
    pshape = convert_meshes(meshes)
    py5.shape(pshape, 0, 0)    

def key_pressed():
    py5.save(__file__[:-2] + 'png')

def xyz_box(x, y, z, w, h, d):
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c
  
def mesh_rotate_x(obj, angle, center=[0, 0, 0]):
    rm = trimesh.transformations.rotation_matrix(angle, (1, 0, 0), center)
    obj.apply_transform(rm)

def mesh_rotate_x(obj, angle, center=[0, 0, 0]):
    rm = trimesh.transformations.rotation_matrix(angle, (1, 0, 0), center)
    obj.apply_transform(rm)

def mesh_rotate_y(obj, angle, center=[0, 0, 0]):
    rm = trimesh.transformations.rotation_matrix(angle, (0, 1, 0), center)
    obj.apply_transform(rm)

def mesh_rotate_z(obj, angle, center=[0, 0, 0]):
    rm = trimesh.transformations.rotation_matrix(angle, (0, 0, 1), center)
    obj.apply_transform(rm)

def mesh_rotate(obj, angle, axis=2, center=[0, 0, 0]):
    """
    Rotate a trimesh object by an angle around axis
    0: X, 1: Y, 2: Z (by default Z)
    centered on the origin [0, 0, 0] by default
    """
    direction = ((1, 0, 0), (0, 1, 0), (0, 0, 1))[axis]
    rm = trimesh.transformations.rotation_matrix(angle, direction, center)
    obj.apply_transform(rm)


def convert_meshes(meshes):
    m = trimesh.util.concatenate(meshes)
    return convert_obj(m)
  
@functools.lru_cache(maxsize=128)
def convert_obj(obj):
   return py5.convert_shape(obj)


py5.run_sketch(block=False)

