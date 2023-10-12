import py5

from shapely.affinity import translate as shapely_translate
from shapely.affinity import rotate as shapely_rotate
from shapely.affinity import scale as shapely_scale
from shapely.geometry import Polygon, MultiPolygon, LineString
from shapely.ops import unary_union
from shapely import GEOSException

from villares.shapely_helpers import *

previous_union = -1
dragged = -1
mirror = False
xo, yo = 10, 200
def setup():
    global shapes, num_of_lines
    py5.size(600, 400)
    #py5.color_mode(py5.HSB)

    font = py5.create_font('Open Sans Bold', 100)
    shapes = polys_from_text(
        'Processing\n& Python',
        font, alternate_spacing=True)
    pairs = [((x, -200), (x, 200))
             for x in range(0, py5.width, 20)]
    line_strs = [LineString(pair).buffer(3) for pair in pairs]
    rotated_lines = [shapely_rotate(line_str,
                                    py5.random(-5,5),
                                    origin='center')
                     for line_str in line_strs]
    
    num_of_lines = len(line_strs)
    shapes.extend(rotated_lines)
    
def draw():
    global current_union, previous_union, meshes
    py5.background(0, 0, 200)
    py5.translate(xo, yo)
    py5.fill(255, 100)
    try:
        letter_shapes = MultiPolygon(shapes[:-num_of_lines])
        clipping_shapes = MultiPolygon(shapes[-num_of_lines:])
        results = list(letter_shapes.buffer(0)
                       .difference(clipping_shapes.buffer(0))
                       .geoms)
    except GEOSException as e:
        print(str(e))
        results = letter_shapes

    for i, shp in enumerate(shapes):
        if i == dragged:
            draw_shapely(shp)
    try:
        side_union = union = unary_union(results)
        if mirror:
            union = unary_union((union, shapely_scale(side_union, -1, 1, 1, origin='center')))
        py5.stroke(0, 100)
        #draw_shapely(side_union)
        #py5.no_stroke()
        for i, shp in enumerate(union.geoms):
            py5.fill(255) #(i * 8) % 256, 255, 255, 200)
            draw_shapely(shp)        
    except GEOSException as e:
        print(str(e))

def mouse_moved():
    global dragged
    if not py5.is_mouse_pressed:
        for i, shp in enumerate(shapes):
            if shp.contains(Point(py5.mouse_x - xo, py5.mouse_y - yo)):
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
py5.run_sketch()
