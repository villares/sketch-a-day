# -*- coding: utf-8 -*-

def c_poly_arc_augmented(op_list, or_list):
    assert len(op_list) == len(or_list), \
        "Number of points and radii not the same"
    # remove overlapping adjacent points
    p_list, r_list, r2_list = [], [], or_list[:]
    for i1, p1 in enumerate(op_list):
        i2 = (i1 + 1) % len(op_list)
        p2, r2, r1 = op_list[i2], r2_list[i2], r2_list[i1]
        if dist(p1[0], p1[1], p2[0], p2[1]) > 1: # or p1 != p2:
            p_list.append(p1)
            r_list.append(r1)
        else:
            r2_list[i2] = min(r1, r2) 
    # reduce radius that won't fit
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 = p_list[i2], r_list[i2], r_list[i1]
        r_list[i1], r_list[i2] = reduce_radius(p1, p2, r1, r2)    
    # calculate the tangents
    a_list = [] 
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 = p_list[i2], r_list[i2], r_list[i1]
        a = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(a)
    # draw
    beginShape()
    for i1, _ in enumerate(a_list):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a1, p11, p12 = a_list[i1]
        a2, p21, p22 = a_list[i2]
        if a1 and a2:
            start = a1 if a1 < a2 else a1 - TWO_PI
            c_arc(p2[0], p2[1], r2 * 2, r2 * 2, start, a2, arc_type=2)
        else:
            # when the the segment is smaller than the diference between
            # radius, circ_circ_tangent won't renturn the angle
            # ellipse(p2[0], p2[1], r2 * 2, r2 * 2) # debug
            if a1:
                vertex(p12[0], p12[1])
            if a2:
                vertex(p21[0], p21[1])
    endShape(CLOSE)

def reduce_radius(p1, p2, r1, r2):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = abs(r1 - r2)
    if d - ri < 0:
        if r1 > r2:
            r1 = map(d, ri + 1, 0, r1, r2)
        else:
            r2 = map(d, ri + 1, 0, r2, r1)
    return(r1, r2)

def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = r1 - r2
    line_angle = atan2(p1[0] - p2[0], p2[1] - p1[1])
    if d - abs(ri) > 0:
        theta = asin(ri / float(d))
        x1 = -cos(line_angle + theta) * r1
        y1 = -sin(line_angle + theta) * r1
        x2 = -cos(line_angle + theta) * r2
        y2 = -sin(line_angle + theta) * r2
        return (line_angle + theta,
                (p1[0] - x1, p1[1] - y1),
                (p2[0] - x2, p2[1] - y2))
    else:
        return (None,
                (p1[0], p1[1]),
                (p2[0], p2[1]))

def c_poly_filleted(p_list, r_list=None, open_poly=False):
    """
    draws a 'filleted' polygon with variable radius
    dependent on roundedCorner()
    """
    if not r_list:
        r_list = [0] * len(p_list)
    assert len(p_list) == len(r_list), \
        "Number of points and radii not the same"
    strokeJoin(ROUND)
    beginShape()
    for p0, p1, p2, r in zip(p_list,
                             [p_list[-1]] + p_list[:-1],
                             [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                             [r_list[-1]] + r_list[:-1]
                             ):
        m1 = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        m2 = (p2[0] + p1[0]) / 2, (p2[1] + p1[1]) / 2
        b_roundedCorner(p1, m1, m2, r)
    endShape(CLOSE)

def b_roundedCorner(pc, p2, p1, r):
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
    startAngle = atan2(p1Cross[1] - circlePoint[1],
                       p1Cross[0] - circlePoint[0])
    endAngle = atan2(p2Cross[1] - circlePoint[1],
                     p2Cross[0] - circlePoint[0])
    # Sweep angle
    sweepAngle = endAngle - startAngle
    # Some additional checks
    A, B = False, False
    if sweepAngle < 0:
        A = True
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle
        # ellipse(pc[0], pc[1], 15, 15) # debug
    if sweepAngle > PI:
        B = True
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = TWO_PI - sweepAngle
        # ellipse(pc[0], pc[1], 25, 25) # debug
    if (A and not B) or (B and not A):
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle
        # ellipse(pc[0], pc[1], 5, 5) # debug
    c_arc(circlePoint[0], circlePoint[1], 2 * max_r, 2 * max_r,
          startAngle, startAngle + sweepAngle, arc_type=2)


def c_arc(cx, cy, w, h, startAngle, endAngle, arc_type=0, num_points=None):
    """
    A poly approximation of an arc
    using the same signature as the original Processing arc()
    arc_type: 0 "normal" arc, using beginShape() and endShape()
              2 "naked" like normal, but without beginShape() and endShape()
                 for use inside a larger PShape
    """
    if not num_points:
        num_points = 12
    sweepAngle = endAngle - startAngle  
    if arc_type == 0:
            beginShape()
    if sweepAngle < 0:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle 
        angle = sweepAngle / int(num_points)
        a = endAngle
        while a >= startAngle:
                sx = cx + cos(a) * w / 2.
                sy = cy + sin(a) * h / 2.
                vertex(sx, sy)
                a -= angle   
    elif sweepAngle > 0:
        angle = sweepAngle / int(num_points)
        a = startAngle
        while a <= endAngle:
                sx = cx + cos(a) * w / 2.
                sy = cy + sin(a) * h / 2.
                vertex(sx, sy)
                a += angle
    else:
        sx = cx + cos(startAngle) * w / 2.
        sy = cy + sin(startAngle) * h / 2.
        vertex(sx, sy)
    if arc_type == 0:
        endShape()
