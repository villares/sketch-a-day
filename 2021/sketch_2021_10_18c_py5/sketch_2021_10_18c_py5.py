import py5
from math import atan2, pi, sin, cos, dist
from itertools import chain
from shapely.geometry import *
from shapely.ops import unary_union

tris = [
    ((10, 0), (0, 10), (10, 10)),
    ( (20, 10),(10, 20), (20, 20)),
    ]

#tris = []
unvisited_tris = tris[:]

def setup():
    py5.size(600, 600)


def draw():
    py5.background(240, 240, 220)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(0, 64)
    py5.fill(50, 150, 150, 100)
    for t in tris:
        py5.begin_shape()
        for x, y in t:
            py5.vertex(x, y)
        py5.end_shape(py5.CLOSE)
    for u in unvisited_tris:
        py5.begin_shape()
        for x, y in u:
            py5.vertex(x, y)
        py5.end_shape(py5.CLOSE)


def mouse_dragged():
    ox, oy = py5.width / 2, py5.height / 2
    drag = ((py5.mouse_x - ox, py5.mouse_y - oy),
            (py5.pmouse_x - ox, py5.pmouse_y - oy))
    unvisited_tris.append(drag)


def key_pressed():
    
    global union
    triangles = GeometryCollection(list(map(Polygon, tris)))
    union = unary_union(triangles)
    unvisited = unvisited_tris[:]
    unvisited_tris[:] = []
#for t in unvisited:
#        grow(t)
    list(map(grow, unvisited))
# my in point
#     loop          10   32877669.0 3287766.9    100.0      grow_all()
#     map           10   30474387.0 3047438.7    100.0      grow_all()
# shapely           10   14608306.0 1460830.6    100.0      grow_all()
# shapely & changes 10   53051177.0 5305117.7    100.0      grow_all()
#                   10   18337830.0 1833783.0     80.8      list(map(grow, unvisited))
# todo: vectorize

def grow(t):
    edges = get_edges(t)
    for e in edges:
        e0, e1 = e[0], e[1]
        a = edge_angle(e)
        m = midpoint(e)
        d = edge_dist(e) * 0.87
        p = point_offset(m, d, a - pi / 2)
        pp = Point(*p)
        if not pp.within(union):
#        if not point_in_tris(p):
            n = (e0, p, e1)
            tris.append(n)
            unvisited_tris.append(n)

def mouse_pressed():
    if py5.mouse_button == py5.RIGHT:
        py5.print_line_profiler_stats()

# def grow(t):
#     edges = get_edges(t)
#     new_tris = []
#     for e in edges:
#         e0, e1 = e[0], e[1]
#         a = edge_angle(e)
#         m = midpoint(e)
#         d = edge_dist(e) * 0.87
#         p = point_offset(m, d, a - pi / 2)
#         if not point_in_tris(p):
#             n = (e0, p, e1)
#             new_tris.append(n)
#     return new_tris

def get_edges(t):
    t0 = t[0]
    return [
        ((xa, ya), (xb, yb)) for (xa, ya), (xb, yb) in zip(t, t[1:] + (t0,))
    ]


def edge_angle(edge):
    (xa, ya), (xb, yb) = edge
    return atan2(yb - ya, xb - xa) + pi


def point_offset(p, offset, angle):
    return (int(p[0] + offset * cos(angle)), int(p[1] + offset * sin(angle)))


def point_in_tris(p):
#    p_in_t = lambda t: point_inside_tri(p, t)
    p_in_t = lambda t: point_inside_poly(p, t)
    return any(map(p_in_t, tris))

def s(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def point_inside_tri(pt, tri):
    v1, v2, v3 = tri
    d1 = s(pt, v1, v2);
    d2 = s(pt, v2, v3);
    d3 = s(pt, v3, v1);
    neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (pos and neg)

def point_inside_poly(p, vertices):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    x, y = p
    inside = False
    for i, v in enumerate(vertices):
        pv = vertices[i - 1]
        xi, yi = v
        xj, yj = pv
        intersect = ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside


def edge_dist(edge):
    return dist(*edge) # math.dist 


def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0

py5.profile_functions(['key_pressed'])
py5.run_sketch()
