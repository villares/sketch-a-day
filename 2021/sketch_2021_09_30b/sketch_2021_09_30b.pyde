from __future__ import division
from helpers import line_intersect, point_inside_poly, ccw

def setup():
    size(500, 500)
    noCursor()
    
def draw():
    background(200)
    scale(2)
    noFill()
    stroke(0)
    t1 = [(100, 100), (200, 100), (150, 150)] ; draw_t(t1)
    t2 = [(mouseX, mouseY), (mouseX +50, mouseY), (mouseX + 25, mouseY + 100)]; draw_t(t2)
    edges1 = t_edges(t1)
    edges2 = t_edges(t2)
    split_edges1 = []
    for edge in edges1:    
        split_edges1 += split_edges(edge, edges2)               
    split_edges2 = []
    for edge in edges2:    
        split_edges2 += split_edges(edge, edges1)               
    stroke(255, 0, 0)     
    edges1_in_t2 = [edge for edge in split_edges1 if edge_in_poly(edge, t2)]
    draw_edges(edges1_in_t2)
    # draw_edges(split_edges1)   
    stroke(0, 0, 200)
    edges2_in_t1 = [edge for edge in split_edges2 if edge_in_poly(edge, t1)]
    draw_edges(edges2_in_t1)
    # draw_edges(split_edges2)   
    
def split_edges(edge, edges):
    points = []
    for other in edges:
        ip = line_intersect(edge, other)
        if ip:
            points.append(ip)
            circle(ip[0], ip[1], 5)
    if not points:
        return  [edge]
    else:
        return split_single_edge(edge, points)

def split_single_edge(edge, points):
    if len(points) == 1:
        return [(edge[0], points[0]), (points[0], edge[1])]
    elif sq_dist(edge[0], points[0]) < sq_dist(edge[0], points[1]):
        return [(edge[0], points[0]), (points[0], points[1]), (points[1], edge[1])]         
    else:
        return [(edge[0], points[1]), (points[1], points[0]), (points[0], edge[1])]         
            
def sq_dist(a, b):
    (xa, ya), (xb, yb) = a, b
    return (xa - xb) * (xa - xb) + (ya - yb) * (ya - yb)
            
def draw_edges(edges):
    push()
    translate(2, 2)
    for (xa, ya), (xb, yb) in edges:
        line(xa, ya, xb, yb)
    pop()

def edge_in_poly(edge, poly):
    x, y = midpoint(edge)
    return point_inside_poly(x, y, poly)

def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0
    
def draw_t(t):
    triangle(*(t[0] + t[1] + t[2]))

def t_edges(t):
    a, b, c = t if not ccw(t) else t[::-1]
    return [(a, b), (b, c), (c, a)]
