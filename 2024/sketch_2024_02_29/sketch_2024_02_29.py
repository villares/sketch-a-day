from functools import lru_cache
import itertools

from shapely import (
    LineString,
    GeometryCollection,
    MultiPolygon,
    Polygon,
    )

import trimesh
import py5

elements = []
vers = []
plate = Polygon(
    [(20, 20), (480, 20), (480, 480), (20, 480)]
    )

def setup():
    py5.size(500, 500, py5.P3D)
    
def draw():
    global plate
    py5.background(200)
    if elements:
        gc = GeometryCollection(elements)
        mp = gc.buffer(10)
        plate = plate.difference(mp)
        if not isinstance(plate, MultiPolygon):
            plate = MultiPolygon([plate])
        for p in plate.geoms:
            s = trimesh.creation.extrude_polygon(p, 10)
            py5.fill(255, 128)
            py5.no_stroke()
            draw_obj(s)
            py5.no_fill()
            py5.stroke(0)
            draw_edges(s)
        
    if len(vers) > 1:
        draw_obj(LineString(vers).buffer(10))


def draw_edges(m):
    vs = m.vertices
    bs = m.facets_boundary
    for facet in bs:
        with py5.begin_shape(py5.LINES):
            py5.vertices(vs[v] for v in itertools.chain(*facet))

def mouse_pressed():
    vers.append((py5.mouse_x, py5.mouse_y))


def mouse_dragged():
    m = py5.mouse_x, py5.mouse_y
    d = py5.dist(*vers[-1], *m)
    if d >= 50:
        vers.append(m)
        
def mouse_released():
    if len(vers) > 1:
        elements.append(LineString(vers))
    vers.clear()


def draw_obj(obj):
    ps = convert_obj(obj)
    ps.disable_style()
    py5.shape(ps, 0, 0)

@lru_cache(maxsize=10)
def convert_obj(obj):
    return py5.convert_shape(obj)

def key_pressed():
    py5.save_frame(__file__[:-3] + '.png')

py5.run_sketch(block=False)

