
def setup():
    size(500, 500)
    # noCursor()

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
        beginShape()
        for x, y in path:
            vertex(x, y)
        endShape()
    fill(0, 100)
    beginShape()
    o = 30 + 10 * sin(degrees(frameCount / 5000.0))
    for x, y in offset_path(path, o):
        vertex(x, y) 
    endShape(CLOSE)
def offset_path(path, offset):
    a = calc_offset(path, offset)
    b = calc_offset(path[::-1], offset)
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
        # draw_seg(second_offset)
        # ip = point_offset(first_seg[1], offset, half_angle)
        # if not point_inside_poly(ip[0], ip[1], (first_offset[1], first_offset[1], second_offset[0])):
        ip = line_intersect(first_offset, second_offset, in_segment=True)
        if not ip:
            new_path.append(first_offset[1])
            new_path.append(second_offset[0])
            # ip = point_offset(first_seg[1], offset, half_angle)
            # line(first_seg[1][0], first_seg[1][1], ip[0], ip[1])
            # if not point_inside_poly(ip[0], ip[1], (first_offset[1], first_offset[1], second_offset[0])):
            #     ip = point_offset(first_seg[1], offset, half_angle + PI)
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
