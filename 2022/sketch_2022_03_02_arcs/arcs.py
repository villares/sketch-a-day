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
"""
from warnings import warn
from line_geometry import is_poly_self_intersecting, triangle_area

try:
    EPSILON
except NameError:
    from py5 import *
    beginShape = begin_shape
    endShape = end_shape
    bezierVertex = bezier_vertex
    textSize = text_size
    
    
    
TEXT_HEIGHT = 12
DEBUG = False
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
    # Based on ideas from Richard DeVeneza via code by Gola Levin:
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

def p_arc(cx, cy, w, h, start_angle, end_angle, mode=0,
          num_points=24, vertex_func=None):
    """
    A poly approximation of an arc using the same
    signature as the original Processing arc().
    mode: 0 "normal" arc, using beginShape() and endShape()
          2 "naked" like normal, but without beginShape() and
             endShape() for use inside a larger PShape.
    """
    vertex_func = vertex_func or vertex
    sweep_angle = end_angle - start_angle
    if mode == 0:
        beginShape()
    if sweep_angle < 0:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle
        angle = float(sweep_angle) / abs(num_points)
        a = end_angle
        while a >= start_angle:
            sx = cx + cos(a) * w / 2.0
            sy = cy + sin(a) * h / 2.0
            vertex_func(sx, sy)
            a -= angle
    elif sweep_angle > 0:
        angle = sweep_angle / int(num_points)
        a = start_angle
        while a <= end_angle:
            sx = cx + cos(a) * w / 2.0
            sy = cy + sin(a) * h / 2.0
            vertex_func(sx, sy)
            a += angle
    else:  # sweep_angle == 0
        sx = cx + cos(start_angle) * w / 2.0
        sy = cy + sin(start_angle) * h / 2.0
        vertex_func(sx, sy)
    if mode == 0:
        endShape()


def arc_filleted_poly(p_list, r_list, **kwargs):
    """
    Draws a 'filleted' polygon with variable radius, depends on arc_corner()

    2020-09-24 Rewritten from poly_rounded2 to be a continous PShape 
    2020-09-27 Moved default args to kwargs, added kwargs support for custom arc_func
    2020-11-10 Moving vertex_func=vertex inside body to make this more compatible with pyp5js
    2020-11-11 Removing use of PVector to improve compatibility with pyp5js
    """
    arc_func = kwargs.pop('arc_func', b_arc)  # draws with bezier aprox. arc by default
    # assumes a closed poly by default
    open_poly = kwargs.pop('open_poly', False)

    p_list, r_list = list(p_list), list(r_list)
    beginShape()
    if not open_poly:
        for p0, p1, p2, r in zip(
                p_list,
                [p_list[-1]] + p_list[:-1],
                [p_list[-2]] + [p_list[-1]] + p_list[:-2],
                [r_list[-1]] + r_list[:-1]
            ):
            m1 = ((p0[0] + p1[0]) / 2.0, (p0[1] + p1[1]) / 2.0)
            m2 = ((p2[0] + p1[0]) / 2.0, (p2[1] + p1[1]) / 2.0)
            arc_corner(p1, m1, m2, r, arc_func=arc_func, **kwargs)
        endShape(CLOSE)
    else:
        for p0, p1, p2, r in zip(
                p_list[:-1],
                [p_list[-1]] + p_list[:-2],
                [p_list[-2]] + [p_list[-1]] + p_list[:-3],
                [r_list[-1]] + r_list[:-2]
            ):
            m1 = ((p0[0] + p1[0]) / 2.0, (p0[1] + p1[1]) / 2.0)
            m2 = ((p2[0] + p1[0]) / 2.0, (p2[1] + p1[1]) / 2.0)
            arc_corner(p1, m1, m2, r, arc_func=arc_func, **kwargs)
        endShape()

def arc_corner(pc, p1, p2, r, **kwargs):
    """
    Draw an arc that 'rounds' the point pc between p1 and p2 using arc_func
    Based on '...rounded corners in a polygon' from https://stackoverflow.com/questions/24771828/
    2020-09-27 Added support for custom arc_func & kwargs
    2020-11-11 Avoiding the use of PVector
    """
    arc_func = kwargs.pop('arc_func', b_arc)  # draws with bezier aprox. arc by default

    def proportion_point(pt, segment, L, dx, dy):
        factor = float(segment) / L if L != 0 else segment
        return((pt[0] - dx * factor), (pt[1] - dy * factor))

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
    # draw "naked" arc (without beginShape & endShape)
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
    2021-07-26 auto-flip option (when concave vertex radius = -radius)
    """
    assert op_list, 'No points were provided.'
    if or_list == None:
        r2_list = [0] * len(op_list)
    else:
        r2_list = or_list[:]
    assert len(op_list) == len(r2_list),\
        'Number of points and radii provided not the same.'
    check_intersection = kwargs.pop('check_intersection', False)
    arc_func = kwargs.pop('arc_func', b_arc)
    auto_flip = kwargs.pop('auto_flip', True)
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
        if or_list == None:
            r_list[i1] = a
        else:
            # # a shrink to flip option...
            # if abs(a) < 1:
            #     r_list[i1] = r_list[i1] * abs(a)
            if a < 0 and auto_flip:
                r_list[i1] = -r_list[i1]
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

def reduce_radius(p1, p2, r1, r2):
    d = dist(p1[0], p1[1], p2[0], p2[1])
    ri = abs(r1 - r2)
    if d - ri <= 0:
        if abs(r1) > abs(r2):
            r1 = map(d, ri + 1, 0, r1, r2)
        else:
            r2 = map(d, ri + 1, 0, r2, r1)
    return(r1, r2)

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

    # 2020-9-25 Added **kwargs, now one can use arc_func=p_arc & num_points=N   
    # 2020-9-26 Added treatment to shorter=N so as to incorporate bar() use.
                Added a keyword argument, internal=True is the default,
                internal=False disables drawing internal circles.
                Minor cleanups, and removed "with" for pushMatrix().
    """
    r2 = r2 if r2 is not None else r1
    draw_internal_circles = kwargs.pop('internal', True)
    arc_func = kwargs.pop('arc_func', b_arc)
    shorter = kwargs.pop('shorter', 0)
    assert not (shorter and r1 != r2),\
        "Can't draw shorter var_bar with different radii"
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    if d > abs(ri):
        clipped_ri_over_d = min(1, max(-1, ri / d))
        beta = asin(clipped_ri_over_d) + HALF_PI
        push()
        translate(p1x, p1y)
        angle = atan2(p1x - p2x, p2y - p1y)
        rotate(angle + HALF_PI)
        x1 = cos(beta) * r1
        y1 = sin(beta) * r1
        x2 = cos(beta) * r2
        y2 = sin(beta) * r2
        beginShape()
        offset = shorter / 2.0 if shorter < d else d / 2.0
        arc_func(offset, 0, r1 * 2, r1 * 2,
                 -beta - PI, beta - PI, mode=2, **kwargs)
        arc_func(d - offset, 0, r2 * 2, r2 * 2,
                 beta - PI, PI - beta, mode=2, **kwargs)
        endShape(CLOSE)
        pop()
    elif draw_internal_circles:
        arc_func(p1x, p1y, r1 * 2, r1 * 2, 0, TWO_PI, **kwargs)
        arc_func(p2x, p2y, r2 * 2, r2 * 2, 0, TWO_PI, **kwargs)
