
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
    )
    with pushStyle():
        noFill()
        stroke(128)
        strokeWeight(5)
        beginShape()
        for x, y in path:
            vertex(x, y)
        endShape()
    offset = 20
    segments = []
    for (xa, ya), (xb, yb) in zip(path[:-1], path[1:]):
        angle = atan2(yb - ya, xb - xa)
        v = PVector.fromAngle(angle + HALF_PI) * offset 
        ro = (xa + v.x, ya + v.y, xb + v.x, yb + v.y)
        lo = (xa - v.x, ya - v.y, xb - v.x, yb - v.y)
        line(*ro)
        line(*lo)
        segments.append((xa, ya, xb, yb, ro, lo, angle))
        
    for sa, sb in zip(segments[:-1], segments[1:]):
        angle_m = (sa[-1] + sb[-1]) / 2
        v = PVector.fromAngle(angle_m + HALF_PI) * offset
        xa, ya = sa[2:4]
        line(xa - v.x, ya - v.y, xa + v.x, ya + v.y)
        roa = sa[4]
        rob = sb[4]
        p = line_intersect(*(roa + rob), in_segment=False)
        if p:
            circle(p[0], p[1], 5)
        loa = sa[5]
        lob = sb[5]
        p = line_intersect((loa[:2], loa[2:]), (lob[:2], lob[2:]), in_segment=False)
        if p:
            circle(p[0], p[1], 5)
            
            
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
