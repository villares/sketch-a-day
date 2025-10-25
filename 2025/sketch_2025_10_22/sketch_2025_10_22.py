import py5
import shapely
from shapely import MultiPolygon, MultiPoint, Polygon

pts = [
    (py5.mouse_x, py5.mouse_y),
    (200, 250),
    (200, 200),
    (250, 250),
    (230, 230),
    (230, 280),
    (230, 230),
    (180, 280),
]

def setup():
    global W
    py5.size(500, 500)
    py5.color_mode(py5.CMAP, 'viridis', 300)
    W = py5.width 

def draw():
    py5.background('k')

    polygons = shapely.voronoi_polygons(MultiPoint(pts), extend_to=shapely.Polygon(((0, 0), (W, 0), (W, W), (0, W))))
#    polygons = shapely.voronoi_polygons(pts) #, extend_to=BOUNDARY)
    max_area = max(shp.area for shp in polygons.geoms)
    py5.no_stroke()
    for shp in polygons.geoms:
        area = shp.area
        py5.fill(area / max_area * 255)
        py5.shape(shp.buffer(-3).buffer(3))
    
    py5.stroke_weight(3)
    py5.stroke('red')
    py5.points(pts)

def key_pressed():
    py5.save_frame('####.png')
    pts[:] = ((py5.random_int(W), py5.random_int(W)) for _ in range(20))


py5.run_sketch()
    
