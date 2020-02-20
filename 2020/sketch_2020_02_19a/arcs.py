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

def b_circle_arc(x, y, radius, start_ang, sweep_ang, mode=0):
    """
    Alternative interface for b_arc
    """
    b_arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang,
          mode=mode)

def b_arc(cx, cy, w, h, start_angle, end_angle, mode=0):
    """
    A bezier approximation of an arc
    using the same signature as the original Processing arc()
    mode: 0 "normal" or stand-alone arc, using beginShape() and endShape()
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

def p_circle_arc(x, y, radius, start_ang, sweep_ang, mode=0, num_points=None):
    """
    Alternative interface for b_arc
    """
    p_arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang,
          mode=mode, num_points=num_points)
                                
def p_arc(cx, cy, w, h, start_angle, end_angle, mode=0, num_points=None):
    """
    A poly approximation of an arc
    using the same signature as the original Processing arc()
    mode: 0 "normal" arc, using beginShape() and endShape()
              2 "naked" like normal, but without beginShape() and endShape()
                 for use inside a larger PShape
    """
    if not num_points:
        num_points = 24  
    # start_angle = start_angle if start_angle < end_angle else start_angle - TWO_PI
    sweep_angle = end_angle - start_angle  
    if mode == 0:
            beginShape()
    if sweep_angle < 0:
        start_angle, end_angle = end_angle, start_angle
        sweep_angle = -sweep_angle 
        angle = sweep_angle / int(num_points)
        a = end_angle
        while a >= start_angle:
                sx = cx + cos(a) * w / 2.
                sy = cy + sin(a) * h / 2.
                vertex(sx, sy)
                a -= angle   
    elif sweep_angle > 0:
        angle = sweep_angle / int(num_points)
        a = start_angle
        while a <= end_angle:
                sx = cx + cos(a) * w / 2.
                sy = cy + sin(a) * h / 2.
                vertex(sx, sy)
                a += angle
    else:
        sx = cx + cos(start_angle) * w / 2.
        sy = cy + sin(start_angle) * h / 2.
        vertex(sx, sy)
    if mode == 0:
        endShape()
