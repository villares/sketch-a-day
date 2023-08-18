from shapely import Polygon
import trimesh  # install mapbox_earcut!

cube_list = []
    
import py5

def setup():
    global mesh
    py5.size(700, 700, py5.P3D)
    for _ in range(10):
        cube_list.append(cube(py5.random(-200, 200),
                              py5.random(-200, 200),
                              py5.random(-200, 200), 200))
    
    mesh = cube_list[0]
    for c in cube_list[1:]:
        mesh = mesh.union(c)


def draw():
    py5.lights()
    py5.no_stroke()
    py5.background(100, 200, 100)
    py5.lights()
    py5.no_stroke()
    py5.translate(py5.width/2, py5.height/2, -py5.height/2)
    py5.rotate_y(py5.radians(py5.mouse_x))
    draw_mesh(mesh)

def cube(x, y, z, w=100):
    hw = w / 2 
    pts = ((-hw, -hw), (hw, -hw), (hw, hw), (-hw, hw))
    c = trimesh.creation.extrude_polygon(Polygon(pts), w)
    c.apply_translation((x, y, z - hw))
    return c
    #trimesh.creation.box(w 

def draw_mesh(m):
    for i, face in enumerate(m.faces):
        with py5.begin_closed_shape():
            py5.vertices([m.vertices[v] for v in face])

py5.run_sketch(block=False)
