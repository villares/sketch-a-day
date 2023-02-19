from shapely import Polygon
import trimesh

pts = ((100, 100), (400, 100), (400, 400), (100, 400))
hole = ((150, 150), (350, 150), (350, 350), (150, 350))
p = Polygon(pts, [hole])
mesh = trimesh.creation.extrude_polygon(p, 100)
#mesh = trimesh.primitives.Extrusion(p, height=100)
other = mesh.copy()
other.apply_translation((150, 50, 50))
mesh = mesh.union(other)
#other.visual = trimesh.visual.ColorVisuals(
#    other,
#    [[255, 0, 0] for _ in other.visual.face_colors]
#     )
for i, face in enumerate(mesh.faces):
    x0, y0, z0 = mesh.vertices[face[0]]
    x1, y1, z1 = mesh.vertices[face[1]]
    x2, y2, z2 = mesh.vertices[face[2]]
    if x0 == x1 and y0 != y1:
        mesh.visual.face_colors[i][:] = 255, 0, 0, 255
#mesh.show()
import py5

def setup():
    py5.size(700, 700, py5.P3D)

def draw():
    py5.background(100, 200, 100)
    py5.translate(350, 0)
    py5.rotate_y(py5.radians(py5.mouse_x))
    py5.translate(-350, 0)
    draw_mesh(mesh)
    
def draw_mesh(m):
    for i, face in enumerate(m.faces):
        r, g, b, a = m.visual.face_colors[i]
        py5.fill(r, g, b, a)
        with py5.begin_closed_shape():
            py5.vertices([m.vertices[v] for v in face])

py5.run_sketch()