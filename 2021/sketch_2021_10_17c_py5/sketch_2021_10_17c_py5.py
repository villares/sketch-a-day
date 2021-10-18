import py5
import numpy as np
from math import atan2, pi, sin, cos
from itertools import chain

tris = []
unvisited_tris = set()


def setup():
    py5.size(600, 600)


def draw():
    py5.background(240, 240, 220)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(0, 64)
    py5.fill(50, 150, 0, 100)
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
    unvisited_tris.add(drag)


def key_pressed():
    global unvisited_tris 
    for t in list(unvisited_tris):
         grow(t)
#     new_tris = map(grow, list(unvisited_tris))
#     print(list(new_tris))
#     unvisited_tris = set(list(new_tris))
#     tris.extend(new_tris)
#     print(len(tris))  # , len(visited_tris)



def mouse_pressed():
    if py5.mouse_button == py5.RIGHT:
        py5.print_line_profiler_stats()

def grow(t):
    edges = get_edges(t)
    unvisited_tris.remove(t)
    for e in edges:
        e0, e1 = e[0], e[1]
        a = edge_angle(e)
        m = midpoint(e)
        d = edge_dist(e) * 0.87
        p = point_offset(m, d, a - pi / 2)
        if not point_in_tris(p):
            n = (e0, p, e1)
            tris.append(n)
            unvisited_tris.add(n)

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
    (xa, ya), (xb, yb) = edge
    return py5.dist(xa, ya, xb, yb)


def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0

py5.profile_functions(['key_pressed'])
py5.run_sketch()
