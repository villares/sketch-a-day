# -*- coding: utf-8 -*-

ROTATION = {0: 0,
            BOTTOM: 0,
            DOWN: 0,
            1: HALF_PI,
            LEFT: HALF_PI,
            2: PI,
            TOP: PI,
            UP: PI,
            3: PI + HALF_PI,
            RIGHT: PI + HALF_PI,
            BOTTOM + RIGHT: 0,
            DOWN + RIGHT: 0,
            DOWN + LEFT: HALF_PI,
            BOTTOM + LEFT: HALF_PI,
            TOP + LEFT: PI,
            UP + LEFT: PI,
            TOP + RIGHT: PI + HALF_PI,
            UP + RIGHT: PI + HALF_PI,
            }

def quarter_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, ROTATION[quadrant], HALF_PI)

def half_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, ROTATION[quadrant], PI)

def circle_arc(x, y, radius, start_ang, sweep_ang):
    arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang)

def poly_arc(x, y, radius, start_ang, sweep_ang, num_points=2):
    angle = sweep_ang / int(num_points)
    a = start_ang
    with beginShape():
        while a <= start_ang + sweep_ang:
            sx = x + cos(a) * radius
            sy = y + sin(a) * radius
            vertex(sx, sy)
            a += angle

def arc_poly(x, y, d, _, start_ang, end_ang, num_points=5):
    sweep_ang = end_ang - start_ang
    angle = sweep_ang / int(num_points)
    a = start_ang
    with beginShape():
        while a <= end_ang:
            sx = x + cos(a) * d / 2
            sy = y + sin(a) * d / 2
            vertex(sx, sy)
            a += angle

def bar(x1, y1, x2, y2, thickness=None, shorter=0, ends=(1, 1)):
    """
    O código para fazer as barras, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    """
    L = dist(x1, y1, x2, y2)
    if not thickness:
        thickness = 10
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        line(thickness / 2, offset, thickness / 2, L - offset)
        line(-thickness / 2, offset, -thickness / 2, L - offset)
        if ends[0]:
            half_circle(0, offset, thickness / 2, UP)
        if ends[1]:
            half_circle(0, L - offset, thickness / 2, DOWN)

def var_bar(p1x, p1y, p2x, p2y, r1, r2=None):
    if r2 is None:
        r2 = r1
    d = dist(p1x, p1y, p2x, p2y)
    if d > 0:
        with pushMatrix():
            translate(p1x, p1y)
            angle = atan2(p1x - p2x, p2y - p1y)
            rotate(angle + HALF_PI)
            ri = r1 - r2
            beta = asin(ri / d) + HALF_PI
            x1 = cos(beta) * r1
            y1 = sin(beta) * r1
            x2 = cos(beta) * r2
            y2 = sin(beta) * r2
            # with pushStyle():
            # noStroke()
            # beginShape()
            # vertex(-x1, -y1)
            # vertex(d - x2, -y2)
            # vertex(d, 0)
            # vertex(d - x2, +y2, 0)
            # vertex(-x1, +y1, 0)
            # vertex(0, 0, 0)
            # endShape()
            line(-x1, -y1, d - x2, -y2)
            line(-x1, +y1, d - x2, +y2)
            arc(0, 0, r1 * 2, r1 * 2,
                -beta - PI, beta - PI)
            arc(d, 0, r2 * 2, r2 * 2,
                beta - PI, PI - beta)
    else:
        ellipse(p1x, p1y, r1 * 2, r1 * 2)
        ellipse(p2y, p2x, r2 * 2, r2 * 2)


def poly_rounded(P, r0, r1=None, r2=None):
    """ based on code by Introscopia"""
    r1 = r0 if not r1 else r1
    r2 = r0 if not r2 else r2
    a = [0] * 3
    d, d1, d2 = 2 * r0, 2 * r1, 2 * r2

    a[0] = atan2(P[1].y - P[0].y, P[1].x - P[0].x) - HALF_PI
    a[1] = atan2(P[2].y - P[1].y, P[2].x - P[1].x) - HALF_PI
    a[2] = atan2(P[0].y - P[2].y, P[0].x - P[2].x) - HALF_PI

    start = a[2] if a[2] < a[0] else a[2] - TWO_PI
    arc(P[0].x, P[0].y, d, d, start, a[0])
    start = a[0] if a[0] < a[1] else a[0] - TWO_PI
    arc(P[1].x, P[1].y, d1, d1, start, a[1])
    start = a[1] if a[1] < a[2] else a[1] - TWO_PI
    arc(P[2].x, P[2].y, d2, d2, start, a[2])

    p01 = PVector(P[0].x + r0 * cos(a[0]), P[0].y + r0 * sin(a[0]))
    p10 = PVector(P[1].x + r1 * cos(a[0]), P[1].y + r1 * sin(a[0]))
    p12 = PVector(P[1].x + r1 * cos(a[1]), P[1].y + r1 * sin(a[1]))
    p21 = PVector(P[2].x + r2 * cos(a[1]), P[2].y + r2 * sin(a[1]))
    p20 = PVector(P[2].x + r2 * cos(a[2]), P[2].y + r2 * sin(a[2]))
    p02 = PVector(P[0].x + r0 * cos(a[2]), P[0].y + r0 * sin(a[2]))

    with pushStyle():
        noStroke()
        with beginClosedShape():
            vertex(P[0].x, P[0].y)
            vertex(p02.x, p02.y)
            vertex(p20.x, p20.y)
            vertex(P[2].x, P[2].y)
            vertex(p21.x, p21.y)
            vertex(p12.x, p12.y)
            vertex(P[1].x, P[1].y)
            vertex(p10.x, p10.y)
            vertex(p01.x, p01.y)

    line(p01.x, p01.y, p10.x, p10.y)
    line(p12.x, p12.y, p21.x, p21.y)
    line(p20.x, p20.y, p02.x, p02.y)


def poly_rounded2(p_list, r_list):
    for p0, p1, p2, r in zip(p_list,
                             [p_list[-1]] + p_list[:-1],
                             [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                             [r_list[-1]] + r_list[:-1]
                             ):
        m0 = (PVector(p0.x, p0.y) + PVector(p2.x, p2.y)) / 2
        m1 = (PVector(p0.x, p0.y) + PVector(p1.x, p1.y)) / 2
        m2 = (PVector(p2.x, p2.y) + PVector(p1.x, p1.y)) / 2
        with pushStyle():
            noStroke()
            beginShape()
            vertex(m0.x, m0.y)
            vertex(m1.x, m1.y)
            vertex(m2.x, m2.y)
            endShape(CLOSE)
    for p0, p1, p2, r in zip(p_list,
                             [p_list[-1]] + p_list[:-1],
                             [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                             [r_list[-1]] + r_list[:-1]
                             ):
        m1 = (PVector(p0.x, p0.y) + PVector(p1.x, p1.y)) / 2
        m2 = (PVector(p2.x, p2.y) + PVector(p1.x, p1.y)) / 2
        roundedCorner(p1, m1, m2, r)


def roundedCorner(pc, p1, p2, r):
    """
    Based on Stackoverflow C# rounded corner post 
    https://stackoverflow.com/questions/24771828/algorithm-for-creating-rounded-corners-in-a-polygon
    """
     # Vector 1
    dx1 = pc.x - p1.x
    dy1 = pc.y - p1.y

    # Vector 2
    dx2 = pc.x - p2.x
    dy2 = pc.y - p2.y

    # Angle between vector 1 and vector 2 divided by 2
    angle = (atan2(dy1, dx1) - atan2(dy2, dx2)) / 2

    # The length of segment between angular point and the
    # points of intersection with the circle of a given radius
    tng = abs(tan(angle))
    segment = r / tng if tng != 0 else r

    # Check the segment
    length1 = GetLength(dx1, dy1)
    length2 = GetLength(dx2, dy2)

    min_len = min(length1, length2)

    if segment > min_len:
        segment = min_len
        max_r = min_len * abs(tan(angle))
    else:
        max_r = r

    # Points of intersection are calculated by the proportion between
    # the coordinates of the vector, length of vector and the length of the
    # segment.
    p1Cross = GetProportionPoint(pc, segment, length1, dx1, dy1)
    p2Cross = GetProportionPoint(pc, segment, length2, dx2, dy2)

    # Calculation of the coordinates of the circle
    # center by the addition of angular vectors.
    dx = pc.x * 2 - p1Cross.x - p2Cross.x
    dy = pc.y * 2 - p1Cross.y - p2Cross.y

    L = GetLength(dx, dy)
    d = GetLength(segment, max_r)

    circlePoint = GetProportionPoint(pc, d, L, dx, dy)

    # StartAngle and EndAngle of arc
    startAngle = atan2(p1Cross.y - circlePoint.y, p1Cross.x - circlePoint.x)
    endAngle = atan2(p2Cross.y - circlePoint.y, p2Cross.x - circlePoint.x)

    # Sweep angle
    sweepAngle = endAngle - startAngle

    # Some additional checks
    if sweepAngle < 0:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = -sweepAngle

    if sweepAngle > PI:
        startAngle, endAngle = endAngle, startAngle
        sweepAngle = TWO_PI - sweepAngle

    # Draw result using graphics
    # noStroke()
    with pushStyle():
        noStroke()
        beginShape()
        vertex(p1.x, p1.y)
        vertex(p1Cross.x, p1Cross.y)
        vertex(p2Cross.x, p2Cross.y)
        vertex(p2.x, p2.y)
        endShape(CLOSE)

    line(p1.x, p1.y, p1Cross.x, p1Cross.y)
    line(p2.x, p2.y, p2Cross.x, p2Cross.y)
    arc(circlePoint.x, circlePoint.y, 2 * max_r, 2 * max_r,
        startAngle, startAngle + sweepAngle)
    # fill(0, 0, 100)
    # text(str(int(r)) + "  " + str(int(max_r)),
    #      circlePoint.x, circlePoint.y)
    # return (p1Cross, circlePoint, p2Cross)

def GetLength(dx, dy):
    return sqrt(dx * dx + dy * dy)


def GetProportionPoint(pt, segment, L, dx, dy):
    # factor = segment / L if L != 0 else 0
    factor = float(segment) / L if L != 0 else segment
    return PVector(
        (pt.x - dx * factor),

        (pt.y - dy * factor))
