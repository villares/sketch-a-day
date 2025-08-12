# sketch_2021_10_20c_py5

import py5

import numpy as np
from numpy import atan2, pi, sin, cos

import shapely
from shapely.ops import unary_union

Vertex = np.dtype([('x','f4'), ('y','f4')])
Edge = np.dtype([('va', Vertex), ('vb',Vertex)])
Triangle = np.dtype([('va', Vertex), ('vb', Vertex), ('vc', Vertex)])

tris = [
  # ((30, 0), (0, 30), (30, 30)),
  #  ((20, 10), (10, 20), (20, 20)),
    ]

all_tris = shapely.Polygon()
unvisited_tris = tris[:]
edges_drag = []

def setup():
    py5.size(600, 600)
   # print(min_max(tris[1]))


def draw():
    py5.background(240, 240, 220)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.stroke(0, 64)
    #py5.shape(all_tris)
    #py5.no_stroke()
    py5.fill(50, 150, 150, 100)
    for t in tris:
        py5.begin_shape()
        for x, y in t:
            py5.vertex(x, y)
        py5.end_shape(py5.CLOSE)


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
 
def key_pressed():
    global all_tris
    if py5.key == ' ':
        print(len(unvisited_tris), len(tris))
        unvisited = unvisited_tris[:]
        unvisited_tris[:] = [] 
        nptris = np.array(unvisited, dtype=Triangle)
        #grow(nptris)
        for t in unvisited:
            grow(t)
        tris.extend(unvisited_tris)
    elif py5.key == 'c':
        all_tris = shapely.Polygon()
        unvisited_tris.clear()
        tris.clear()
    elif py5.key == 's':
        py5.save_frame('###.png')

#@np.vectorize
def grow(t):
    global all_tris
    (xa, ya), (xb, yb), (xc, yc) = t
    for edge in (((xa, ya), (xb, yb)),
                 ((xb, yb), (xc, yc)),
                 ((xc, yc), (xa, ya))):
        process_edge(edge)

def mouse_pressed():
    if py5.mouse_button == py5.RIGHT:
        py5.print_line_profiler_stats()


        
def process_edge(e):
    global all_tris
    e0, e1 = e
    a = edge_angle(e)
    m = midpoint(e)
    d = py5.dist(*e0, *e1) * py5.random(0.66, 1)
    p = point_offset(m, d, a - pi / 2)
    n = (e0, p, e1)
    t = shapely.Polygon(n)
    #print(t)
    if not all_tris.contains(t):
        #n = np.array((e0, p, e1), dtype=Triangle)
        unvisited_tris.append(n)
        try:
            all_tris = all_tris.union(t)
        except shapely.GEOSException:
            print('GEOSException')

def edge_angle(edge):
    (xa, ya), (xb, yb) = edge
    return atan2(yb - ya, xb - xa) + pi

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