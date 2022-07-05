# -*- coding: utf-8 -*-
"""
From https://github.com/villares/villares/blob/main/arcs.py

2020-09-22 Merges/renames several versions of the arc related functions
2020-09-24 Updates arc_filleted_poly and arc_augmented_poly
2020-09-25 Added bar() and var_bar()
2020-09-26 Moved code from bar() to var_bar() and added several new kwargs
2020-09-27 Revising arc_filleted_poly, added kwargs. Revised circle_arc and related functions
2020-11    Improving compatibility with pyp5js, not using PVector anymore
2021-07-26 Added auto-flip option to arc_augmented_poly
2022-03-02 Make it work with py5
2022-03-13 On arc_filleted_poly, add radius keyword argument to be used.
2022-06-10 Added arc_pts() & var_bar_pts(). Also some p_arc and var_bar clean up.
2022-06-11 Fixing arc_pts bug. Making arc_filleted_poly return points with arc_pts
           Added a radius keywarg to arc_augmented_poly, and a py5 compatibilty fix.
2022_06_13 Attempt at arc_augmented_points(), changing some behaviour of arc_augmente_poly()
2022_07_03 Adding alternative resolution control to arc_pts (@introscopia's suggestion)
"""

from warnings import warn

try:
    from line_geometry import is_poly_self_intersecting, triangle_area
except ModuleNotFoundError:
    from villares.line_geometry import is_poly_self_intersecting, triangle_area

# The following block makes this compatible with py5.ixora.io
try:
    EPSILON
    remap = map
except NameError:
    from py5 import *
    beginShape = begin_shape
    endShape = end_shape
    bezierVertex = bezier_vertex
    textSize = text_size
    
DEBUG, TEXT_HEIGHT = False, 12  # For debug

# For use with half_circle and quarter_circle functions
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
            BOTTOM + LEFT: HALF_PI,
            TOP + LEFT: PI,
            TOP + RIGHT: PI + HALF_PI,
            }

def circle_arc(x, y, radius, start_ang, sweep_ang, *args, **kwargs):
    arc_func = kwargs.pop('arc_func', arc)
    arc_func(x, y, radius * 2, radius * 2, start_ang,
             start_ang + sweep_ang, *args, **kwargs)

def quarter_circle(x, y, radius, quadrant, *args, **kwargs):
    circle_arc(x, y, radius, ROTATION[quadrant], HALF_PI, *args, **kwargs)

def half_circle(x, y, radius, quadrant, *args, **kwargs):
    circle_arc(x, y, radius, ROTATION[quadrant], PI, *args, **kwargs)

def b_circle_arc(x, y, radius, start_ang, sweep_ang, mode=0):
    b_arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang,
          mode=mode)

def b_arc(cx, cy, w, h, start_angle, end_angle, mode=0):
    """
    Draw a bezier approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc, using beginShape() and endShape()
          1 "middle" used in recursive call of smaller arcs
          2 "naked" like normal, but without beginShape() and
             endShape() for use inside a larger PShape.
    """
    # Based on ideas from Richard DeVeneza via code by Golan Levin:
    # http://www.flong.com/blog/2009/bezier-approximation-of-a-circular-arc-in-processing/
    theta = end_angle - start_angle
    # Compute raw Bezier coordinates.
    if mode != 1 or abs(theta) < HALF_PI:
        x0 = cos(theta / 2.0)
        y0 = sin(theta / 2.0)
        x3 = x0
        y3 = 0 - y0
        x1 = (4.0 - x0) / 3.0
        y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0) if y0 != 0 else 0
        x2 = x1
        y2 = 0 - y1
        # Compute rotationally-offset Bezier coordinates, using:
        # x' = cos(angle) * x - sin(angle) * y
        # y' = sin(angle) * x + cos(angle) * y
        bezAng = start_angle + theta / 2.0
        cBezAng = cos(bezAng)
        sBezAng = sin(bezAng)
        rx0 = cBezAng * x0 - sBezAng * y0
        ry0 = sBezAng * x0 + cBezAng * y0
        rx1 = cBezAng * x1 - sBezAng * y1
        ry1 = sBezAng * x1 + cBezAng * y1
        rx2 = cBezAng * x2 - sBezAng * y2
        ry2 = sBezAng * x2 + cBezAng * y2
        rx3 = cBezAng * x3 - sBezAng * y3
        ry3 = sBezAng * x3 + cBezAng * y3
        # Compute scaled and translated Bezier coordinates.
        rx, ry = w / 2.0, h / 2.0
        px0 = cx + rx * rx0
        py0 = cy + ry * ry0
        px1 = cx + rx * rx1
        py1 = cy + ry * ry1
        px2 = cx + rx * rx2
        py2 = cy + ry * ry2
        px3 = cx + rx * rx3
        py3 = cy + ry * ry3
        if DEBUG:
            ellipse(px3, py3, 3, 3)
            ellipse(px0, py0, 5, 5)
    # Drawing
    if mode == 0:  # 'normal' arc (not 'middle' nor 'naked')
        beginShape()
    if mode != 1:  # if not 'middle'
        vertex(px3, py3)
    if abs(theta) < HALF_PI:
        bezierVertex(px2, py2, px1, py1, px0, py0)
    else:
        # to avoid distortion, break into 2 smaller arcs
        b_arc(cx, cy, w, h, start_angle, end_angle - theta / 2.0, mode=1)
        b_arc(cx, cy, w, h, start_angle + theta / 2.0, end_angle, mode=1)
    if mode == 0:  # end of a 'normal' arc
        endShape()

def p_circle_arc(x, y, radius, start_ang, sweep_ang, mode=0, **kwargs):
    p_arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang,
          mode=mode, **kwargs)

def circle_arc_pts(x, y, radius, start_ang, sweep_ang, **kwargs):
    arc_pts(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang,
              **kwargs)

def p_arc(cx, cy, w, h, start_angle, end_angle, mode=0,
          num_points=24, vertex_func=None):
    """
    A poly approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc-like, using beginShape() and endShape()
          1 "middle" not implemented on p_arc, used on recursive b_arc 
          2 "naked" like normal, but without beginShape() and
             endShape() for use inside a larger PShape.
    """
    vertex_func = vertex_func or vertex
    if mode == 0:
        beginShape()
    vertex_pts = arc_pts(cx, cy, w, h, start_angle, end_angle, num_points)
    for vx, vy in vertex_pts:
        vertex_func(vx, vy)
    if mode == 0:
        endShape()

def arc_pts(cx, cy, w, h, start_angle, end_angle, num_points=None, seg_len=None):
    """
    Returns points approximating an arc using the same
    signature as the original Processing arc().
    """
    sweep_angle = end_angle - start_angle
    if abs(sweep_angle) < 0.0001:
        vx = cx + cos(start_angle) * w / 2.0
        vy = cy + sin(start_angle) * h / 2.0
        return [(vx, vy)]
    if num_points is None and seg_len is None:
        num_points = 24
    elif num_points is None:
        num_points = abs(sweep_angle * (w + h) / 4) / seg_len
    pts_list = []
    step_angle = float(sweep_angle) / num_points    
    va = start_angle
    side = 1 if sweep_angle > 0 else -1
    while va * side < end_angle * side or abs(va - end_angle) < 0.0001:
        vx = cx + cos(va) * w / 2.0
        vy = cy + sin(va) * h / 2.0
        pts_list.append((vx, vy))
        va += step_angle
    return pts_list

def arc_filleted_poly(p_list, r_list=None, **kwargs):
    """
    Draws a 'filleted' polygon with variable radius, depends on arc_corner()

    2020-09-24 Rewritten from poly_rounded2 to be a continous PShape 
    2020-09-27 Moved default args to kwargs, added kwargs support for custom arc_func
    2020-11-10 Moving vertex_func=vertex inside body to make this more compatible with pyp5js
    2020-11-11 Removing use of PVector to improve compatibility with pyp5js
    2022-03-13 Allows a radius keyword argument to be used when no r_list is suplied
    2022-06-11 Refactoring and added arc_pts non-drawing feature that returns points.
    """
    arc_func = kwargs.pop('arc_func', b_arc)  # draws with bezier aprox. arc by default
    open_poly = kwargs.pop('open_poly', False)  # assumes a closed poly by default
    assert p_list, 'No points were provided.'
    assert not ('radius' in kwargs and r_list),\
           "You can't use a radii list and a radius kwarg together."
    if r_list is None:
        r_list = [kwargs.pop('radius', 0)] * len(p_list)
    p_list, r_list = list(p_list), list(r_list)
    draw_shape = False if arc_func == arc_pts else True
    
    def mid(p0, p1):
        return (p0[0] + p1[0]) * 0.5, (p0[1] + p1[1]) * 0.5
    
    if open_poly:
        p0_p1_p2_r_sequence = zip(p_list[:-1],
            [p_list[-1]] + p_list[:-2],
            [p_list[-2]] + [p_list[-1]] + p_list[:-3],
            [r_list[-1]] + r_list[:-2])
    else:
        p0_p1_p2_r_sequence = zip(p_list,
            [p_list[-1]] + p_list[:-1],
            [p_list[-2]] + [p_list[-1]] + p_list[:-2],
            [r_list[-1]] + r_list[:-1])
    if draw_shape:
        beginShape()
        for p0, p1, p2, r in p0_p1_p2_r_sequence:
            arc_corner(p1, mid(p0, p1), mid(p1, p2), r,
                       arc_func=arc_func, **kwargs)
    else:
        pts_list = []
        for p0, p1, p2, r in p0_p1_p2_r_sequence:
            pts_list.extend(arc_corner(p1, mid(p0, p1), mid(p1, p2), r,
                                       arc_func=arc_func, **kwargs))
        return pts_list
    # then, if draw_shape:
    if open_poly:
        endShape()       
    else:
        endShape(CLOSE)

def arc_corner(pc, p1, p2, r, **kwargs):
    """
    Draw an arc that 'rounds' the point pc between p1 and p2 using arc_func
    Based on '...rounded corners in a polygon' from https://stackoverflow.com/questions/24771828/
    2020-09-27 Added support for custom arc_func & kwargs
    2020-11-11 Avoiding the use of PVector
    2022-06-11 Now returns the result of arc_pts
    """
    arc_func = kwargs.pop('arc_func', b_arc)  # draws with bezier aprox. arc by default

    def proportion_point(pt, segment, L, dx, dy):
        factor = float(segment) / L if L != 0 else segment
        return (pt[0] - dx * factor), (pt[1] - dy * factor)

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
    dx = pc[0] * 2 - p1Cross[0] - p2Cross[0]
    dy = pc[1] * 2 - p1Cross[1] - p2Cross[1]
    L = sqrt(dx * dx + dy * dy)
    d = sqrt(segment * segment + max_r * max_r)
    arc_center = proportion_point(pc, d, L, dx, dy)
    # start_angle and end_angle of arc
    start_angle = atan2(p1Cross[1] - arc_center[1], p1Cross[0] - arc_center[0])
    end_angle = atan2(p2Cross[1] - arc_center[1], p2Cross[0] - arc_center[0])
    # Sweep angle
    sweep_angle = end_angle - start_angle
    # Some additional checks
    nsa = False  # negative sweep angle
    if sweep_angle < 0:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
        nsa = True
        if DEBUG:
            circle(arc_center[0], arc_center[1], max_r / 2)
    lsa = False  # large sweep angle
    if sweep_angle > PI:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = TWO_PI - sweep_angle
        lsa = True
        if DEBUG:
            circle(arc_center[0], arc_center[1], max_r)
    if (lsa and nsa) or (not lsa and not nsa):
        # reverse sweep direction
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
    if arc_func == arc_pts:
        return arc_pts(arc_center[0], arc_center[1], 2 * max_r, 2 * max_r,
                        start_angle, start_angle + sweep_angle, **kwargs)
    # else, draw "naked" arc (without beginShape & endShape)
    arc_func(arc_center[0], arc_center[1], 2 * max_r, 2 * max_r,
             start_angle, start_angle + sweep_angle, mode=2, **kwargs)


def arc_augmented_poly(op_list, or_list=None, **kwargs):
    """
    Draw a continous PShape "Polyline" as if around pins of various diameters.
    Has an ugly check_intersection mode that does not draw and "roughly" checks
    for self intersections using slow polygon aproximations.
    2020-09-22 Renamed from b_poly_arc_augmented 
    2020-09-24 Removed Bezier mode in favour of arc_func + any keyword arguments.
    2020-09-26 Moved arc_func to kwargs, updates exceptions
    2021-07-26 Added auto-flip switch/option (when concave vertex radius = -radius)
    2022-06-11 Added remap py5 compatibility alias & radius kwarg for or_list=None
    2022-06-14 Connected to arc_augmented_points. Added reduce_both kwarg.
    """
    arc_func = kwargs.pop('arc_func', b_arc)
    if arc_func == arc_pts:
        return arc_augmented_points(op_list, or_list, **kwargs)
    
    assert op_list, 'No points were provided.'
    assert not ('radius' in kwargs and or_list),\
           "You can't use a radii list and a radius kwarg together."
    if 'radius' in kwargs and or_list == None:
        or_list = [kwargs.pop('radius')] * len(op_list)
    r2_list = list(or_list)
    assert len(op_list) == len(r2_list),\
        'Number of points and radii provided not the same.'
    check_intersection = kwargs.pop('check_intersection', False)

    auto_flip = kwargs.pop('auto_flip', True)
    gradual_flip = kwargs.pop('gradual_flip', False)
    reduce_both = kwargs.pop('reduce_both', True)
    if check_intersection and arc_func:
        warn("check_intersection mode overrides arc_func (arc_func ignored).")
    if check_intersection:
        global _points, vertex_func
        _points = []
        vertex_func = lambda x, y: _points.append((x, y))
        arc_func = p_arc
        kwargs = {"num_points": 4, "vertex_func": vertex_func}
    else:
        vertex_func = vertex
    # remove overlapping adjacent points
    p_list, r_list = [], []
    for i1, p1 in enumerate(op_list):
        i2 = (i1 - 1)
        p2, r2, r1 = op_list[i2], r2_list[i2], r2_list[i1]
        if dist(p1[0], p1[1], p2[0], p2[1]) > 1:  # or p1 != p2:
            p_list.append(p1)
            r_list.append(r1)
        else:
            r2_list[i2] = min(r1, r2)
    # invert radius
    for i1, p1 in enumerate(p_list):
        i0 = (i1 - 1)
        p0 = p_list[i0]
        i2 = (i1 + 1) % len(p_list)
        p2 = p_list[i2]
        a = triangle_area(p0, p1, p2) / 1000.
        if auto_flip and a < 0:
            r_list[i1] = -r_list[i1]
            if gradual_flip:
                r_list[i1] = r_list[i1] * min(1, abs(a))
    # reduce radius that won't fit
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 = p_list[i2], r_list[i2], r_list[i1]
        r_list[i1], r_list[i2] = reduce_radius(p1, p2, r1, r2,
                                               reduce_both=reduce_both)
    # calculate the tangents
    a_list = []
    for i1, p1 in enumerate(p_list):
        i2 = (i1 + 1) % len(p_list)
        p2, r2, r1 = p_list[i2], r_list[i2], r_list[i1]
        cct = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(cct)
    # check basic "skeleton poly" intersection (whithout the p_arc aprox.)
    if check_intersection:
        skeleton_points = []
        for ang, p1, p2 in a_list:
            skeleton_points.append(p1)
            skeleton_points.append(p2)
        if is_poly_self_intersecting(skeleton_points):
            return True
    # now draw it!
    beginShape()
    for i1, ia in enumerate(a_list):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a1, p11, p12 = ia
        a2, p21, p22 = a_list[i2]
        if DEBUG:
            circle(p1[0], p1[1], 10)
        if a1 != None and a2 != None:
            start = a1 if a1 < a2 else a1 - TWO_PI
            if r2 <= 0:
                a2 = a2 - TWO_PI
            abs_angle = abs(a2 - start)
            if abs_angle > TWO_PI:
                if a2 < 0:
                    a2 += TWO_PI
                else:
                    a2 -= TWO_PI
            if abs(a2 - start) != TWO_PI:
                arc_func(p2[0], p2[1], r2 * 2, r2 * 2, start, a2, mode=2,
                         **kwargs)
            if DEBUG:
                textSize(TEXT_HEIGHT)
                text(str(int(degrees(start - a2))), p2[0], p2[1])
        else:
            # when the the segment is smaller than the diference between
            # radius, circ_circ_tangent won't renturn the angle
            if DEBUG:
                ellipse(p2[0], p2[1], r2 * 2, r2 * 2)
            if a1:
                vertex_func(p12[0], p12[1])
            if a2:
                vertex_func(p21[0], p21[1])
    endShape(CLOSE)
    # check augmented poly aproximation instersection
    if check_intersection:
        return is_poly_self_intersecting(_points)

def arc_augmented_points(op_list, or_list=None, **kwargs):
    """
    A version of arc_augmented_poly that returns the points
    of a poly-approximation with arc_pts
    """
    
    def mid(p0, p1):
        return (p0[0] + p1[0]) * 0.5, (p0[1] + p1[1]) * 0.5
    
    assert op_list, 'No points were provided.'
    assert not ('radius' in kwargs and or_list),\
        "You can't use a radii list and a radius kwarg together."
    if 'radius' in kwargs and or_list == None:
        or_list = [kwargs.pop('radius')] * len(op_list)
    r2_list = list(or_list)
    assert len(op_list) == len(r2_list),\
        'Number of points and radii provided not the same.'
    auto_flip = kwargs.pop('auto_flip', True)
    gradual_flip = kwargs.pop('gradual_flip', False)  # experimentas    
    pts_list = []
    # remove overlapping adjacent points
    p_list, r_list = [], []
    p2_list = list(op_list)
    for i1, p1 in enumerate(p2_list):
        i2 = (i1 + 1) % len(p2_list)
        p2, r2, r1 = p2_list[i2], r2_list[i2], r2_list[i1]
        d = dist(p1[0], p1[1], p2[0], p2[1])
        if d > abs(r1 - r2):
            p_list.append(p1)
            r_list.append(r1)
        else:
            p2_list[i2] = mid(p1, p2)
            r2_list[i2] = max(r1, r2)
    # invert radius
    for i1, p1 in enumerate(p_list):
        i0 = (i1 - 1)
        p0 = p_list[i0]
        i2 = (i1 + 1) % len(p_list)
        p2 = p_list[i2]
        a = triangle_area(p0, p1, p2) / 1000
        if auto_flip and a < 0:
            r_list[i1] = -r_list[i1]
            if gradual_flip:
                r_list[i1] = r_list[i1] * min(1, abs(a))
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
        cct = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(cct)
    # now draw it!
    for i1, ia in enumerate(a_list):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a1, p11, p12 = ia
        a2, p21, p22 = a_list[i2]
        if DEBUG:
            circle(p1[0], p1[1], r1 * 2)
        if a1 != None and a2 != None:
            start = a1 if a1 < a2 else a1 - TWO_PI # was <
            if r2 < 0:  # was <=
                a2 = a2 - TWO_PI
            abs_angle = abs(a2 - start)
            if abs_angle > TWO_PI:
                if a2 < 0:
                    a2 += TWO_PI
                else:
                    a2 -= TWO_PI
            if abs(a2 - start) != TWO_PI:
                pts_list.extend(arc_pts(p2[0], p2[1], r2 * 2, r2 * 2, start, a2,
                                        **kwargs))
            if DEBUG:
                textSize(TEXT_HEIGHT)
                text(' {:0.2f} {:0.2f}'.format(r2, degrees(abs_angle)), p2[0], p2[1])
        else:
            # when the the segment is smaller than the diference between
            # radius, circ_circ_tangent won't renturn the angle
            if DEBUG:
                ellipse(p2[0], p2[1], r1, r1)
            if a1:
                pts_list.append((p12[0], p12[1]))
            if a2:
                pts_list.append((p21[0], p21[1]))
    return pts_list

def reduce_radius(p1, p2, r1, r2, reduce_both=True):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = abs(r1 - r2)
    if d - ri <= 0:
        if reduce_both:
           r1, r2 = (remap(d, ri + 1, 0, r1, (r1 + r2) / 2),
                     remap(d, ri + 1, 0, r2, (r1 + r2) / 2))
        elif abs(r1) > abs(r2):
            r1 = remap(d, ri + 1, 0, r1, r2)
        else:
            r2 = remap(d, ri + 1, 0, r2, r1)
    return r1, r2

def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = r1 - r2
    line_angle = atan2(p1[0] - p2[0], p2[1] - p1[1])
    if d - abs(ri) >= 0:
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

def bar(x1, y1, x2, y2, thickness, **kwargs):
    """
    Draw a thick strip with rounded ends.
    It can be shorter than the supporting (axial) line segment.

    # 2020-9-25 First rewrite attempt based on var_bar + arc_func + **kwargs
    # 2020-9-26 Let's do everything in var_bar()!
    """
    var_bar(x1, y1, x2, y2, thickness / 2, **kwargs)

def var_bar(p1x, p1y, p2x, p2y, r1, r2=None, **kwargs):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius
    
    Expected keyword arguments:
        shorter: Will draw a shorter "bar" (only if r1 == r2)
        internal: When too short draws circle from smaller radius end
                  inside circle from larger radius end (default is  True)
        arc_func: Allows choosing the arc funcio, like p_arc (default is b_arc)
        num_points: Will be passed to the arc_func (works with p_arc)
    
    # 2020-9-25 Added **kwargs, now one can use arc_func=p_arc & num_points=N   
    # 2020-9-26 Added treatment to shorter=N so as to incorporate bar() use.
                Added a keyword argument, internal=True is the default,
                internal=False disables drawing internal circle.
                Minor cleanups, and removed "with" for pushMatrix().
    # 2022-6-10 Removed unused variables & changed behaviour for small distances,
                when internal=False, draw a circle from the larger radius.
    """
    r2 = r2 if r2 is not None else r1
    draw_internal_circle = kwargs.pop('internal', True)
    arc_func = kwargs.pop('arc_func', b_arc)
    shorter = kwargs.pop('shorter', 0)
    assert not (shorter and r1 != r2),\
        "Can't draw shorter var_bar with different radii. r1={} r2={}".format(r1, r2)
    assert not (kwargs and arc_func == b_arc),\
        "Can't use keyword arguments with b_arc. {}".format(kwargs)
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    if d > abs(ri):
        clipped_ri_over_d = min(1, max(-1, ri / d))
        beta = asin(clipped_ri_over_d) + HALF_PI
        push()
        translate(p1x, p1y)
        angle = atan2(p1x - p2x, p2y - p1y)
        rotate(angle + HALF_PI)
        beginShape()
        offset = shorter / 2.0 if shorter < d else d / 2.0
        arc_func(offset, 0, r1 * 2, r1 * 2,
                 -beta - PI, beta - PI, mode=2, **kwargs)
        arc_func(d - offset, 0, r2 * 2, r2 * 2,
                 beta - PI, PI - beta, mode=2, **kwargs)
        endShape(CLOSE)
        pop()
    else:  # draw a circle with the bigger radius if distance is too small
        r = max(r1, r2)
        x, y = (p1x, p1y) if r1 > r2 else (p2x, p2y)
        arc_func(x, y, r * 2, r * 2, 0, TWO_PI, **kwargs)
        if draw_internal_circle:
            r = min(r1, r2)
            x, y = (p1x, p1y) if r1 < r2 else (p2x, p2y)
            arc_func(x, y, r * 2, r * 2, 0, TWO_PI, **kwargs)

def var_bar_pts(p1x, p1y, p2x, p2y, r1, r2=None, **kwargs):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius
    
    Expected keyword arguments:
        shorter: will make a shorter "bar" (only if r1 == r2)
        num_points: will be passed to arc_pts (default there is 24)
        internal: unavailable
    """
    r2 = r2 if r2 is not None else r1
    shorter = kwargs.pop('shorter', 0)
    assert not (shorter and r1 != r2),\
        "Can't draw shorter var_bar with different radii"
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    result = []
    if d > abs(ri):
        clipped_ri_over_d = min(1, max(-1, ri / d))
        beta = asin(clipped_ri_over_d) + HALF_PI
        angle = atan2(p1x - p2x, p2y - p1y) + HALF_PI
        offset = shorter / 2.0 if shorter < d else d / 2.0
        result.extend(arc_pts(offset, 0, r1 * 2, r1 * 2,
                     -beta - PI, beta - PI, **kwargs))
        result.extend(arc_pts(d - offset, 0, r2 * 2, r2 * 2,
                      beta - PI, PI - beta, **kwargs))
        return rotate_offset_points(result, angle, p1x, p1y)
    else:
        r = max(r1, r2)
        x, y = (p1x, p1y) if r1 > r2 else (p2x, p2y)
        return arc_pts(x, y, r * 2, r * 2, 0, TWO_PI, **kwargs)
                          
def rotate_offset_points(pts, angle, offx, offy, y0=0, x0=0):
    return [(((xp - x0) * cos(angle) - (yp - y0) * sin(angle)) + x0 + offx,
             ((yp - y0) * cos(angle) + (xp - x0) * sin(angle)) + y0 + offy)
            for xp, yp in pts]
