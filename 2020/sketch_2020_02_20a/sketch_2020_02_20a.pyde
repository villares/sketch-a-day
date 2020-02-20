from arcs import *

arrows = []

def setup():
    size(500, 500)
    colorMode(HSB)
    strokeJoin(ROUND)
    create_arrows()

def create_arrows():
    arrows[:] = []
    arrows.append((125,  # radius
                   PI,  # start
                   PI,  # sweep
                   100,  # thickness
                   color(255),  # color
                   ))

def draw():
    background(200)
    for rad, start, sweep, thick, cor in arrows:
        thick = mouseY - 250
        sweep = radians(1 + mouseX)
        noFill()
        strokeWeight(5)
        stroke(180)
        circle(width / 2, height / 2, rad * 2)
        stroke(cor)
        arc_arrow(width / 2, height / 2, rad, start, sweep, thick)
        stroke(0)
        arc_arrow_b(width / 2, height / 2, rad, start, sweep, thick-10)


def keyPressed():
    if key == ' ':
        create_arrows()
    if key == 's':
        saveFrame('#####.png')

def arc_arrow_b(x, y, radius, start_ang, sweep_ang, thickness=None):
    """
    Draws an arrow in a circular arc shape
    """
    if thickness is None:
        thickness = radius / 2.
    if radius * .75 < abs(thickness / 2):
        thickness = radius * 1.5 if thickness > 0 else -radius * 1.5
    half_thickness = thickness / 2.
    offset = half_thickness / radius
    beginShape()
    b_circle_arc(x, y, radius + half_thickness,
                 start_ang, sweep_ang, mode=2)
    vertex(*point_on_arc(x, y, radius, start_ang + sweep_ang + offset))
    b_circle_arc(x, y, radius - half_thickness,
                 start_ang + sweep_ang, -sweep_ang, mode=2)
    vertex(*point_on_arc(x, y, radius, start_ang + offset))
    endShape(CLOSE)


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
    if radius * .75 < abs(thickness / 2):
        thickness = radius * 1.5 if thickness > 0 else -radius * 1.5

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
    # # debug
    # pushStyle()
    # stroke(180)
    # line(mp[0], mp[1], ep[0], ep[1]) # debug
    # popStyle()
    
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
