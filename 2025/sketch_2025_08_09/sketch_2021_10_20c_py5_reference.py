# sketch_2021_10_20c_py5

import py5
from math import atan2, pi, sin, cos, dist
from itertools import chain
from shapely.geometry import *
from shapely.ops import unary_union

import numpy as np

Vertex = np.dtype([('x','f4'), ('y','f4')])
Edge = np.dtype([('va', Vertex), ('vb',Vertex)])
Triangle = np.dtype([('va', Vertex), ('vb', Vertex), ('vc', Vertex)])

tris = [
    ((10, 0), (0, 10), (10, 10)),
    ((20, 10), (10, 20), (20, 20)),
    ]

unvisited_tris = tris[:]
edges_drag = []

def setup():
    py5.size(600, 600)
    print(min_max(tris[1]))


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
#     for e in edges_drag:
#         (xa, ya), (xb, yb) = e
#         py5.line(xa, ya, xb, yb)


def mouse_dragged():
    ox, oy = py5.width / 2, py5.height / 2
    mt = (py5.mouse_x - ox, py5.mouse_y - oy) 
    pmt =(py5.pmouse_x - ox, py5.pmouse_y - oy) 
    if mt != pmt:
        edges_drag.append((pmt, mt))

def mouse_released():
    if edges_drag:
        temp = unvisited_tris[:]
        unvisited_tris[:] = []
        for e in edges_drag:
            process_edge(e)
            process_edge(e[::-1])
        tris.extend(unvisited_tris)
        unvisited_tris[:] = temp + unvisited_tris
        edges_drag[:] = []
 
 
# my in point
#     loop          10   32877669.0 3287766.9    100.0      grow_all()
#     map           10   30474387.0 3047438.7    100.0      grow_all()
# shapely           10   14608306.0 1460830.6    100.0      grow_all()
# shapely & changes 10   53051177.0 5305117.7    100.0      grow_all()
#                   10   18337830.0 1833783.0     80.8      list(map(grow, unvisited))
# todo: vectorize
#vv        63        10     959033.0  95903.3     99.9      grow(nptris)
# removes edge vectorization
#       73          10   43257670.0 4325767.0    100.0      grow(nptris)
#         72        10   89445396.0 8944539.6    100.0      grow(nptris)


def key_pressed():
    print(len(unvisited_tris), len(tris))
    unvisited = unvisited_tris[:]
    unvisited_tris[:] = [] 
    nptris = np.array(unvisited, dtype=Triangle)
    grow(nptris)
    tris.extend(unvisited_tris)

@np.vectorize
def grow(t):
    (xa, ya), (xb, yb), (xc, yc) = t
    for edge in (((xa, ya), (xb, yb)),
                 ((xb, yb), (xc, yc)),
                 ((xc, yc), (xa, ya))):
        process_edge(edge)
        
def process_edge(e):
    e0, e1 = e
    a = edge_angle(e)
    m = midpoint(e)
    d = edge_dist(e) * 0.87
    p = point_offset(m, d, a - pi / 2)
    if not point_in_tris(p):
        #n = np.array((e0, p, e1), dtype=Triangle)
        n = (e0, p, e1)
        unvisited_tris.append(n)

def mouse_pressed():
    if py5.mouse_button == py5.RIGHT:
        py5.print_line_profiler_stats()


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
#    p_in_t = lambda t: point_inside_poly(p, t)
    return any(map(lambda t: point_inside_tri(p, t), tris))

def s(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def point_inside_tri(pt, tri):
    x, y = pt
    (x_min, y_min), (x_max, y_max) = min_max(tri)
    if not (x_min <= x <= x_max and y_min <= y <= y_max):
        #print(pt, (x_min, y_min), (x_max, y_max))
        return False    
    v1, v2, v3 = tri
    d1 = s(pt, v1, v2);
    d2 = s(pt, v2, v3);
    d3 = s(pt, v3, v1);
    neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (pos and neg)


def edge_dist(edge):
    return dist(*edge) # math.dist 

def min_max(points):
    coords = tuple(zip(*points))
    return tuple(map(min, coords)), tuple(map(max, coords))

def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0

py5.profile_functions(['key_pressed'])
py5.run_sketch(block=False)