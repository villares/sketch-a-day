import functools

import py5
import trimesh # pip install trimesh[all]

tubes = []
holes = []

def setup():
    py5.size(600, 600, py5.P3D)
    py5.no_stroke()
    gerar_formas()
    #py5.color_mode(py5.HSB)
    #py5.shape_mode(py5.CENTER)
   
def gerar_formas():
    tubes.clear()
    holes.clear()
    for i in range(50):
        x = py5.random_int(-50, 50) * 10
        y = py5.random_int(-50, 50) * 10
        z = py5.random_int(-50, 50) * 10
        b = xyz_tub(x, y, z, 200, 1600)
        mesh_rotate_y(b, py5.radians(x/20), center=(x, y, z))
        tubes.append(b)
        h = xyz_tub(x, y, z, 150, 1605)
        mesh_rotate_y(h, py5.radians(x/20), center=(x, y, z))
        holes.append(h)
    big_hole = trimesh.boolean.union(holes)
    for i, b in enumerate(tubes):
        tubes[i] = b.difference(big_hole)
        tubes[i].visual.face_colors[:] = (
            (i * 32) % 255,
            (i * 64) % 255,
            (i * 128) % 255,
            255
            )
    
def draw():
    py5.background(0)
    py5.lights()
    #py5.ambient_light(32, 32, 32)
    py5.translate(py5.width / 2,
                  py5.height / 2,
                  -2000)
    #py5.rotate_x(py5.radians(py5.mouse_y))
    py5.rotate_y(py5.radians(py5.mouse_x))
    #py5.scale(0.5)
    
    S = 1000
    m = 0 # py5.remap(py5.mouse_y, 0, py5.width, 0, 1)
    for i, b in enumerate(tubes):
        pshape = convert_obj(b)
        py5.shape(pshape, m * i * S, m * i * S)    

def key_pressed():
    if py5.key == ' ':
        gerar_formas()
    elif py5.key == 's':
        py5.save_frame('####.png')

def xyz_tub(x, y, z, w, d):
    c = trimesh.creation.cylinder(w / 2, d)
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



