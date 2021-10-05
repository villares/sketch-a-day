from __future__ import division
from helpers import line_intersect, point_inside_poly, ccw, poly_edges
from collections import deque

def setup():
    size(500, 500)
    noCursor()
    textFont(createFont('Inconsolata Bold', 8))
    
def draw():
    global t1, t2
    background(200)
    scale(2)
    # noFill()
    t2 = [((50, 40), (200, 90), (100, 230)), [((mouseX, mouseY), (mouseX, mouseY +20),  (mouseX + 20, mouseY))]] 
    r = 40
    # t1 = [(mouseX + (r if  a % 2 else r / 2) * cos(radians(a)),
    #        mouseY + (r if  a % 2 else r / 2) * sin(radians(a)))
    #       for a in range(0, 360, 15) ]                   
    stroke(0)
    fill(255, 200)
    draw_poly(t2)    
    # stroke(255) ; draw_poly(t1) 

    translate(10, 10)    
    stroke(0, 200, 0)
    fill(100, 64)
    draw_polys(join_edges(subtraction_edges(t2[0], t2[1][0])))
    stroke(0, 0, 200)
    fill(150, 64)
    # draw_polys(diff_shapes(t1, t2))
    stroke(200, 0, 0)
    fill(240, 64)
    translate(1, 1)    
    # draw_polys(inter_shapes(t1, t2)/)

    
def mousePressed():
    print(diff_shapes(t1, t2))
    
def union_shapes(a, b):
    return join_edges(union_edges(t1, t2))
    
def diff_shapes(a, b):
    return join_edges(subtraction_edges(a, b))

def inter_shapes(a, b):
    return join_edges(intersection_edges(t1, t2))
    
def join_edges(edges):
    result = []
    if edges:
        poly = fail = 0
        edges_left = deque((edges))
        start = edges_left.popleft() 
        result.append(list(start))
        while edges_left and poly < len(edges) / 3:
            edge = edges_left.popleft()
            if is_close(edge[0], result[poly][-1]):
                result[poly].append(edge[1])  #;print(edge, result[poly][-1])
            elif is_close(edge[1], result[poly][-1]):
                result[poly].append(edge[0]) #;print(edge[1], result[poly][-1], 'i')
            else:
               fail += 1
               if fail > len(edges) * 10:
                   poly += 1
                   # print(fail, edges_left)
                   fail = 0
                   result.append(list(edge))
               else:
                   edges_left.append(edge)
    new_result = []
    for poly in result:
        if is_close(poly[0], poly[-1]):
            poly.pop()
        if len(poly) > 2:
            new_result.append((poly, [])) # poly, empty holes list
    # print new_result
    for i, (poly, holes) in reversed(list(enumerate(new_result))):
        for other_poly, othe_holes in new_result:
            if point_inside_poly(poly[0][0], poly[0][1], other_poly):
                del new_result[i]
                othe_holes.append(poly)
                break
    return new_result
      
def intersection_edges(shape_a, shape_b):
    split_a, split_b = split_both_shapes(shape_a, shape_b)
    a_edges_in_b = edges_inside_poly(split_a, shape_b)
    b_edges_in_a = edges_inside_poly(split_b, shape_a)
    return a_edges_in_b + b_edges_in_a

def subtraction_edges(shape_a, shape_b):
    split_a, split_b = split_both_shapes(shape_a, shape_b)
    a_edges_in_b = edges_inside_poly(split_a, shape_b)
    b_edges_in_a = edges_inside_poly(split_b, shape_a)
    diff = set(split_a + b_edges_in_a) - set(a_edges_in_b)
    return diff

def union_edges(shape_a, shape_b):
    split_a, split_b = split_both_shapes(shape_a, shape_b)
    a_edges_in_b = edges_inside_poly(split_a, shape_b)
    b_edges_in_a = edges_inside_poly(split_b, shape_a)
    union = set(split_a + split_b) - set(a_edges_in_b + b_edges_in_a)
    return union
  
def is_close(a, b):
    tol = 1
    return abs(a[0] - b[0]) < tol and abs(a[1] - b[1]) < tol
              
def int_edges(edges):
    return [(tuple(map(int, edge[0])),
            tuple(map(int, edge[1]))) for edge in edges]
    
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
         
def edges_inside_poly(edges, poly):
    return [edge for edge in edges if edge_in_poly(edge, poly)]
                  
def edge_in_poly(edge, poly):
    x, y = midpoint(edge)
    return point_inside_poly(x, y, poly)

def midpoint(edge):
    (xa, ya), (xb, yb) = edge
    return (xa + xb) / 2.0, (ya + yb) / 2.0
    
def draw_poly(points):
    if len(points) == 2:
        points, holes = points
    else:
        holes = []
    beginShape()
    for x, y in points:
        vertex(x, y)
    for hole in holes:
        beginContour()
        for x, y in hole:
            vertex(x, y)
        endContour()
    endShape(CLOSE)

def draw_polys(polys):
    for i, poly in enumerate(polys):
        draw_poly(poly)
        push()
        textSize(10)
        fill(g.strokeColor)
        # x, y = poly[0]
        # text(i, x + 5, y + 5)
        pop()
        
def draw_edges(edges):
    push()
    translate(2, 2) # debug hack!
    for i, ((xa, ya), (xb, yb)) in enumerate(edges):
        line(xa, ya, xb, yb)
        # text(i, xa, ya)
    pop()
