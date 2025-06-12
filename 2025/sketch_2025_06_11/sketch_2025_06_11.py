import py5, py5_tools
import shapely
import trimesh
import numpy as np

def setup():
    global subtracted_box, crescent_mesh
    py5.size(500, 500, py5.P3D)
    c = shapely.Point(0, 0).buffer(50)  # circle from point, buffer is radius
    d = shapely.affinity.translate(c, 50, 0)  # new translated circle
    crescent = c - d   # same as c.difference(d)
    crescent_mesh = trimesh.creation.extrude_polygon(crescent, 250)  # extrusion
    crescent_mesh.apply_translation((0, 0, -125))  # single argument, tuple
    apply_rotation(crescent_mesh, py5.PI/2, direction=(0, 1, 0))  # my rotation helper
    hole = trimesh_box(0, 0, 0, 180, 300, 180)
    square_tube = trimesh_box(0, 0, 0, 200).difference(hole)  
    plus = trimesh_box(0, 0, 0, 100, 50, 300).union(trimesh_box(0, 0, 0, 50, 100, 300))
    subtracted_box = square_tube.difference(crescent_mesh).difference(plus)
    # to export gif
    py5_tools.animated_gif('out.gif', duration=0.05, frame_numbers=range(1, 361, 3))
   
def draw():
    py5.background(0, 100, 100)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.PI / 8)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.fill(200, 200, 0)
    draw_mesh(subtracted_box)
    #py5.fill(0, 0, 100)       # to debug
    #draw_mesh(crescent_mesh)

def draw_mesh(m):
    vs = m.vertices
    bs = m.facets_boundary
    # draw the triangulated faces without stroke
    py5.push_style()  # this is so I can revert to previous stroke settings
    py5.no_stroke()
    with py5.begin_closed_shape(py5.TRIANGLES):
        py5.vertices(vs[np.concatenate(m.faces)])
    py5.pop_style()
    # now draw just the facet boundary lines
    a, b = np.vstack(bs).T
    py5.lines(np.column_stack((vs[a], vs[b])))
  
def apply_rotation(obj, angle, direction=[1, 0, 0], center=[0, 0, 0]):
    rot_matrix = trimesh.transformations.rotation_matrix(angle, direction, center)
    obj.apply_transform(rot_matrix)

def trimesh_box(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    mesh = trimesh.creation.box((w, h, d))
    mesh.apply_translation((x, y, z))  # in place!
    return mesh

py5.run_sketch(block=False)