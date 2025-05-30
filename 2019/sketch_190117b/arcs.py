# -*- coding: utf-8 -*-

ROTATION = {0 : 0,
            BOTTOM : 0,
            DOWN : 0,
            1 : HALF_PI,
            LEFT : HALF_PI,
            2 : PI,
            TOP : PI,
            UP : PI,
            3 : PI + HALF_PI,
            RIGHT: PI + HALF_PI,
            BOTTOM + RIGHT : 0,
            DOWN + RIGHT : 0,
            DOWN + LEFT : HALF_PI,
            BOTTOM + LEFT : HALF_PI,
            TOP + LEFT : PI,
            UP + LEFT : PI,
            TOP + RIGHT: PI + HALF_PI,
            UP + RIGHT: PI + HALF_PI,
            }
    
def quarter_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, ROTATION[quadrant], HALF_PI)

def half_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, ROTATION[quadrant], PI)

def circle_arc(x, y, radius, start_ang, sweep_ang):
    npoints = 2.
    angle = sweep_ang/npoints
    a = start_ang
    while a < start_ang + sweep_ang:
            sx = x + cos(a) * radius
            sy = y + sin(a) * radius
            line(0, 0, sx, sy)
            a += angle
    
    #arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang)
    
def bar(x1, y1, x2, y2, thickness=None, shorter=0, ends=(1,1)):
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
        line(thickness/2, offset, thickness/2, L - offset)
        line(-thickness/2, offset, -thickness/2, L - offset)
        if ends[0]:
            half_circle(0, offset, thickness/2, UP)
        if ends[1]:
            half_circle(0,  L - offset, thickness/2, DOWN)
