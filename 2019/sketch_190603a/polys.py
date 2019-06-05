# -*- coding: utf-8 -*-

def poly(p_list, closed=True):
    beginShape()
    for p in p_list:
        if len(p) == 2 or p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()

def poly_arc_augmented(p_list, r_list):
    a_list = []
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 =  p_list[i2], r_list[i2], r_list[i1]
        a = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(a)
        # ellipse(p1[0], p1[1], 2, 2)

    for i1, _ in enumerate(a_list):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        #ellipse(p1[0], p1[1], r1 * 2, r1 * 2)
        a1 = a_list[i1]
        a2 = a_list[i2]
        if a1 and a2:
            start = a1 if a1 < a2 else a1 - TWO_PI
            arc(p2[0], p2[1], r2 * 2, r2 * 2, start, a2)
        else:
            ellipse(p2[0], p2[1], r2 * 2, r2 * 2)


def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = r1 - r2
    line_angle = atan2(p1[0] - p2[0], p2[1] - p1[1])
    if d > abs(ri):
        theta = asin(ri / float(d))

        x1 = cos(line_angle - theta) * r1
        y1 = sin(line_angle - theta) * r1
        x2 = cos(line_angle - theta) * r2
        y2 = sin(line_angle - theta) * r2
        # line(p1[0] - x1, p1[1] - y1, p2[0] - x2, p2[1] - y2)
    
        x1 = -cos(line_angle + theta) * r1
        y1 = -sin(line_angle + theta) * r1
        x2 = -cos(line_angle + theta) * r2
        y2 = -sin(line_angle + theta) * r2
        line(p1[0] - x1, p1[1] - y1, p2[0] - x2, p2[1] - y2)
        return line_angle + theta
    else:
    #     # line(p1[0], p1[1], p2[0], p2[1])
        return None


def poly_filleted(p_list, r_list=None, open_poly=False):
    """
    draws a 'filleted' polygon with variable radius
    dependent on roundedCorner()
    """
    if not r_list:
        r_list = [0] * len(p_list)

    if not open_poly:
        with pushStyle():
            noStroke()
            beginShape()
            for p0, p1 in zip(p_list, [p_list[-1]] + p_list[:-1]):
                m = (PVector(p0[0], p0[1]) + PVector(p1[0], p1[1])) / 2
                vertex(m[0], m[1])
            endShape(CLOSE)
        for p0, p1, p2, r in zip(p_list,
                                 [p_list[-1]] + p_list[:-1],
                                 [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                                 [r_list[-1]] + r_list[:-1]
                                 ):
            m1 = (PVector(p0[0], p0[1]) + PVector(p1[0], p1[1])) / 2
            m2 = (PVector(p2[0], p2[1]) + PVector(p1[0], p1[1])) / 2
            roundedCorner(p1, m1, m2, r)
    else:
        for p0, p1, p2, r in zip(p_list[:-1],
                                 [p_list[-1]] + p_list[:-2],
                                 [p_list[-2]] + [p_list[-1]] + p_list[:-3],
                                 [r_list[-1]] + r_list[:-2]
                                 ):
            m1 = (PVector(p0[0], p0[1]) + PVector(p1[0], p1[1])) / 2
            m2 = (PVector(p2[0], p2[1]) + PVector(p1[0], p1[1])) / 2
            roundedCorner(p1, m1, m2, r)


def roundedCorner(pc, p1, p2, r):
    """
    Based on Stackoverflow C# rounded corner post 
    https://stackoverflow.com/questions/24771828/algorithm-for-creating-rounded-corners-in-a-polygon
    """
    def GetProportionPoint(pt, segment, L, dx, dy):
        factor = float(segment) / L if L != 0 else segment
        return PVector((pt[0] - dx * factor), (pt[1] - dy * factor))

    # Vector 1
    dx1 = pc[0] - p1[0]
    dy1 = pc[1] - p1[1]

    # Vector 2
    dx2 = pc[0] - p2[0]
    dy2 = pc[1] - p2[1]

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
    dx = pc[0] * 2 - p1Cross[0] - p2Cross[0]
    dy = pc[1] * 2 - p1Cross[1] - p2Cross[1]

    L = sqrt(dx * dx + dy * dy)
    d = sqrt(segment * segment + max_r * max_r)

    circlePoint = GetProportionPoint(pc, d, L, dx, dy)

    # StartAngle and EndAngle of arc
    startAngle = atan2(p1Cross[1] - circlePoint[1], p1Cross[0] - circlePoint[0])
    endAngle = atan2(p2Cross[1] - circlePoint[1], p2Cross[0] - circlePoint[0])

    # Sweep angle
    sweepAngle = endAngle - startAngle

    # Some additional checks
    if sweepAngle < 0:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle

    if sweepAngle > PI:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = TWO_PI - sweepAngle

    with pushStyle():
        noStroke()
        beginShape()
        vertex(p1[0], p1[1])
        vertex(p1Cross[0], p1Cross[1])
        vertex(p2Cross[0], p2Cross[1])
        vertex(p2[0], p2[1])
        endShape(CLOSE)

    line(p1[0], p1[1], p1Cross[0], p1Cross[1])
    line(p2[0], p2[1], p2Cross[0], p2Cross[1])
    arc(circlePoint[0], circlePoint[1], 2 * max_r, 2 * max_r,
        startAngle, startAngle + sweepAngle)
    
