from itertools import combinations
from functools import cache
import pickle

from shapely import Point, LineString
import py5

elements = []
S = 5
W = 50

def setup():
    py5.size(800, 800)
    grid = [
        (x, y)
        for x in range(W, 800, W)
        for y in range(W, 800, W)
        ] 
    elements.extend(
        [Point((x, y)).buffer(S), False]
        for x, y in grid
        )            
    elements.extend(
        [LineString((a, b)).buffer(S), False]
        for a, b in combinations(grid, 2)
        if py5.dist(*a, *b) < W * 1.5
        )
    
def draw():
    py5.background(240)
    py5.no_fill()
    py5.stroke(255)
    for el, viz in elements:    
        draw_obj(el)
    py5.no_stroke()
    py5.fill(0)
    for el, viz in elements:
        if viz:          
            draw_obj(el)
    py5.no_fill()
    py5.stroke(200, 0, 0)
    for el, viz in elements:
        if mouse_over_shape(py5.mouse_x, py5.mouse_y, el):
            draw_obj(el)
            break
 
def draw_obj(obj):
    shp = convert_obj(obj)
    shp.disable_style()
    py5.shape(shp, 0, 0)


@cache
def mouse_over_shape(mx, my, shp):
    return shp.contains(Point((mx, my)))

@cache
def convert_obj(obj):
    return py5.convert_shape(obj)

def mouse_pressed():
    for el_viz in elements: # [shapely_element, visibility_status]
        if el_viz[0].contains(Point((py5.mouse_x, py5.mouse_y))):
            el_viz[1] = not el_viz[1]
            break

def key_pressed():
    if py5.key == 'd':
        pickle

py5.run_sketch()