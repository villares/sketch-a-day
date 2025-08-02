import py5
import py5_tools 
import trimesh
import numpy as np

def setup():
    global demo_mesh, hole_volume
    py5.size(500, 500, py5.P3D)
    main_volume = box_mesh(0, 0, 0, 200)
    hole_volume = box_mesh(0, 0, 0, 200)
    apply_rotation(hole_volume, py5.radians(45), direction=(0, 0, 1))
    apply_rotation(hole_volume, py5.radians(45), direction=(0, 1, 0))
    demo_mesh = main_volume.difference(hole_volume)
    # Export animation, skip empty frame 0 created on setup
#     py5_tools.animated_gif('demo_mesh.gif', duration=0.08,
#                            frame_numbers=range(1, 361, 5)) 

def draw():
    py5.background(200, 0, 200)
    py5.lights()
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_x(py5.PI / 8)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.stroke_weight(2)
    py5.fill(0, 200, 200)
    py5.stroke(0)
    draw_mesh(demo_mesh)
    if py5.is_key_pressed:
        py5.scale(1.01)
        py5.no_fill()
        py5.stroke(255)
        draw_mesh(hole_volume)
    
def box_mesh(x, y, z, w, h=None, d=None):
    h = h or w
    d = d or h
    mesh = trimesh.creation.box((w, h, d))
    mesh.apply_translation((x, y, z))
    return mesh
    
def apply_rotation(mesh, angle, direction=[1, 0, 0], center=[0, 0, 0]):
    rot_matrix = trimesh.transformations.rotation_matrix(angle, direction, center)
    mesh.apply_transform(rot_matrix)
    
def draw_mesh(mesh, tol=py5.EPSILON):
    vs = mesh.vertices
    py5.push_style()  # To be able to get the stroke settings back
    py5.no_stroke()   # Turn off strokes, to draw without edges
    # Draw triangulated faces without edges
    with py5.begin_closed_shape(py5.TRIANGLES):
        py5.vertices(vs[np.concatenate(mesh.faces)])
    py5.pop_style() # Get previous stroke settings
    # Draw only edges
    coplanar_edges = mesh.face_adjacency_edges[mesh.face_adjacency_angles < tol]
    mask = ~np.any(np.all(coplanar_edges[:, None] == mesh.edges_unique, axis=2), axis=0)
    a, b = np.vstack(mesh.edges_unique[mask]).T
    py5.lines(np.column_stack((vs[a], vs[b])))
#    a, b = np.vstack(mesh.facets_boundary).T
#    py5.lines(np.column_stack((vs[a], vs[b])))

py5.run_sketch(block=False)
