import py5
from py5_tools import animated_gif

from shapely import Polygon, LineString

from villares.geometry_helpers import Line, lerp_tuple, rotate_point, rect_points

pts = [(100, 100), (300, 200), (400, 100), (300, 400), (150, 300)]
hole = [ (250, 200), (200, 200), (200, 250),  (250, 250)]

def setup():
    py5.size(512, 512)
    py5.color_mode(py5.HSB)
    #animated_gif('out.gif', duration=0.2, frame_numbers=range(1, 361, 5))

def draw():
    py5.background(240)
    py5.fill(255, 100)
    py5.stroke(0, 0, 200)
    #draw_poly(pts, [hole])
    py5.no_fill()
    ang = py5.radians(py5.frame_count)
    py5.stroke(200, 0, 0)
    #hatch_poly(pts, [hole], 10, py5.PI/4)
    lis = par_hatch(pts, 30, 1, 2, 3)
    for li in lis:
        li.draw()

def hatch_poly(pts, holes=[], spacing=5, angle=0):
    p = Polygon(pts, [hole])
    min_x, min_y, max_x, max_y = p.bounds
    w = max_x - min_x
    h = max_y - min_y
    n = int(w / spacing * 0.7)
    cx, cy = p.centroid.x, p.centroid.y 
    for i in range(-n, n+1):
        x = cx + i * spacing
        py5.line(x, cy - h * 0.7, x , cy + h * 0.7);
    py5.fill(255, 150)
    py5.shape(py5.convert_cached_shape(p))

def par_hatch(points, divisions, *sides):
    # points = [(p[0], p[1]) for p in points]
    lines = []
    if not sides:
        sides = [0]
    for s in sides:
        a, b = points[-1 + s], points[+0 + s]
        d, c = points[-2 + s], points[-3 + s]
        for i in range(1, divisions):
            s0 = lerp_tuple(a, b, i / divisions)
            s1 = lerp_tuple(d, c, i / divisions)
            lines.append(Line(s0, s1))
    return lines

# def draw_poly(exterior, holes=[]):
#     with py5.begin_closed_shape():
#         py5.vertices(pts)
#         for hole in holes:
#             with py5.begin_contour():
#                 py5.vertices(hole)
def key_pressed():
    py5.save('out.png')

py5.run_sketch(block=False)

