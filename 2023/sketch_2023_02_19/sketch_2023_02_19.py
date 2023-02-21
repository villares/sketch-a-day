
from shapely import Polygon
import trimesh

pts = ((100, 100), (400, 100), (400, 400), (100, 400))
hole = ((150, 150), (350, 150), (350, 350), (150, 350))
p = Polygon(pts, [hole])

mesh = trimesh.creation.extrude_polygon(p, 100)
other = mesh.copy()

other.apply_translation((150, 50, 50))
mesh = mesh.union(other).process()


colors = []
for f in mesh.faces:
    if any(other.bounding_box.contains([mesh.vertices[v] for v in f])):
        colors.append([255, 0, 0])
    else:
       colors.append([0, 0, 200])
mesh.visual = trimesh.visual.ColorVisuals(mesh, colors)
#mesh.show()
mesh.export('m.stl')
import py5

def setup():
    py5.size(700, 700, py5.P3D)

def draw():
    py5.background(100, 0, 100)
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