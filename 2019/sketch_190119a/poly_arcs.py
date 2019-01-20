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
     
def quarter_poly(x, y, radius, quadrant):
    with pushMatrix():
        translate(x, y)
        rotate(ROTATION[quadrant])
        line(radius, 0, 0, radius)
    

def half_poly(x, y, radius, quadrant):
    with pushMatrix():
        translate(x, y)
        rotate(ROTATION[quadrant] + HALF_PI)
        line( 0, -radius, radius, 0)
        line(radius, 0, 0,  radius)
    #poly_arc(x, y, radius, ROTATION[quadrant], PI)

def poly_arc(x, y, radius, start_ang, sweep_ang, num_points=2):
    angle = sweep_ang / int(num_points)
    a = start_ang
    with beginShape(): 
        while a <= start_ang + sweep_ang:
            sx = x + cos(a) * radius
            sy = y + sin(a) * radius
            vertex(sx, sy)
            a += angle
    
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
            half_poly(0, offset, thickness/2, UP)
        if ends[1]:
            half_poly(0,  L - offset, thickness/2, DOWN)
