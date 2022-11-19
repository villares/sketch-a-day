# Using py5coding.org (Processing + Python) and shapely
# you'll need to install py5 and shapely

from shapely.geometry import Polygon, MultiPolygon
from shapely.geos import TopologicalError
#from shapely import intersection_all
from shapely.ops import unary_union

stars = []

save_pdf = False   # Use "p" to save a PDF
mirror = True      # Use "m" to toggle
# press <backspace> to remove last segment/click


def setup():
    global mh, mv
    size(1000, 500)
    mh, mv = width / 2, height / 2
    for _ in range(10):
        stars.append(s_star(random(100, width-100), random(100, height-100)))

def draw():
    background(128, 128, 255)  # it's better to leave the background out!
    if len(stars) > 1:
        fill(255)
        result = unary_union(stars)
        draw_polys(result)
        fill(255, 0, 255)
        inters = []
        for star in stars:
            for other in stars:
                if star is not other:
                    r = star.intersection(other)
                    if r:
                        inters.append(r)
        draw_polys(inters)

def draw_polys(poly):
    if isinstance(poly, MultiPolygon):
        for p in poly.geoms:
            draw_polys(p)
    elif isinstance(poly, list):
        for p in poly:
            draw_polys(p)
    elif isinstance(poly, Polygon):
        begin_shape()
        for x, y in poly.exterior.coords:
            vertex(x, y)
        for hole in poly.interiors:
            begin_contour()
            for x, y in hole.coords:
                vertex(x, y)
            end_contour()
        end_shape(CLOSE)
    else:
        begin_shape()
        for x, y in poly:
            vertex(x, y)
        end_shape(CLOSE)
        
def s_star(x, y):
    return Polygon(star_pts(x, y, 100, 50, 12),
          holes=[star_pts(x, y, 75, 35, 12)])
        
                   

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

