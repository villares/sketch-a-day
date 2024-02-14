import functools

import py5
import trimesh # installed manifold3d with trimesh[all]

meshes = []

def setup():
    global tri
    py5.size(600, 600, py5.P3D)
    #py5.no_stroke()
    py5.no_stroke()
    
    for x in range(-500, 501, 50):
        b = xyz_box(x, 0, 0, 40)
        b.visual.face_colors[:] = 255, 0, 0, 255
        meshes.append(b)
    for y in range(-500, 501, 50):
        b = xyz_box(0, y, 0, 45)
        b.visual.face_colors[:] = 0, 255, 0, 255
        meshes.append(b)
    for z in range(-500, 501, 35):
        b = xyz_box(0, 0, z, 45)
        b.visual.face_colors[:] = 0, 0, 255, 255
        meshes.append(b)


#     hole = trimesh.creation.cylinder(190, 410)
#     tri = tri.difference(hole)
#     apply_rotation(hole, py5.PI / 2)
#     tri = tri.difference(hole)
#     apply_rotation(hole, py5.PI / 2, direction=(0, 0, 1))
#     tri = tri.difference(hole)
     
    
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

def xyz_box(x, y, z, w, h=None, d=None):
    h = h or w  # UGH! was wrong!
    d = d or h
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c
  
def apply_rotation(obj, angle, direction=[1, 0, 0], center=[0, 0, 0]):
    rot_matrix = trimesh.transformations.rotation_matrix(angle, direction, center)
    obj.apply_transform(rot_matrix)
  
def convert_objs(meshes):
    m = trimesh.util.concatenate(meshes)
    return convert_obj(m)
  
@functools.lru_cache(maxsize=128)
def convert_obj(obj):
   ps = py5.convert_shape(obj)
#  # Unnecessary, py5 gets the face colors!!!
#  # but I could meddle if I wanted to...
#    colors = []
#    for r, g, b, a in obj.visual.face_colors:
#        c = py5.color(r, g, b, a)
#        colors.extend((c, c, c))   
#    ps.set_fills(colors)
   return ps

py5.run_sketch(block=False)
