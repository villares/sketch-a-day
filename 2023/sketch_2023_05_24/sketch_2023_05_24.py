from itertools import combinations, product
from shapely import Point, LineString, Polygon
from shapely import MultiPoint, MultiLineString, MultiPolygon
import shapely

grid = []
margin = 100
step = 200

def setup():
    global paths, union, mp
    size(600, 600)
    pts = list(product(range(margin, width, step), repeat=2))
    combos = combinations(pts, 2)
    paths = [LineString(combo) for combo in combos]
    mp = MultiPolygon([path.buffer(10) for path in paths])
    union = shapely.unary_union(mp.geoms[:15])
    
def draw():
    background(200)
    fill(255, 100)
    draw_shapely(mp)
    fill(0, 200, 0, 200)
    draw_shapely(union)
    

def draw_shapely(shp):
    if isinstance(shp, (MultiPolygon, MultiLineString)):
        for p in shp.geoms:
            draw_shapely(p)
    elif isinstance(shp, Polygon):
        begin_shape()
        for x, y in shp.exterior.coords:
            vertex(x, y)
        for hole in shp.interiors:
            begin_contour()
            try:
                for x, y in shp.coords:
                    vertex(x, y)
            except NotImplementedError:
                for x, y in shp.exterior.coords:
                    vertex(x, y)
            end_contour()
        end_shape(CLOSE)
    elif isinstance(shp, LineString):
        with push_style():
            no_fill()
            begin_shape()
            for x, y in shp.coords:
                vertex(x, y)
            end_shape()
    else:
        print(f"não consigo desenhar: {shp}")