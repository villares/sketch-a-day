# -*- coding: UTF-8 -*-
from villares.arcs import p_arc, b_arc

DEBUG = True

def arc_filleted_poly(p_list,
                      r_list,
                      open_poly=False,
                      arc_func=p_arc):
    """
    Draws a 'filleted' polygon with variable radius, depends on arc_corner()
    2020-09-24 Rewritten from poly_rounded2 to be a continous PShape 
    """
    p_list, r_list = list(p_list), list(r_list)
    beginShape()
    if not open_poly:
        for p0, p1, p2, r in zip(p_list,
                                 [p_list[-1]] + p_list[:-1],
                                 [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                                 [r_list[-1]] + r_list[:-1]
                                 ):
            m1 = (PVector(p0[0], p0[1]) + PVector(p1[0], p1[1])) / 2
            m2 = (PVector(p2[0], p2[1]) + PVector(p1[0], p1[1])) / 2
            arc_corner(p1, m1, m2, r, arc_func)
        endShape(CLOSE)
    else:
        for p0, p1, p2, r in zip(p_list[:-1],
                                 [p_list[-1]] + p_list[:-2],
                                 [p_list[-2]] + [p_list[-1]] + p_list[:-3],
                                 [r_list[-1]] + r_list[:-2]
                                 ):
            m1 = (PVector(p0[0], p0[1]) + PVector(p1[0], p1[1])) / 2
            m2 = (PVector(p2[0], p2[1]) + PVector(p1[0], p1[1])) / 2
            arc_corner(p1, m1, m2, r, arc_func)
        endShape()

def arc_corner(pc, p1, p2, r, arc_func=b_arc):
    """
    Draw an arc that 'rounds' the point pc between p1 and p2 using arc_func
    Based on '...rounded corners in a polygon' from https://stackoverflow.com/questions/24771828/
    """
    def proportion_point(pt, segment, L, dx, dy):
        factor = float(segment) / L if L != 0 else segment
        return PVector((pt[0] - dx * factor), (pt[1] - dy * factor))

    # Vectors 1 and 2
    dx1, dy1 = pc[0] - p1[0], pc[1] - p1[1]
    dx2, dy2 = pc[0] - p2[0], pc[1] - p2[1]
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
    p1Cross = proportion_point(pc, segment, length1, dx1, dy1)
    p2Cross = proportion_point(pc, segment, length2, dx2, dy2)
    # Calculation of the coordinates of the circle
    # center by the addition of angular vectors.
    dx = pc[0] * 2 - p1Cross.x - p2Cross.x
    dy = pc[1] * 2 - p1Cross.y - p2Cross.y
    L = sqrt(dx * dx + dy * dy)
    d = sqrt(segment * segment + max_r * max_r)
    arc_center = proportion_point(pc, d, L, dx, dy)
    # start_angle and end_angle of arc
    start_angle = atan2(p1Cross.y - arc_center.y, p1Cross.x - arc_center.x)
    end_angle = atan2(p2Cross.y - arc_center.y, p2Cross.x - arc_center.x)
    # Sweep angle
    sweep_angle = end_angle - start_angle
    # Some additional checks
    nsa = False  # negative sweep angle
    if sweep_angle < 0:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
        nsa = True
        if DEBUG:
            circle(arc_center.x, arc_center.y, max_r / 2)
    lsa = False  # large sweep angle
    if sweep_angle > PI:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = TWO_PI - sweep_angle
        lsa = True
        if DEBUG:
            circle(arc_center.x, arc_center.y, max_r)
    if (lsa and nsa) or (not lsa and not nsa):
        # reverse sweep direction
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
    # draw "naked" arc (without beginShape & endShape)
    arc_func(arc_center.x, arc_center.y, 2 * max_r, 2 * max_r,
             start_angle, start_angle + sweep_angle, mode=2)
