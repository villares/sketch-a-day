import py5
import py5_tools 
import trimesh
import numpy as np

def setup():
    global a, b, c, d, e
    py5.size(500, 500, py5.P3D)
    a = box_mesh(0, 0, 0, 200)
#     b = a.copy()
#     apply_rotation(b, py5.radians(45), direction=(0, 0, 1))
#     apply_rotation(b, py5.radians(45), direction=(0, 1, 0))
    c = a.copy()
    apply_rotation(c, py5.radians(45), direction=(0, 0, 1))
    apply_rotation(c, py5.radians(45), direction=(1, 0, 0))
    d = a.copy()
    apply_rotation(d, py5.radians(45), direction=(1, 0, 0))
    apply_rotation(d, py5.radians(45), direction=(0, 1, 0))
#     e = a.copy()
#     apply_rotation(e, py5.radians(45), direction=(1, 0, 0))
#     apply_rotation(e, py5.radians(45), direction=(0, 0, 1))      
#     a = a.intersection(b)
    e = c.intersection(d)
    # Export animation, skip empty frame 0 created on setup
    py5_tools.animated_gif('demo_mesh.gif', duration=0.08,
                           frame_numbers=range(1, 361, 5)) 

def draw():
    py5.background(200, 0, 200)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.PI / 8)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.stroke_weight(2)
    py5.fill(0, 200, 200)
    py5.stroke(0)
    draw_mesh(e)
    if py5.is_key_pressed:
        py5.scale(1.01)
        py5.no_fill()
        py5.stroke(255)
        draw_mesh(c)
        draw_mesh(d)
    
def box_mesh(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    mesh = trimesh.creation.box((w, h, d))
    mesh.apply_translation((x, y, z))
    return mesh
    
def apply_rotation(mesh, angle, direction=[1, 0, 0], center=[0, 0, 0]):
    rot_matrix = trimesh.transformations.rotation_matrix(angle, direction, center)
    mesh.apply_transform(rot_matrix)
    
def draw_mesh(m):
    vs = m.vertices
    bs = m.facets_boundary
    py5.push_style()  # To be able to get the stroke settings back
    py5.no_stroke()   # Turn off strokes, to draw without edges
    # Draw triangulated faces without edges
    with py5.begin_closed_shape(py5.TRIANGLES):
        py5.vertices(vs[np.concatenate(m.faces)])
    py5.pop_style() # Get previous stroke settings
    # Draw only edges that are facet boundaries
    a, b = np.vstack(bs).T
    py5.lines(np.column_stack((vs[a], vs[b])))
    
py5.run_sketch()
