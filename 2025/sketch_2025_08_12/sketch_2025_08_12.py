import py5
from py5 import atan2, sin, cos

import shapely
from shapely.ops import unary_union

polys = [
  ((0, 0), (0, 30), (30, 30), (30, 0)),
  #  ((20, 10), (10, 20), (20, 20)),
    ]

all_polys = shapely.Polygon()
unvisited_polys = polys[:]

def setup():
    py5.size(600, 600)

def draw():
    py5.background(240, 240, 220)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(0, 64)
    #py5.shape(all_polys)
    #py5.no_stroke()
    py5.fill(50, 150, 100, 150)
    for t in polys:
        py5.begin_shape()
        for x, y in t:
            py5.vertex(x, y)
        py5.end_shape(py5.CLOSE)


def key_pressed():
    global all_polys
    if py5.key == ' ':
        print(len(unvisited_polys), len(polys))
        unvisited = unvisited_polys[:]
        unvisited_polys[:] = [] 
        for t in unvisited:
            grow(t)
        polys.extend(unvisited_polys)
    elif py5.key == 'c':
        all_polys = shapely.Polygon()
        unvisited_polys.clear()
        polys.clear()
    elif py5.key == 's':
        py5.save_frame('###.png')

def grow(p):
    global all_polys
    for edge in zip(p, p[1:] + (p[0],)):
        ea, eb = edge
        ang = edge_angle(edge)
        da = py5.dist(*ea, *eb) * py5.random(0.66, 1)
        pa = point_offset(ea, da, ang - py5.PI / 2)
        db = py5.dist(*ea, *eb) * py5.random(0.66, 1)
        pb = point_offset(eb, db, ang - py5.PI / 2)
        n = (ea, pa, pb, eb)
        t = shapely.Polygon(n)
        #print(t)
        if not all_polys.contains(t):
            #n = np.array((e0, p, e1), dtype=Triangle)
            unvisited_polys.append(n)
            try:
                all_polys = all_polys.union(t)
            except shapely.GEOSException:
                print('GEOSException')

def mouse_pressed():
    if py5.mouse_button == py5.RIGHT:
        py5.print_line_profiler_stats()
     

def edge_angle(edge):
    (xa, ya), (xb, yb) = edge
    return atan2(yb - ya, xb - xa) + py5.PI

def point_offset(p, offset, angle):
    return (int(p[0] + offset * cos(angle)), int(p[1] + offset * sin(angle)))

def min_max(points):
    coords = tuple(zip(*points))
    return tuple(map(min, coords)), tuple(map(max, coords))
# 
# def midpoint(edge):
#     (xa, ya), (xb, yb) = edge
#     return (xa + xb) / 2.0, (ya + yb) / 2.0

py5.profile_functions(['key_pressed'])
py5.run_sketch(block=False)