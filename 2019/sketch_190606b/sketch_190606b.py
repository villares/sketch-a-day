from pytop5js import *

pts = [(100, 100), (110, 400), (400, 400)]
rds = [40, 40, 40, 30, 70, 50]
dragged_pt = -1

def setup():
    createCanvas(500, 500)
    pts.append((250, 150))

    pts.append((250 + 100 * cos(PI / 6.0),
                250 + 100 * sin(PI / 6.0)))
    pts.append((250 - 100 * cos(PI / 6.0),
                250 + 100 * sin(PI / 6.0)))

def draw():
    background(200)
    fill(255, 100)
    b_poly_arc_augmented(pts, rds)
    fill(0, 0, 100)
    for pt in pts:
        ellipse(pt[0], pt[1], 10, 10)


def keyPressed():
    global r, d
    delta = 0
    if key == "-":
    	delta = -1
    elif key == "=" or key == "+":
    	delta = 1
    for i, pt in enumerate(pts):
        if dist(mouseX, mouseY, pt[0], pt[1]) < 10:
            rds[i] += 5 * delta
    return False

def mousePressed():
    global dragged_pt
    for i, pt in enumerate(pts):
        if dist(mouseX, mouseY, pt[0], pt[1]) < 10:
            dragged_pt = i
            break

def mouseDragged():
    if dragged_pt >= 0:
        pts[dragged_pt] = mouseX, mouseY

def mouseReleased():
    global dragged_pt
    dragged_pt = -1

def b_poly_arc_augmented(op_list, or_list):
    assert len(op_list) == len(or_list), \
        "Number of points and radii not the same"
    # remove overlapping adjacent points
    p_list, r_list, r2_list = [], [], or_list[:]
    for i1, p1 in enumerate(op_list):
        i2 = (i1 + 1) % len(op_list)
        p2, r2, r1 = op_list[i2], r2_list[i2], r2_list[i1]
        if dist(p1[0], p1[1], p2[0], p2[1]) > 1:  # or p1 != p2:
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
            if r2 < 0:
                a2 = a2 - TWO_PI
            b_arc(p2[0], p2[1], r2 * 2, r2 * 2, start, a2, 2)
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

def b_arc(cx, cy, w, h, start_angle, end_angle, mode):
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

# ==== This is required by pyp5js to work
event_functions = { "mousePressed": mousePressed,  "mouseDragged": mouseDragged,  "mouseReleased": mouseReleased, "keyPressed":keyPressed }
start_p5(setup, draw, event_functions)
