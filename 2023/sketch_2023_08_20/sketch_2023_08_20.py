import trimesh  # install mapbox_earcut!    
import py5

cube_list = []
hole_list = []

sf = 22 # scale/grid factor

def setup():
    global mesh
    py5.size(700, 700, py5.P3D)
    mesh = make_stuff_up()

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
    mesh = cube_list[0]
    for c in cube_list[1:]:
        mesh = mesh.union(c)
    hole = hole_list[0]
    for c in hole_list[1:]:
        hole = hole.union(c)
    mesh = mesh.difference(hole)
    #mesh = mesh.difference(cube(0, 0, 0, 400))
    return mesh

def draw():
    py5.background(100, 200, 100)
    py5.lights()
    if not py5.is_key_pressed:
        py5.no_stroke()
    else:
        py5.stroke(0)
    py5.fill(200, 240, 100)
    py5.translate(py5.width/2, py5.height/2, -py5.height/2)
    py5.rotate_y(py5.radians(py5.mouse_x))
    draw_mesh(mesh)

def cube(x, y, z, w, h=None, d=None):
    h = w or h
    d = d or h
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c
    
def draw_mesh(m):
#     for face in m.faces:
#         with py5.begin_closed_shape():
#             py5.vertices([m.vertices[v] for v in face])
    # this might be faster:
#     vs = []
#     for face in m.faces:
#         vs.extend(m.vertices[v] for v in face)
#     with py5.begin_closed_shape(py5.TRIANGLES):
#         py5.vertices(vs)
    # or maybe this:
    with py5.begin_closed_shape(py5.TRIANGLES):
        py5.vertices(m.vertices[v]
                     for face in m.faces
                     for v in face)    

def key_pressed():
    if py5.key == 's':
        py5.save_frame('######.png')
    elif py5.key == ' ':
        global mesh
        mesh = make_stuff_up()
    
py5.run_sketch(block=False)


