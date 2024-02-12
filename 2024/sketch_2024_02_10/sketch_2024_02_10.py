import functools

import py5
from shapely import Polygon, MultiPolygon
import trimesh # install manifold3d

from villares.shapely_helpers import polys_from_text

def setup():
    py5.size(800, 400, py5.P3D)
    py5.no_stroke()

    global meshes
    f = py5.create_font('Tomorrow Regular', 100)
    py5.text_font(f)
    texto = '     take a box\n     subtract a cylinder'
    meshes = [
        trimesh.creation.extrude_polygon(poly.buffer(3), 20)
        for poly in MultiPolygon(polys_from_text(texto, f)).geoms
        ]

    tri = xyz_box(0, 0, 0, 100)
    hole = trimesh.creation.cylinder(30, 120)
    meshes.append(tri.difference(hole))

    
def draw():
    py5.background(240)
    py5.lights()
    py5.translate(300, 200)
    py5.rotate_x(py5.radians(py5.mouse_y))
    py5.scale(0.6)
    

    py5.translate(-200, 0, 20)
    py5.fill(0, 0, 200)
    for mesh in meshes:
        pshape = convert_obj(mesh)
        py5.shape(pshape, 0, 0)    

def key_pressed():
    py5.save(__file__[:-2] + 'png')

def xyz_box(x, y, z, w, h=None, d=None):
    h = w or h
    d = d or h
    c = trimesh.creation.box((w, h, d))
    c.apply_translation((x, y, z))
    return c
    
@functools.cache
def convert_obj(obj):
   return py5.convert_shape(obj)

py5.run_sketch(block=False)