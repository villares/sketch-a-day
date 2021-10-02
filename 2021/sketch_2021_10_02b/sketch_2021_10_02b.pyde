from __future__ import division
from helpers import line_intersect, point_inside_poly, ccw, poly_edges
from collections import deque

def setup():
    size(500, 500)
    noCursor()
    
def draw():
    global t1, t2
    background(200)
    scale(2)
    noFill()
    stroke(0)
    t2 = [(50, 50), (200, 100), (150, 150)] ; draw_poly(t2)
    r = 50
    t1 = [(mouseX + (r if  a % 2 else r / 2) * cos(radians(a)),
           mouseY + (r if  a % 2 else r / 2) * sin(radians(a)))
          for a in range(0, 360, 15) ]; draw_poly(t1)
                          
    stroke(0, 0, 200)
    draw_edges(int_edges(union_edges(t1, t2)))
    stroke(200, 0, 0)
    draw_polys(join_edges(union_edges(t1, t2)))
    
def keyPressed():
    print(join_edges(union_edges(t1, t2))),  
    
def join_edges(edges):
    result = []
    if edges:
        poly = fail = 0
        edges_left = deque(int_edges(edges))
        start = edges_left.popleft()
        result.append(list(start))
        while edges_left and poly < len(edges) / 3:
            edge = edges_left.popleft()
            if edge[0] == result[poly][-1]:
                result[poly].extend(edge)
            elif edge[1] == result[poly][-1]:
                result[poly].extend(reversed(edge))
            else:
               fail += 1
               if fail > len(edges):
                   poly += 1
                   fail = 0
                   result.append(list(edge))
               else:
                   edges_left.append(edge)
    return result
  
def int_edges(edges):
    return [(tuple(map(int, edge[0])),
            tuple(map(int, edge[1]))) for edge in edges] 
        
def union_edges(shape_a, shape_b):
    split_a, split_b = split_both_shapes(shape_a, shape_b)
    a_edges_in_b = edges_inside_poly(split_a, shape_b)
    b_edges_in_a = edges_inside_poly(split_b, shape_a)
    return a_edges_in_b + b_edges_in_a
        
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

def draw_polys(polys):
    for poly in polys:
        draw_poly(poly)
        
def draw_edges(edges):
    push()
    textSize(8)
    translate(2, 2) # debug hack!
    for i, ((xa, ya), (xb, yb)) in enumerate(edges):
        line(xa, ya, xb, yb)
        text(i, xa, ya)
    pop()
