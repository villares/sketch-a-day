from itertools import combinations, product
from shapely import Point, LineString, Polygon
from shapely import MultiPoint, MultiLineString, MultiPolygon
import shapely
import numpy as np

grid = []
margin = 0
step = 300

def setup():
    global paths, union, mp
    size(900, 900)
    w, h = width, height
    pts = list(product(range(margin, w + 1, step), repeat=2))
    combos = combinations(pts, 2)
    pairs = [((a, b), (c, d)) for ((a, b), (c, d)) in combos
             if dist(a, b, c, d) < step * 3]
    3print(pairs)
    paths = [LineString(combo).buffer(7) for combo in pairs]
    #paths = [Polygon(bar_points(a, b, c, d, 10, o=10)) for (a, b), (c, d) in combos]    
    union = shapely.unary_union(paths)
    
    R = np.linspace(0, 255, w).reshape(1, -1)
    G = np.linspace(0, 255, h).reshape(-1, 1)
    B = np.random.uniform(128, 255, (h, w))
    A = np.array([[128 + dist(w /2, h / 2, x, y) % 128
                   for x in range(w)]
                   for y in range(h)])
    rgba = np.dstack(np.broadcast_arrays(R, G, B, A))
    img = create_image_from_numpy(rgba, 'RGBA');    
    image(img, 0, 0)
    fill(255)
    stroke_weight(2)
    draw_shapely(union)
    save('out.png')

def draw_shapely(shp):
    if isinstance(shp, MultiPolygon):
        for p in shp.geoms:
            draw_shp(p)
    elif isinstance(shp, Polygon):
        begin_shape()
        for x, y in shp.exterior.coords:
            vertex(x, y)
        for hole in shp.interiors:
            begin_contour()
            for x, y in hole.coords:
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
        
def bar_points(p1x, p1y, p2x, p2y, w1, w2=None, o=0):
    """
    trapezoid, draws a rotated quad with axis
    starting at (p1x, p1y) ending at (p2x, p2y) where
    w1 and w2 are the starting and ending side widths.
    """
    if w2 is None:
        w2 = w1
    d = dist(p1x, p1y, p2x, p2y)
    angle = atan2(p1x - p2x, p2y - p1y) + HALF_PI
    unrotated_points = (
        (p1x - o, p1y - w1 / 2),
        (p1x - o, p1y + w1 / 2),
        (p1x + d + o, p1y + w2 / 2),
        (p1x + d + o, p1y - w2 / 2)
    )
    return [rot(pt, angle, center=(p1x, p1y))
            for pt in unrotated_points]


def rot(pt, angle, center=None):
    xp, yp = pt
    x0, y0 = center or (0, 0)
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)