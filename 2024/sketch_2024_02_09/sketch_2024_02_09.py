import functools

import py5
from shapely import Polygon, MultiPolygon
import trimesh

from villares.shapely_helpers import polys_from_text, draw_shapely_objs

pontos = [
    (100, 100),
    (300, 100),
    (300, 300),
    (150, 250),
    ]

quadradinho = [
    (150, 150),
    (200, 150),
    (200, 200),
    (150, 200)
    ]

def setup():
    global polys, st
    py5.size(800, 400, py5.P3D)
    py5.no_stroke()
    py5.lights()
    py5.translate(50, 50)
    py5.rotate_x(py5.radians(30))
    py5.scale(0.6)
    
    p = Polygon(pontos)
    q = Polygon(quadradinho)
    pb = p.buffer(50)
    pd = pb.difference(q)
    tri = trimesh.creation.extrude_polygon(pd, 20)
    pt = convert_obj(tri)
    py5.fill(240)
    py5.shape(pt, 0, 0)

    f = py5.create_font('Tomorrow Regular', 100)
    py5.text_font(f)
    texto = 'Hello shapely!\nHello trimesh!'
    polys = MultiPolygon(polys_from_text(texto, f))
    py5.translate(200, 300, 20)
    py5.fill(0, 0, 200)
    st = polys.buffer(3)
    for el in st.geoms:
        tri = trimesh.creation.extrude_polygon(el, 20)
        est = convert_obj(tri)
        py5.shape(est, 0, 0)    
    py5.save(__file__[:-2] + 'png')

    
@functools.cache
def convert_obj(obj):
   return py5.convert_shape(obj)

py5.run_sketch(block=False)