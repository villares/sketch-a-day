# -*- coding: UTF-8 -*-
from villares.arcs import p_arc

def arc_filleted_poly(p_list, r_list, open_poly=False):
    """
    draws a 'filleted' polygon with variable radius
    dependent on roundedCorner()
    """
    p_list = list(p_list)
    r_list = list(r_list)
    beginShape()
    if not open_poly:
        for p0, p1, p2, r in zip(p_list,
                                [p_list[-1]] + p_list[:-1],
                                [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                                [r_list[-1]] + r_list[:-1]
                                ):
            m1 = (PVector(p0.x, p0.y) + PVector(p1.x, p1.y)) / 2
            m2 = (PVector(p2.x, p2.y) + PVector(p1.x, p1.y)) / 2
            roundedCorner(p1, m1, m2, r)
        endShape(CLOSE)
    else:
        for p0, p1, p2, r in zip(p_list[:-1],
                                [p_list[-1]] + p_list[:-2],
                                [p_list[-2]] + [p_list[-1]] + p_list[:-3],
                                [r_list[-1]] + r_list[:-2]
                                ):
            m1 = (PVector(p0.x, p0.y) + PVector(p1.x, p1.y)) / 2
            m2 = (PVector(p2.x, p2.y) + PVector(p1.x, p1.y)) / 2
            roundedCorner(p1, m1, m2, r)
        endShape()        

def roundedCorner(pc, p1, p2, r):
    """
    Based on Stackoverflow C# rounded corner post 
    https://stackoverflow.com/questions/24771828/algorithm-for-creating-rounded-corners-in-a-polygon
    """    
    def GetProportionPoint(pt, segment, L, dx, dy):
        factor = float(segment) / L if L != 0 else segment
        return PVector((pt.x - dx * factor), (pt.y - dy * factor))

    # Vectors 1 and 2
    dx1, dy1 = pc.x - p1.x, pc.y - p1.y
    dx2, dy2 = pc.x - p2.x, pc.y - p2.y
    # Angle between vector 1 and vector 2 divided by 2
    angle = (atan2(dy1, dx1) - atan2(dy2, dx2)) / 2
    # The length of segment between angular point and the
    # points of intersection with the circle of a given radius
    tng = abs(tan(angle))
    segment = r / tng if tng != 0 else r
    # Check the segment
    length1 = sqrt(dx1 * dx1 + dy1 * dy1)
    length2 = sqrt(dx2 * dx2 + dy2 * dy2)
    min_len = min(length1, length2)
    if segment > min_len:
        segment = min_len
        max_r = min_len * abs(tan(angle))
    else:
        max_r = r
    # Points of intersection are calculated by the proportion between
    # length of vector and the length of the segment.
    p1Cross = GetProportionPoint(pc, segment, length1, dx1, dy1)
    p2Cross = GetProportionPoint(pc, segment, length2, dx2, dy2)
    # Calculation of the coordinates of the circle
    # center by the addition of angular vectors.
    dx = pc.x * 2 - p1Cross.x - p2Cross.x
    dy = pc.y * 2 - p1Cross.y - p2Cross.y
    L = sqrt(dx * dx + dy * dy)
    d = sqrt(segment * segment + max_r * max_r)
    circlePoint = GetProportionPoint(pc, d, L, dx, dy)
    # StartAngle and EndAngle of arc
    startAngle = atan2(p1Cross.y - circlePoint.y, p1Cross.x - circlePoint.x)
    endAngle = atan2(p2Cross.y - circlePoint.y, p2Cross.x - circlePoint.x)
    # Sweep angle
    sweepAngle = endAngle - startAngle
    # Some additional checks
    ns = False
    if sweepAngle < 0:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle
        circle(circlePoint.x, circlePoint.y, max_r/2)
        ns = True
    ls = False
    if sweepAngle > PI:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = TWO_PI - sweepAngle
        circle(circlePoint.x, circlePoint.y, max_r)
        ls = True
    if (ls and ns) or not (ls or ns):   
    # if not ((ls or ns) and not (ls and ns)):
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle 

    p_arc(circlePoint.x, circlePoint.y, 2 * max_r, 2 * max_r,
        startAngle, startAngle + sweepAngle, mode=2)    
