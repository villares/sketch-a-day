import py5

from shapely.affinity import translate as shapely_translate
from shapely.affinity import rotate as shapely_rotate

from shapely.geometry import Polygon, MultiPolygon, GeometryCollection, LineString, Point
from shapely.ops import unary_union

from shapely_helpers import *

import trimesh

dragged = -1

def setup():
    global shapes
    py5.size(1200, 400, py5.P3D)
    py5.color_mode(py5.HSB)

    font = py5.create_font('D050000L', 100)
    shapes = polys_from_text(
        'abcdefghijkl\nABCDEFGHIJK',
        font)

def draw():
    py5.window_title(str(py5.get_frame_rate()))
    py5.background(100)
    py5.translate(100, 100)
    if py5.is_key_pressed:
        py5.rotate_x(py5.PI / 10)
    py5.fill(255, 100)
    for i, shp in enumerate(shapes):
        py5.fill((i * 8) % 256, 255, 255, 100)
        if i == dragged:
            draw_shapely_objs(shp)
    try:
        union = unary_union(shapes)
        if not py5.is_key_pressed:
            draw_shapely_objs(union)
        else:
            for p in union.geoms:
                if isinstance(p, Polygon):
                    m = trimesh.creation.extrude_polygon(p, 10)
                    draw_mesh(m)
    except ValueError:
        print('ValueError')

def mouse_moved():
    global dragged
    if not py5.is_mouse_pressed:
        for i, shp in enumerate(shapes):
            if shp.contains(Point(py5.mouse_x - 100, py5.mouse_y - 100)):
                dragged = i
                break
        else:
            dragged = -1

def mouse_dragged():
    if dragged >= 0:
        dx = py5.mouse_x - py5.pmouse_x
        dy = py5.mouse_y - py5.pmouse_y
        shapes[dragged] = shapely_translate(shapes[dragged], xoff=dx, yoff=dy) 


def mouse_wheel(e):
    if dragged >= 0:
        # hapely.affinity.rotate(geom, angle, origin='center'
        shapes[dragged] = shapely_rotate(shapes[dragged],
                                         e.get_count(), origin='center')
         

def process_glyphs(polys):
    """
    Try to subtract the shapely Polygons representing a glyph
    in order to produce appropriate looking glyphs!
    """
    polys = sorted(polys, key=lambda p: p.area, reverse=True)
    results = [polys[0]]
    for p in polys[1:]:
        # works on edge cases like â and ®
        for i, earlier in enumerate(results):
            if earlier.contains(p):
                results[i] = results[i].difference(p)
                break
        else:   # the for-loop's else only executes after unbroken loops 
            results.append(p)
    return results


      
def draw_mesh(m):
    for i, face in enumerate(m.faces):
        py5.fill((m.vertices[0][0]) % 256, 255, 255)
        with py5.begin_closed_shape():
            py5.vertices([m.vertices[v] for v in face])

py5.run_sketch()
