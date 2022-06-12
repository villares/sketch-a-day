# these are unnecessary if using villares.arc.py module
DEBUG = False
beginShape = begin_shape
endShape = end_shape
bezierVertex = bezier_vertex
textSize = text_size

def setup():
    size(600, 600)
    
def draw():
    background(100, 150, 100)
    input_points = ((100, 100),  (500, 200), (200, 500), (mouse_x, mouse_y))
    stroke_weight(1)
    arc_filleted_poly(input_points, radius=50) 
    output_points = arc_filleted_poly(input_points,
                                      radius=50,
                                      arc_func=arc_pts,
                                      num_points=5) 
    stroke_weight(5)
    points(output_points)
    
def arc_filleted_poly(p_list, r_list=None, **kwargs):
    """
    Draws a 'filleted' polygon with variable radius, depends on arc_corner()

    2020-09-24 Rewritten from poly_rounded2 to be a continous PShape 
    2020-09-27 Moved default args to kwargs, added kwargs support for custom arc_func
    2020-11-10 Moving vertex_func=vertex inside body to make this more compatible with pyp5js
    2020-11-11 Removing use of PVector to improve compatibility with pyp5js
    2022-03-13 Allows a radius keyword argument to be used when no r_list is suplied
    2022-06-11 Refactoring and preparing a non-drawing version.
    """
    arc_func = kwargs.pop('arc_func', b_arc)  # draws with bezier aprox. arc by default
    open_poly = kwargs.pop('open_poly', False)  # assumes a closed poly by default
    if r_list is None:
        r_list = [kwargs.pop('radius', 0)] * len(p_list)
    p_list, r_list = list(p_list), list(r_list)
    draw_shape = True if arc_func != arc_pts else False
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
    # if draw shape:
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
    if arc_func == arc_pts:
        return arc_func(arc_center[0], arc_center[1], 2 * max_r, 2 * max_r,
                        start_angle, start_angle + sweep_angle, **kwargs)
    # else, draw "naked" arc (without beginShape & endShape)
    arc_func(arc_center[0], arc_center[1], 2 * max_r, 2 * max_r,
             start_angle, start_angle + sweep_angle, mode=2, **kwargs)

def arc_pts(cx, cy, w, h, start_angle, end_angle, num_points=24):
    """
    Returns points approximating an arc using the same
    signature as the original Processing arc().
    """
    sweep_angle = end_angle - start_angle
    if abs(sweep_angle) < 0.0001:
        vx = cx + cos(start_angle) * w / 2.0
        vy = cy + sin(start_angle) * h / 2.0
        return [(vx, vy)]
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