def setup():
    size(500, 500)

def draw():
    background(230)
    path = (
        (50, 100),
        (250, 150),
        # (300, 450),
        (mouseX, mouseY),
        (450, 450),
        (450, 100),
    )
    with pushStyle():
        noFill()
        stroke(128)
        strokeWeight(1)
        # beginShape()
        # for x, y in path:
        #     vertex(x, y)
        # endShape()
    fill(0, 100)
    o = 30 #+ 10 * sin(degrees(frameCount / 5000.0))
    op = offset_path(path, o)
    if is_poly_self_intersecting(op):
        fill(200, 0, 0)
    beginShape()        
    for x, y in op:
        vertex(x, y) 
    endShape(CLOSE)
    
def offset_path(path, offset):
    a = calc_offset(path, offset)
    b = calc_offset(path[::-1], offset)
    if keyPressed:
        a = remove_loops(a)
        b = remove_loops(b)
    return a + b
                        
def calc_offset(path, offset):
    first_seg = path[:2]  # first segment
    first_angle = seg_angle(first_seg)
    first_point = point_offset(first_seg[0], offset, first_angle)
    first_offset = seg_offset(first_seg, offset)
    # draw_seg(first_offset)
    new_path = [first_point, first_offset[0]]
    for p in path[2:]:
        second_seg = (first_seg[1], p)
        second_offset = seg_offset(second_seg, offset)
        half_angle = (seg_angle(first_seg) + seg_angle(second_seg)) / 2 - HALF_PI
        ip = line_intersect(first_offset, second_offset, in_segment=True)
        if not ip:
            new_path.append(first_offset[1])
            new_path.append(second_offset[0])
        else:
            new_path.append(ip)
        # prepare for next loop    
        first_seg = second_seg
        first_offset = second_offset
    new_path.append(second_offset[1]) # final offset point
    return new_path 
   
def draw_seg(seg):
    (xa, ya), (xb, yb) = seg
    line(xa, ya, xb, yb)
        
def seg_offset(seg, offset):
    angle = seg_angle(seg) + HALF_PI  # angle perpendiculat to seg
    return point_offset(seg[0], offset, angle), point_offset(seg[1], offset, angle)    
    
def point_offset(p, offset, angle):
    return p[0] + offset * cos(angle), p[1] + offset * sin(angle)    
                
def seg_angle(seg):
    (xa, ya), (xb, yb) = seg
    return atan2(yb - ya, xb - xa) + PI
 
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
        uA = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / divisor
        uB = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / divisor
    else:
        return None
    if not in_segment or 0 <= uA <= 1 and 0 <= uB <= 1:
        x = x1 + uA * (x2 - x1)
        y = y1 + uA * (y2 - y1)
        return (x, y)
    else:
        return None

def is_poly_self_intersecting(poly_points):
    edges = poly_edges(poly_points)
    for a, b in edges[::-1]:
        for c, d in edges[2::]:
            # test only non consecutive edges
            if (a != c) and (b != c) and (a != d):
                if simple_intersect(a, b, c, d):
                    return True
    return False

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

def ccw(*args):
    """Returns True if the points are arranged counter-clockwise in the plane"""
    if len(args) == 1:
        a, b, c = args[0]
    else:
        a, b, c = args
    return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])


def simple_intersect(*args):
    """Returns True if line segments intersect."""
    if len(args) == 2:    
        (a1, b1), (a2, b2) = args[0], args[1]
    else:
        a1, b1, a2, b2 = args
    return ccw(a1, b1, a2) != ccw(a1, b1, b2) and ccw(a2, b2, a1) != ccw(a2, b2, b1)


# def remove_loops(poly_points):
#     edges = poly_edges(poly_points)
#     new_path = []
#     next_point = None
#     for a, b in edges[::-1]:
#         if next_point is not None and a != next_point:
#             continue
#         else:
#             next_point = None
#         for c, d in edges[2::]:
#             # test only non consecutive edges
#             if (a != c) and (b != c) and (a != d):
#                 ip =  line_intersect(a, b, c, d)
#                 if ip:    
#                     new_path.append(a)
#                     new_path.append(ip)
#                     next_point = d
#                     break        
#         new_path.append(a)
#         last_point = b
#     #new_path.append(last_point)
#     return new_path

def remove_loops(path):
    path = list(path)
    crossings = []
    for i, (pa, pb) in enumerate(zip(path, path[1:]), 2):
        for pc, pd in zip(path[2:], path[3:]):
            if pb == pc or pd == pa or pa == pc or pb == pd:
                continue
            ip = line_intersect(pa, pb, pc, pd)
            if ip:
                crossings.append((i, ip))
    if len(crossings) >= 2:
        (ia, ip), (ib, _) = crossings[-2:]
        path = path[:ia - 1] + [ip] + path[ib - 1:] 
        #crossings = crossings[:-2]        
    for i, (x, y) in crossings:
        print(i, x, y)
        circle(x, y, 20 - i * 2)
    return tuple(path)
