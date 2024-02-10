import trimesh  # install mapbox_earcut!    
import py5

from functools import cache

cube_list = []
hole_list = []

sf = 22 # scale/grid factor
rot90 = trimesh.transformations.rotation_matrix(py5.HALF_PI, [0, 1, 0])

def setup():
    global mesh_a, mesh_b
    py5.size(700, 700, py5.P3D)
    mesh_a, mesh_b = make_stuff_up()

def make_stuff_up():
    cube_list[:] = []
    hole_list[:] = []
    for _ in range(10):
        x, y, z = (int(py5.random(-5, 5)) * sf * 2,
                   int(py5.random(-5, 5)) * sf * 2,
                   int(py5.random(-5, 5)) * sf * 2)
        w = int(py5.random(5, 15)) * sf
        cube_list.append(cube(x, y, z, w, w, 15 * sf))
        hole_list.append(cube(x, y, z,
                              w - sf, w - sf, 15 * sf + 2))
    solid = cube_list[0]
    for c in cube_list[1:]:
        solid = solid.union(c)
    hole = hole_list[0]
    for c in hole_list[1:]:
        hole = hole.union(c)
        
    mesh_a = solid.difference(hole)
    mesh_b = mesh_a.copy().apply_transform(rot90)
    mesh_b = mesh_b.difference(solid)
    solid_b = solid.copy().apply_transform(rot90)
    mesh_a = mesh_a.difference(solid_b)

    return mesh_a, mesh_b

def draw():
    py5.background(150, 150, 250)
    py5.lights()
    if not py5.is_mouse_pressed:
        py5.no_stroke()
    else:
        py5.stroke(0)
    py5.fill(200, 240, 100)
    py5.translate(py5.width/2, py5.height/2, -py5.height/2)
    py5.rotate_y(py5.radians(py5.mouse_x))
    
    for mesh, c in ((mesh_a, py5.color(100, 0, 200)),
                    (mesh_b, py5.color(0, 100, 100))):
        py5.fill(c)
        draw_mesh(mesh)
    py5.window_title(str(round(py5.get_frame_rate())))

def cube(x, y, z, w, h=None, d=None):
    h = w or h
    d = d or h
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c


def draw_mesh(m):
    if  py5.is_key_pressed:
        with py5.begin_closed_shape(py5.TRIANGLES):
            py5.vertices(m.vertices[v]
                         for face in m.faces
                         for v in face)
    else:
        ps = convert_mesh(m)
        py5.shape(ps, 0, 0)

@cache
def convert_mesh(m):
    return py5.convert_shape(m)
    

def key_pressed():
    if py5.key == 's':
        py5.save_frame('######.png')
    elif py5.key == ' ':
        global mesh_a, mesh_b
        mesh_a, mesh_b = make_stuff_up()
    
py5.run_sketch(block=False)