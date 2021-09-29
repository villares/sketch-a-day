from villares.arcs import *

def setup():
    size(500, 500)
    noCursor()

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
        strokeWeight(5)
        beginShape()
        for x, y in path:
            vertex(x, y)
        endShape()
    stroke(0, 0, 100)
    draw_offset(path, offset=20)
    stroke(0, 100, 0)
    draw_offset(tuple(reversed(path)), offset=20)
        
def draw_offset(path, offset):
    first_seg = path[:2]  # first segment
    first_offset = seg_offset(first_seg, 20)
    draw_seg(first_offset)
    for p in path[2:]:
        second_seg = (first_seg[1], p)
        second_offset = seg_offset(second_seg, 20)
        draw_seg(second_offset)
        ip = line_intersect(first_offset, second_offset, in_segment=True)
        if not ip:
            half_angle = (seg_angle(first_seg) + seg_angle(second_seg)) / 2 + HALF_PI
           #half_angle = half_angle + PI if half_angle < 0 else half_angle 
            # ip = point_offset(first_seg[1], offset, half_angle)
            ip = line_intersect(first_offset, second_offset, in_segment=False)
            # fill(0)
            # line(first_seg[1][0], first_seg[1][1], ip[0], ip[1])
            if ip:
                text(degrees(seg_angle(first_seg)), ip[0], ip[1])
                beginShape()       
                arc_corner(ip, first_offset[1], second_offset[0], 100)
                endShape()                
        else:
            circle(ip[0], ip[1], 5) 

        # prepare for next loop    
        first_seg = second_seg
        first_offset = second_offset
        
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
    return atan2(yb - ya, xb - xa)
            
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
