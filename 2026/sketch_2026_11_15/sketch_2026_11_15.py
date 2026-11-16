# !pip install trimesh[easy]
# !pip install manifold3D

import py5
import numpy as np
import trimesh
import shapely
from py5_tools import animated_gif 

def setup():
    global shp
    py5.size(600, 600, py5.P3D)
    ico = trimesh.creation.icosphere(subdivisions=2 , radius=240.0)
    edge_idx = ico.edges_unique          # (30, 2) vertex index pairs
    edges = ico.vertices[edge_idx]    # (30, 2, 3) start and end coordinates
    a, b = edges[0]    
    #section = shapely.Polygon(((0, 0), (0, 10), (10, 10), (10, 0)))
    #section = shapely.affinity.translate(section, -section.centroid.x, -section.centroid.y)
    section = shapely.Point(0, 0).buffer(4, quad_segs=2)
    struts = []
    for a, b in edges:
        edge_len = np.linalg.norm(b - a)
        prism = trimesh.creation.extrude_polygon(section, edge_len)
        align_mesh_to_seg(prism, a, b)
        struts.append(prism)
    #mesh = trimesh.util.concatenate(struts)
    mesh = trimesh.boolean.union(struts, engine="manifold")
    shp = py5.convert_cached_shape(mesh)
    animated_gif('out.gif', frame_numbers=range(1, 181, 4), duration=0.1)
        
def draw():
    py5.background(0, 0, 100)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rotate_y(py5.radians(py5.frame_count))
    py5.shape(shp)

def align_mesh_to_seg(mesh, a, b):
    seg = b - a
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


