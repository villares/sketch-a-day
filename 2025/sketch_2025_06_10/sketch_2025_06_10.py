# py5 imported mode code: learn about it at py5coding.org

import shapely
from shapely import Polygon, Point, LineString
from shapely.affinity import translate as s_translate
import trimesh

def setup():
    global subtracted_box
    size(500, 500, P3D)
    c = Point(50, 50).buffer(50)  # buffer com o raio
    d = s_translate(c, 50, 0)
    crescent = c - d
    m = trimesh.creation.extrude_polygon(crescent, 100)
    b = trimesh_box(0, 0, 0, 200)
    subtracted_box = b.difference(m)

def draw():
    background(0, 0, 100)
    lights()
    translate(width / 2, height / 2)
    rotate_y(radians(mouse_x))
    fill(0, 200, 0)
    draw_mesh(subtracted_box)
     
def trimesh_box(x, y, z, w, h=None, d=None):
    h = w or h
    d = d or h
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c

def draw_mesh(m):
    vs = m.vertices
    bs = m.facets_boundary
    # draw the triangulated faces without stroke
    push_style()  # so I can revert to previous stroke settings
    no_stroke()
#     with begin_closed_shape(TRIANGLES):
#         vertices(m.vertices[v]
#                  for face in m.faces
#                  for v in face)
    with begin_closed_shape(TRIANGLES):
        vertices(vs[np.concatenate(m.faces)])
    pop_style()
    # now draw the facet boundary edges
#     for facet in bs:
#         for a, b in facet:
#             line(*vs[a], *vs[b])
    a, b = np.vstack(bs).T
    lines(np.column_stack((vs[a], vs[b])))
  
def apply_rotation(obj, angle, direction=[1, 0, 0], center=[0, 0, 0]):
    rot_matrix = trimesh.transformations.rotation_matrix(angle, direction, center)
    obj.apply_transform(rot_matrix)
