# Using py5coding.org (Processing + Python) and shapely
# you'll need to install py5 and shapely

from shapely.geometry import Polygon, MultiPolygon
from shapely.geos import TopologicalError
from shapely.ops import unary_union

circles = []
solid = []
holes = []

def setup():
    global mh, mv
    size(1000, 500)
    mh, mv = width / 2, height / 2
    for _ in range(50):
        x, y = random(100, width-100), random(100, height-100)
        solid.append(big_circle(x, y))
        holes.append(small_circle(x, y))
        circles.append(ring(x, y))
    no_stroke()


def draw():
    background(0, 64, 128) 
    fill(255)
    result = unary_union(solid)
    result = result.difference(unary_union(holes))
    draw_elements(result)
    fill(255, 0, 255, 32)
    inters = []
    for c in circles:
        for other in circles:
            if c is not other:
                r = c.intersection(other)
                if r:
                    inters.append(r)
    draw_elements(inters)

def draw_elements(element):
    if isinstance(element, MultiPolygon):
        for p in element.geoms:
            draw_elements(p)
    elif isinstance(element, Polygon):
        with begin_closed_shape():
            vertices(element.exterior.coords)
            for hole in element.interiors:
                with begin_contour():
                    vertices(hole.coords)        
    elif isinstance(element, (list, tuple)):
        for p in element:
            draw_elements(p)
    else:  # legacy code tuple/points
        with begin_closed_shape():
            vertices(element)
        
def ring(x, y):
    return Polygon(circle_pts(x, y, 100),
          holes=[circle_pts(x, y, 75)])

def small_circle(x, y):
    return Polygon(circle_pts(x, y, 75))

def big_circle(x, y):
    return Polygon(circle_pts(x, y, 100))
                   

def circle_pts(cx, cy, d, n=24, **kwargs):
    passo = TWO_PI / n
    pts = []
    for i in range(n):  # enquanto o ângulo for menor que 2 * PI:
        ang = passo * i
        ax = cx + cos(ang) * d / 2
        ay = cy + sin(ang) * d / 2
        pts.append((ax, ay))

    return pts    


