from functools import lru_cache
import itertools

from shapely import (
    LineString,
    GeometryCollection,
    Polygon,
    MultiPolygon,
    Point,
    MultiPoint,
    )

import trimesh
import py5

elements = []
vers = []
plate = Polygon(
    [(20, 20), (480, 20), (480, 480), (20, 480)]
    )

SPACING = 100
S = 25
SQR2 = py5.sqrt(2)

grid = list(itertools.product(range(SPACING, 500, SPACING), repeat=2))
grid += [(x + SPACING / 2, y + SPACING / 2) for x, y in grid if x < 400 and y < 400]
half_grid = list(itertools.product(range(SPACING, 500 - SPACING // 2, SPACING // 2), repeat=2))    
    

def setup():
    py5.size(500, 500, py5.P3D)
    py5.pixel_density(2)
    
def draw():
    global mesh
    py5.background(0, 0, 200)
    py5.translate(0, py5.height / 2)
    if not py5.is_mouse_pressed or py5.is_key_pressed:
        py5.rotate_x(py5.radians(30))
    py5.translate(0, -py5.height / 1.5)

    if elements:
        gc = GeometryCollection(elements)
        mp = gc.buffer(4)
        plate_with_holes = plate.difference(mp)
        if not isinstance(plate_with_holes, MultiPolygon):
            plate_with_holes = MultiPolygon([plate_with_holes])
        mesh = trimesh.util.concatenate([
            trimesh.creation.extrude_polygon(p, 5)
            for p in plate_with_holes.geoms]) 
        py5.fill(255)
        py5.no_stroke()
        draw_obj(mesh)
        py5.no_fill()
        py5.stroke(0)
        py5.stroke_weight(0.5)
        draw_edges(mesh)
        
    if len(vers) > 1:
        draw_obj(LineString(vers).buffer(4))


def draw_edges(m):
    vs = m.vertices
    bs = m.facets_boundary
    for facet in bs:
        with py5.begin_shape(py5.LINES):
            py5.vertices(vs[v] for v in itertools.chain(*facet))

def mouse_pressed():
    gp = closer_grid(py5.mouse_x, py5.mouse_y)
    print(gp)
    vers.append(gp)

def closer_grid(mx, my):
    min_pos = None
    md = 1000
    for x, y in grid:
        d = py5.dist(x, y, mx, my)
        #print(x, y, mx, my, md, d)
        if d < md:
            md = d
            min_pos = x, y
    return min_pos

def mouse_dragged():
    gp = closer_grid(py5.mouse_x, py5.mouse_y)
    if vers[-1] != gp:
        vers.append(gp)
        
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
    if py5.key == 'p':
        py5.save_frame(__file__[:-3] + '.png')
    elif py5.key == ' ':
        elements.clear()
    elif py5.key == 'd' and elements:
        elements.pop()
    elif py5.key == 's':
        mesh.export('teste.stl')
        print('stl salvo')
    elif py5.key == 'R':
        for x, y in grid:
            for xo, yo in ((S, 0),
                           (S / SQR2, S / SQR2),
                           (S / SQR2, -S / SQR2),
                           (0, S)):        
                elements.append(LineString([(x + xo, y + yo), (x - xo, y -yo)]))
    elif py5.key == 'r':
        elements.append(MultiPoint([(x, y) for x, y in half_grid]))


py5.run_sketch(block=False)

