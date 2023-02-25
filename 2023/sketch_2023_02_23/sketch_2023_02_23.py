"""
Editor de máscaras - Sesc Av. Paulista

a - Engrossa forma sob o mouse
s - Salva SVG
p - Salva estado do projeto (pickle dump)
r - Restaura estado do projeto (pickle load)
m - espelhamento (mirror)

TODO:
Interface para escolher os glifos
Acrescentar mais formas
Duplicar formas
Remover formas
Exportar STL (com trimesh)
melhorar UND
""" 

import py5

from shapely.geometry import Polygon, MultiPolygon, GeometryCollection, LineString, Point
from shapely.ops import unary_union
from shapely.affinity import translate as shapely_translate
from shapely.affinity import rotate as shapely_rotate
from shapely.affinity import scale as shapely_scale

from shapely_helpers import *

mouse_over = -1
mirror = True
export_svg = False
shift_pressed = False
ctrl_pressed = False

union = side_union = []
shapes = []
previous_shapes = []

initial_glyphs = 'ab cd\nAB CD'
extra_glyphs = '\n'.join('ERTYerty')
drawer = False

def setup():
    global n_font, extra_shapes
    py5.size(1000, 600)

    n_font = py5.create_font('Nymphette.ttf', 100)
    
    shapes.extend(polys_from_text(initial_glyphs, n_font))
    previous_shapes[:] = shapes[:]
    
    extra_shapes = polys_from_text(extra_glyphs, n_font)
 
    
def draw():
    global union, export_svg
    #py5.window_title(str(py5.get_frame_rate()))
    py5.background(100)
    py5.translate(100, 100)
    py5.fill(255, 100)
    try:
        side_union = union = unary_union(shapes)
        if mirror:
            union = unary_union((union, shapely_scale(side_union, -1, 1, 1, origin='center')))
    except Exception as e:
        print(e)

    if export_svg:
        output = py5.create_graphics(py5.width, py5.height, py5.SVG,
                                     f'mascara-{py5.frame_count}.svg')
        py5.begin_record(output)
    py5.stroke(0)
    draw_shapely_objs(union)
    
    if export_svg:
        py5.end_record()
        export_svg = False
    
    if py5.is_mouse_pressed:
        py5.fill(255, 255, 100, 100)
        draw_shapely_objs(side_union)
             
    for i, shp in enumerate(shapes):
        py5.fill(255, 100, 100, 100)
        if i == mouse_over:
            draw_shapely_objs(shp)

    if drawer:
        py5.translate(600, 0)
        draw_shapely_objs(extra_shapes)
  
def key_pressed():
    global export_svg, mirror
    global shift_pressed, ctrl_pressed
    global drawer
    if mouse_over >= 0:
        if py5.key == 'a':
            save_for_undo()
            shapes[mouse_over] = shapes[mouse_over].buffer(2)
    elif py5.key == 'd':
        drawer = not drawer
    elif py5.key == 's':
        export_svg = True
    elif py5.key == 'm':
        mirror = not mirror
    elif py5.key == 'p':
        py5.save_pickle(shapes, 'mascaras.data')
    elif py5.key == 'r':
        shapes[:] = py5.load_pickle('mascaras.data')
    elif py5.key_code == py5.SHIFT:
        shift_pressed = True
    elif py5.key_code == py5.CONTROL:
        ctrl_pressed = True
        print('Control pressed')
    elif py5.key_code == 90 and ctrl_pressed:
        print('desfazer')
        undo()
    # print(py5.key, py5.key_code) # debug
    
def undo():
    global shapes, previous_shapes
    previous_shapes, shapes = shapes, previous_shapes

def save_for_undo():
    previous_shapes[:] = shapes[:]

def key_released():
    global shift_pressed, ctrl_pressed
    if py5.key_code == py5.SHIFT:
        shift_pressed = False
    elif py5.key_code == py5.CONTROL:
        ctrl_pressed = False

def mouse_moved():
    global mouse_over
    if not py5.is_mouse_pressed:
        for i, shp in enumerate(shapes):
            if shp.contains(Point(py5.mouse_x - 100, py5.mouse_y - 100)):
                mouse_over = i
                break
        else:
            mouse_over = -1

def mouse_dragged():
    if mouse_over >= 0:
        dx = py5.mouse_x - py5.pmouse_x
        dy = py5.mouse_y - py5.pmouse_y
        shapes[mouse_over] = shapely_translate(shapes[mouse_over], xoff=dx, yoff=dy) 

def mouse_wheel(e):
    if mouse_over >= 0:
        if shift_pressed:
            f = 1 + e.get_count() / 5
            shapes[mouse_over] = shapely_scale(shapes[mouse_over],f ,f, origin='center')
        else:
            shapes[mouse_over] = shapely_rotate(shapes[mouse_over],
                                             e.get_count(), origin='center')

py5.run_sketch()

