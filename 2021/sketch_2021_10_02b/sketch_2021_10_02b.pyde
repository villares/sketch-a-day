from __future__ import division
from helpers import line_intersect, point_inside_poly, ccw, poly_edges

def setup():
    size(500, 500)
    noCursor()
    
def draw():
    background(200)
    scale(2)
    noFill()
    stroke(0)
    t2 = [(50, 50), (200, 100), (150, 150)] ; draw_poly(t2)
    r = 50
    t1 = [(mouseX + (r if  a % 2 else r / 2) * cos(radians(a)),
           mouseY + (r if  a % 2 else r / 2) * sin(radians(a)))
          for a in range(0, 360, 15) ]; draw_poly(t1)
    
    split_t1, split_t2 = split_both_shapes(t1, t2)
                  
    stroke(255, 0, 0)     
    t1e_in_t2 = edges_inside_poly(split_t1, t2)
    draw_edges(t1e_in_t2)
    stroke(0, 0, 200)
    t2e_in_t1 = edges_inside_poly(split_t2, t1)
    draw_edges(t2e_in_t1)
    
def edges_inside_poly(edges, poly):
    return [edge for edge in edges if edge_in_poly(edge, poly)]
    
def split_both_shapes(poly_a, poly_b):
    a_edges = poly_edges(poly_a)
    b_edges = poly_edges(poly_b)
    return (
        split_edges(a_edges, b_edges),
        split_edges(b_edges, a_edges),
    )
    
def split_edges(a_edges, b_edges):
    a_split = []
    for edge in a_edges:    
        a_split += split_edge(edge, b_edges)               
    return a_split
    
def split_edge(edge, edges):
    points = []
    for other in edges:
        ip = line_intersect(edge, other)
        if ip:
            points.append(ip)
            # circle(ip[0], ip[1], 5) # visual debug aid
    if not points:
        return [edge]
    else:
        points.sort(key=lambda p: sq_dist(edge[0], p))
        return split_edge_at_points(edge, points)

def split_edge_at_points(edge, points):
    if len(points) == 1:
        return [(edge[0], points[0]), (points[0], edge[1])]
    else:
        return [(edge[0], points[0])] + split_edge_at_points((points[0], edge[1]), points[1:]) 
                    
def sq_dist(a, b):
    (xa, ya), (xb, yb) = a, b
    return (xa - xb) * (xa - xb) + (ya - yb) * (ya - yb)
            
def draw_edges(edges):
    push()
    translate(2, 2) # debug hack!
    for (xa, ya), (xb, yb) in edges:
        line(xa, ya, xb, yb)
    pop()

def edge_in_poly(edge, poly):
    x, y = midpoint(edge)
    return point_inside_poly(x, y, poly)

def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0
    
def draw_poly(points):
    beginShape()
    for x, y in points:
        vertex(x, y)
    endShape(CLOSE)
