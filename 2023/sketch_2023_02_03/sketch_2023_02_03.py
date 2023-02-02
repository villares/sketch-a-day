import trimesh
import shapely

from shapely.geometry import Polygon, MultiPolygon, GeometryCollection, LineString, Point
from shapely.geos import TopologicalError
from shapely.ops import unary_union


from polys_with_holes import process_polys

def setup():
    global m, f
    size(800, 400)
    no_fill()
    stroke(255)
    color_mode(HSB)
    f = create_font('DejaVu Sans', 100)
    
    polygon = shapely.geometry.Polygon([(-100, -100), (0, -100),
                                        (0, 0), (-50, -50), (-100, 0)])
    m = trimesh.creation.extrude_polygon(polygon, 30)

def polys_from_text(words, f=None):
    f = f or create_font('Courier', 100)
    results = []
    x_offset = y_offset = 0
    for c in words:
        if c == '\n':
            y_offset += f.get_size()
            x_offset = 0  # assuming left aligned text...
            continue
        results.append([])
        c_shp = f.get_shape(c, 1)
        vs3 = [c_shp.get_vertex(i) for i in range(c_shp.get_vertex_count())]
        vs = set() 
        for vx, vy, _  in vs3:
            x = vx + x_offset
            y = vy + y_offset
            results[-1].append((x, y))
            if (x, y) not in vs:
                vs.add((x, y))
            else:
                results.append([])
        w = c_shp.get_width() if vs3 else f.get_size() / 3
        x_offset += w
    return [Polygon(p) for p in results if len(p) > 2]
    
def draw():
    background(100)
    translate(100, 100)
    stuff = process_polys(polys_from_text('Oi!\nOlá mundo...', f))
    fill(255, 100)
    draw_elements(stuff)
    
def draw_elements(element):
    if isinstance(element, (MultiPolygon, GeometryCollection)):
        for p in element.geoms:
            draw_elements(p)
    elif isinstance(element, Polygon):
        with begin_closed_shape():
            #if element.exterior.coords:
            vertices(element.exterior.coords)
            for hole in element.interiors:
                with begin_contour():
                    vertices(hole.coords)        
    elif isinstance(element, list):
        for p in element:
            draw_elements(p)
    elif isinstance(element, LineString):
        stroke(255, 0, 0)
        (xa, ya), (xb, yb) = element.coords
        line(xa, ya, xb, yb)
        no_stroke()
    elif isinstance(element, Point):
        with push_style():
            fill(255, 0, 0)
            x, y = element.coords[0]
            circle(x, y, 15)
    else:
        print(element)
