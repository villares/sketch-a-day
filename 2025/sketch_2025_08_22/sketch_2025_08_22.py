import py5
from py5 import atan2, sin, cos

import shapely
from shapely.ops import unary_union

start = [
    shapely.Polygon(
        ((0, 0), (0, 30), (30, 30))
        ),
    ]

all_polys = start[0]
polys = start.copy()
unvisited_polys = start.copy()

def setup():
    py5.size(600, 600)
    py5.color_mode(py5.HSB)

def draw():
    global p
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(0, 150)
    for p in polys:
        py5.fill(p.area * 0.2 % 255, 255, 255, 150)
        py5.shape(p)


def key_pressed():
    global all_polys
    if py5.key == ' ':
        print(len(unvisited_polys), len(polys))
        unvisited_polys[:] = grow(unvisited_polys)
        polys.extend(unvisited_polys)
    elif py5.key == 'c':
        all_polys = start[0]
        unvisited_polys[:] = start
        polys[:] = start
    elif py5.key == 's':
        py5.save_frame('###.png')

def grow(polys):
    global all_polys
    #shrinked_all_polys = all_polys.buffer(-1) # this allows a bit of overlap
    for poly in polys:
        p = tuple(poly.exterior.coords)
        for edge in zip(p, p[1:] + (p[0],)):
            ea, eb = edge
            m = midpoint(edge)
            ang = edge_angle(edge)
            da = py5.dist(*ea, *eb) * py5.random(0.66, 1)
            pm = point_offset(m, da, ang - py5.PI / 2)
            #db = py5.dist(*ea, *eb) * py5.random(0.66, 1)
            #pb = point_offset(eb, db, ang - py5.PI / 2)
            new_p = shapely.Polygon((ea, pm, eb))
            shrinked = new_p.buffer(-1)
            if (shrinked.area > 10 and
                not all_polys.intersects(shrinked)):
                try:
                    all_polys = all_polys.union(new_p)
                    yield new_p
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

def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0

py5.profile_functions(['key_pressed'])
py5.run_sketch(block=False)