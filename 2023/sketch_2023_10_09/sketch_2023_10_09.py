import py5

from shapely.affinity import translate as shapely_translate
from shapely.affinity import rotate as shapely_rotate
from shapely.affinity import scale as shapely_scale
from shapely.geometry import Polygon, MultiPolygon, GeometryCollection, LineString, Point
from shapely.ops import unary_union

import trimesh  # warining, install mapbox_earcut!

from villares.shapely_helpers import *

previous_union = -1
dragged = -1
mirror = True

def setup():
    global shapes
    py5.size(1200, 400, py5.P3D)
    py5.color_mode(py5.HSB)

    font = py5.create_font('Open Sans', 100)
    shapes = polys_from_text(
        'abcdefghijkl\nABCDEFGHIJK',
        font)

def draw():
    py5.lights()
    global current_union, previous_union, meshes
    py5.window_title(str(py5.get_frame_rate()))
    py5.background(100)
    py5.translate(100, 100)
    if py5.is_key_pressed:
        py5.rotate_x(py5.PI / 10)
    py5.fill(255, 100)
    for i, shp in enumerate(shapes):
        py5.fill((i * 8) % 256, 255, 255, 100)
        if i == dragged:
            draw_shapely(shp)
    try:
        side_union = union = unary_union(shapes)
        if mirror:
            union = unary_union((union, shapely_scale(side_union, -1, 1, 1, origin='center')))
        
        current_union = hash(union)
        if not py5.is_key_pressed:
            py5.stroke(0, 100)
            draw_shapely(side_union)
            py5.no_stroke()
            draw_shapely(union)
        else:
            if current_union != previous_union:
                meshes = [trimesh.creation.extrude_polygon(p, 10)
                          for p in union.geoms
                          if isinstance(p, Polygon)]
                previous_union = current_union
            for mesh in meshes:
                draw_mesh(mesh)
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
        if py5.key_code == py5.SHIFT:
            f = 1 + e.get_count() / 5
            shapes[dragged] = shapely_scale(shapes[dragged],f ,f, origin='center')
        else:
            shapes[dragged] = shapely_rotate(shapes[dragged],
                                             e.get_count(), origin='center')

def draw_mesh(m):
    for i, face in enumerate(m.faces):
        py5.fill((m.vertices[0][0]) % 256, 255, 255)
        with py5.begin_closed_shape():
            py5.vertices([m.vertices[v] for v in face])

py5.run_sketch()
