import functools

import py5
import trimesh # installed manifold3d with trimesh[all]

meshes = []
X, Y, Z = 'xyz'

def setup():
    global tri
    py5.size(600, 600, py5.P3D)
    #py5.no_stroke()
    py5.no_stroke()
    
    for x in range(-500, 501, 50):
        b = xyz_box(x, 0, 0, 40, 40, 40)
        b.visual.face_colors[:] = 255, 0, 0, 255
        meshes.append(b)
    for y in range(-500, 501, 50):
        b = xyz_box(0, y, 0, 45, 45, 45)
        b.visual.face_colors[:] = 0, 255, 0, 255
        meshes.append(b)
    for z in range(-500, 501, 50):
        b = xyz_box(0, 0, z, 35, 35, 35)
        b.visual.face_colors[:] = 0, 0, 255, 255
        meshes.append(b)
    b = xyz_box(-100, 100, 100, 100, 200, 300)
    meshes.append(b)
    b = xyz_box(100, 100, 100, 100, 200, 300)
    rotate_mesh(b, py5.radians(30), direction=X)
    meshes.append(b)


def draw():
    py5.background(240)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.radians(py5.mouse_y))
    py5.rotate_y(py5.radians(py5.mouse_x))
    py5.scale(0.6)
    
    pshape = convert_objs(meshes)
    py5.shape(pshape, 0, 0)    

def key_pressed():
    py5.save(__file__[:-2] + 'png')

def xyz_box(x, y, z, w, h, d):
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c
  
def rotate_mesh(obj, angle, direction=Z, center=[0, 0, 0]):
    d = {X: (1, 0, 0), Y: (0, 1, 0), Z: (0, 0, 1)}[direction]
    rot_matrix = trimesh.transformations.rotation_matrix(angle, d, center)
    obj.apply_transform(rot_matrix)
  
def convert_objs(meshes):
    m = trimesh.util.concatenate(meshes)
    return convert_obj(m)
  
@functools.lru_cache(maxsize=128)
def convert_obj(obj):
   return py5.convert_shape(obj)


py5.run_sketch(block=False)
