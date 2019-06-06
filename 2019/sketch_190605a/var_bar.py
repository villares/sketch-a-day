def var_bar(p1x, p1y, p2x, p2y, r1, r2=None):
    """
    Tangent/tangent shape on 2 circles of arbitrary radius
    """
    if r2 is None:
        r2 = r1
    #line(p1x, p1y, p2x, p2y)
    d = dist(p1x, p1y, p2x, p2y)
    ri = r1 - r2
    if d > abs(ri):
        rid = (r1 - r2) / d
        if rid > 1:
            rid = 1
        if rid < -1:
            rid = -1
        beta = asin(rid) + HALF_PI
        with pushMatrix():
            translate(p1x, p1y)
            angle = atan2(p1x - p2x, p2y - p1y)
            rotate(angle + HALF_PI)
            x1 = cos(beta) * r1
            y1 = sin(beta) * r1
            x2 = cos(beta) * r2
            y2 = sin(beta) * r2
            #print((d, beta, ri, x1, y1, x2, y2))
            beginShape()  
            b_arc(0, 0, r1 * 2, r1 * 2,
                -beta - PI, beta - PI, mode=2)
            b_arc(d, 0, r2 * 2, r2 * 2,
                beta - PI, PI - beta, mode=2)
            endShape(CLOSE)

    else:
        ellipse(p1x, p1y, r1 * 2, r1 * 2)
        ellipse(p2x, p2y, r2 * 2, r2 * 2)
        
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
    if mode != 1 or theta < HALF_PI:
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
    if mode == 0: # 'normal' arc (not 'middle' nor 'naked')
        beginShape()
    if mode != 1: # if not 'middle'
        vertex(px3, py3)
    if theta < HALF_PI:
        bezierVertex(px2, py2, px1, py1, px0, py0)
    else:
        # to avoid distortion, break into 2 smaller arcs
        b_arc(cx, cy, w, h, start_angle, end_angle - theta / 2.0, mode=1)
        b_arc(cx, cy, w, h, start_angle + theta / 2.0, end_angle, mode=1)
    if mode == 0: # end of a 'normal' arc
        endShape()
