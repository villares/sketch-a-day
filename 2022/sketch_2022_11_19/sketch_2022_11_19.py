# Using py5coding.org (Processing + Python) and shapely
# you'll need to install py5 and shapely

from shapely.geometry import Polygon, MultiPolygon
from shapely.geos import TopologicalError
from shapely.ops import unary_union

stars = []
solid = []
holes = []

def setup():
    global mh, mv
    size(1000, 500)
    mh, mv = width / 2, height / 2
    for _ in range(10):
        x, y = random(100, width-100), random(100, height-100)
        solid.append(big_star(x, y))
        holes.append(small_star(x, y))
        stars.append(s_star(x, y))
    no_stroke()


def draw():
    background(128, 128, 255) 
    fill(255)
    result = unary_union(solid)
    result = result.difference(unary_union(holes))
    draw_elements(result)
    fill(255, 0, 255, 32)
    inters = []
    for star in stars:
        for other in stars:
            if star is not other:
                r = star.intersection(other)
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
    elif isinstance(element, list):
        for p in element:
            draw_elements(p)
    else:  # legacy code tuple/points
        with begin_closed_shape():
            vertices(element)
        
def s_star(x, y):
    return Polygon(star_pts(x, y, 100, 50, 12),
          holes=[star_pts(x, y, 75, 35, 12)])

def small_star(x, y):
    return Polygon(star_pts(x, y, 75, 35, 12))

def big_star(x, y):
    return Polygon(star_pts(x, y, 100, 50, 12))
                   

def star_pts(cx, cy, ra, rb, n, **kwargs):
    passo = TWO_PI / n
    pts = []
    for i in range(n):  # enquanto o ângulo for menor que 2 * PI:
        ang = passo * i
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        bx = cx + cos(ang + passo / 2.) * rb
        by = cy + sin(ang + passo / 2.) * rb
        pts.append((ax, ay))
        pts.append((bx, by))
    return pts    

