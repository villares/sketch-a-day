from __future__ import division
from collections import deque


def is_poly_self_intersecting(poly_points):
    ed = poly_edges(poly_points)
    for a, b in ed[::-1]:
        for c, d in ed[2::]:
            # test only non consecutive edges
            if (a != c) and (b != c) and (a != d):
                if simple_intersect(a, b, c, d):
                    return True
    return False

def simple_intersect(*args):
    """Returns True if line segments intersect."""
    if len(args) == 2:    
        (a1, b1), (a2, b2) = args[0], args[1]
    else:
        a1, b1, a2, b2 = args
    return ccw(a1, b1, a2) != ccw(a1, b1, b2) and ccw(a2, b2, a1) != ccw(a2, b2, b1)

def point_inside_poly(x, y, points):
    # ray-casting algorithm based on
    # https://wrf.ecse.rpi.edu/Research/Short_Notes/pnpoly.html
    inside = False
    for i, p in enumerate(points):
        pp = points[i - 1]
        xi, yi = p
        xj, yj = pp
        intersect = ((yi > y) != (yj > y)) and (
            x < (xj - xi) * (y - yi) / (yj - yi) + xi)
        if intersect:
            inside = not inside
    return inside

def line_intersect(*args, **kwargs):
    """
    Adapted from Bernardo Fontes https://github.com/berinhard/sketches/
    2020-11-14 Does not assume Line objects anymore, and works with 4 points or 8 coords.
    2021_09_26 Adding intersection outside the segments. Also fixing bug when calling with 8 coords as arguments.
    2021_09_26 Removed line_a & line_b variables, rewrote ZeroDivision exception catching as a conditional check.
    """
    as_PVector = kwargs.get('as_PVector', False)
    in_segment = kwargs.get('in_segment', True)
    
    if len(args) == 2:  # expecting 2 Line objects or 2 tuples of 2 point tuples.
        (x1, y1), (x2, y2) = args[0]
        (x3, y3), (x4, y4) = args[1]
    elif len(args) == 4:
        (x1, y1), (x2, y2) = args[:2]
        (x3, y3), (x4, y4) = args[2:]
    elif len(args) == 8:
        x1, y1, x2, y2, x3, y3, x4, y4 = args
    else:
        raise ValueError, "line_intersect requires 2 lines, 4 points or 8 coords."
            
    divisor = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if divisor:
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / float(divisor)
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / float(divisor)
    else:
        return None
    if not in_segment or 0 <= uA <= 1 and 0 <= uB <= 1:
        x = x1 + uA * (x2 - x1)
        y = y1 + uA * (y2 - y1)
        return PVector(x, y) if as_PVector else (x, y)
    else:
        return None
    
def ccw(*args):
    """Returns True if the points are arranged counter-clockwise in the plane"""
    if len(args) == 1:
        a, b, c = args[0]
    else:
        a, b, c = args
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])

def edges_as_sets(poly_points, frozen=True):
    """
    Return a (frozen)set of poly edges as frozensets of 2 points.
    """
    if frozen:
        return frozenset(frozenset(edge) for edge in poly_edges(poly_points))
    else:
        return set(frozenset(edge) for edge in poly_edges(poly_points))

def poly_edges(poly_points):
    """
    Return a list of edges (tuples containing pairs of points)
    for a list of points that represent a closed polygon
    """
    return pairwise(poly_points) + [(poly_points[-1], poly_points[0])]


def pairwise(iterable):
    from itertools import tee
    "s -> (s0, s1), (s1, s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)



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
        for other_poly, other_holes in reversed(new_result):
            if point_inside_poly(poly[0][0], poly[0][1], other_poly):
                del new_result[i]
                other_holes.append(poly)
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
