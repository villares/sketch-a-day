import py5
from pathlib import Path
from shapely import Point, Polygon, affinity, LineString, unary_union
import trimesh
import numpy as np

rotate_shape = affinity.rotate
scale_shape = affinity.scale

shapes = []
starting_point = []
n = 6
W = 5
cap_style = 'square'

def setup():
    py5.size(600, 600, py5.P3D)  # drawing size in pixels
    
def draw():
    global final_form
    py5.lights()
    py5.background(100, 150, 150)  # clear the canvas (red)
    forms = []  # used to merge all shapes
    middle = py5.width / 2, py5.height / 2
    py5.rotate_y(py5.radians(30))
    section = Point(0, 0).buffer(20, quad_segs=2)
    for shp in shapes:  # going through all shapes      
        for i in range(n):   
            angle = i * 360 / n
            rshape = rotate_shape(
                    shp,
                    angle,
                    origin=middle
                )
            a, b = rshape.coords
            a = np.array(a + (0,))
            b = np.array(b + (0,))
            edge_len = py5.dist(*a, *b) #n p.linalg.norm(b - a)
            prism = trimesh.creation.extrude_polygon(section, edge_len)
            align_mesh_to_seg(prism, a, b)
            forms.append(prism) # draw  the shape
#             forms.append(scale_shape( # scale used to mirror 
#                 rshape,
#                 xfact=-1,
#                 origin=middle))
    final_form = trimesh.util.concatenate(forms) # merged shapes
    py5.shape(final_form)
    if starting_point:
        ls = LineString([starting_point[0], (py5.mouse_x, py5.mouse_y)])        
        with py5.push_style():
            py5.no_fill()
            py5.shape(ls.buffer(W, cap_style=cap_style))
     
def mouse_pressed():  # when mouse is pressed
    starting_point.append((py5.mouse_x, py5.mouse_y))
    
def mouse_released():  # when mouse is released
    if starting_point:
        # print([starting_point[0], (mouse_x, mouse_y)])
        ls = LineString([starting_point[0], (py5.mouse_x, py5.mouse_y)])        
        shapes.append(ls) #Polygon(ls.buffer(W, cap_style=cap_style)))
    starting_point.clear()
    
def key_pressed():
    global n
    if py5.key == 'c':
        shapes.clear()
    elif py5.key == 'a':
        n = n + 1
    elif py5.key == 'z':
        n = n - 1
    elif py5.key == 's':
        py5.save_frame('out.png')        
        
def align_mesh_to_seg(mesh, a, b):
    seg = np.array(b) - np.array(a)
    seg_len = np.linalg.norm(seg)
    d = seg / seg_len  # normalized segment direction
    align_mesh(mesh, d, a)
    
def align_mesh(mesh, d, translate_to=(0, 0, 0)):
    z = np.array([0.0, 0.0, 1.0])  # assuming an "upright" mesh at the origin
    if np.allclose(d, z):          # if d already aligned
        R = np.eye(4)              # then use the identity matrix
    elif np.allclose(d, -z):       # if aligned but pointing the wrong way
        R = trimesh.transformations.rotation_matrix(np.pi, [1, 0, 0])  # then just turn it arround
    else:
        R = trimesh.geometry.align_vectors(z, d)
    mesh.apply_transform(R)     # rotates around mesh origin
    mesh.apply_translation(translate_to)
 
py5.run_sketch()
