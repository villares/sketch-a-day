def b_poly_arc_augmented(op_list, or_list=None, check_intersection=False):
    if not op_list: return
    if or_list == None:
        r2_list = [0] * len(op_list)
    else:
        r2_list = or_list[:]
    assert len(op_list) == len(r2_list), \
        "Number of points and radii not the same"
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
        a = area(p0, p1, p2) / 1000.
        if or_list == None:
            r_list[i1] = a
        else:
            # if abs(a) < 1:
            #     r_list[i1] = r_list[i1] * abs(a)
            if a <= 0:
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
        a = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(a)
    # draw
    beginShape()
    for i1, ia in enumerate(a_list):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a1, p11, p12 = ia
        a2, p21, p22 = a_list[i2]
        circle(p1[0], p1[1], 10, 10)
        if a1 != None and a2 != None:
            start = a1 if a1 < a2 else a1 - TWO_PI
            if r2 < 0:
                a2 = a2 - TWO_PI
            b_arc(p2[0], p2[1], r2 * 2, r2 * 2, start, a2, mode=2)
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

def b_arc(cx, cy, w, h, start_angle, end_angle, mode=0):
    """
    A bezier approximation of an arc
    using the same signature as the original Processing arc()
    mode: 0 "normal" arc, using beginShape() and endShape()
              1 "middle" used in recursive call of smaller arcs
              2 "naked" like normal, but without beginShape() and endShape()
                 for use inside a larger PShape
    """
    theta = end_angle - start_angle
    # Compute raw Bezier coordinates.
    if mode != 1 or abs(theta) < HALF_PI:
        x0 = cos(theta / 2.0)
        y0 = sin(theta / 2.0)
        x3 = x0
        y3 = 0 - y0
        x1 = (4.0 - x0) / 3.0
        if y0 != 0:
            y1 = ((1.0 - x0) * (3.0 - x0)) / (3.0 * y0)  # y0 != 0...
        else:
            y1 = 0
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
        # Debug points... comment this out!
        # stroke(0)
        # ellipse(px3, py3, 15, 15)
        # ellipse(px0, py0, 5, 5)
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

def area(p0, p1, p2):
    a = (p1[0] * (p2[1] - p0[1]) +
         p2[0] * (p0[1] - p1[1]) +
         p0[0] * (p1[1] - p2[1]))
    return a
