from arcs import *

arrows = []

def setup():
    size(500, 500)
    colorMode(HSB)
    create_arrows()
    
def create_arrows():
    arrows[:] = []
    for _ in range(12):
        arrows.append((random(height * 0.04, height * 0.4),
                       random(TWO_PI),  # start
                       random(TWO_PI),  # sweep
                       random(-height / 10, height / 10),  # thickness
                       random(255),  # hue
                       ))

def draw():
    background(0)
    for rad, start, sweep, thick, h in arrows:
        fill(h, 255, 255, 100)
        arc_arrow(width / 2, height / 2, rad, start, sweep, thick)

def keyPressed():
    if key == ' ':
        create_arrows()
    if key == 's':
        saveFrame('#####.png')

def arc_arrow(x, y, radius, start_ang, sweep_ang, thickness=None):
    """
    Draws an arrow in a circular arc shape
    """
    if thickness is None:
        thickness = radius / 2
    # off = radius / 2
    # if radius - off / 2 < thickness / 2:
    # fill(255, 0, 0) # debug
    #     thickness = radius * 2 - off
    # else:
    # fill(255)
    if radius * .75 < thickness / 2:
        thickness = radius * 1.5

    beginShape()
    b_circle_arc(x, y, radius + thickness / 2,
                 start_ang, sweep_ang, mode=2)
    mid_ending(x, y, radius, start_ang + sweep_ang, thickness)
    b_circle_arc(x, y, radius - thickness / 2,
                 start_ang + sweep_ang, -sweep_ang, mode=2)
    mid_ending(x, y, radius, start_ang, thickness)
    endShape(CLOSE)

def mid_ending(x, y, radius, angle, thickness):
    pa = point_on_arc(x, y, radius + thickness / 2, angle)
    pb = point_on_arc(x, y, radius - thickness / 2, angle)
    mp = mid_point(pa, pb)
    ep = point_on_arc(mp[0], mp[1], thickness / 2, angle + HALF_PI)
    vertex(*ep)
    # circle(mp[0], mp[1], 15) # debug

def mid_point(pa, pb):
    if len(pa) == 3 and len(pb) == 3:
        return ((pa[0] + pb[0]) / 2,
                (pa[1] + pb[1]) / 2,
                (pa[2] + pb[2]) / 2)
    else:
        return ((pa[0] + pb[0]) / 2,
                (pa[1] + pb[1]) / 2)

def point_on_arc(cx, cy, radius, angle):
    x = cx + radius * cos(angle)
    y = cy + radius * sin(angle)
    return (x, y)
