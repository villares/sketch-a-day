# add_library('VideoExport')
from arcs import *
# i, t = 0

def setup():
    size(400, 400)
    colorMode(HSB)
    noFill()
    strokeWeight(4)
    strokeJoin(ROUND)

    # global videoExport
    # videoExport = VideoExport(this, "video.mp4")
    # videoExport.setFrameRate(24)
    # videoExport.startMovie()
    # frameRate(24)

def create_arrows():
    arrows = []
    for _ in range(12):
        d = -1 if random(100) >= 50 else 1
        arrows.append((random(height * 0.04, height * 0.4),
                       random(TWO_PI),  # start
                       random(TWO_PI),  # sweep
                       random(5, height / 10) * d,  # thickness
                       random(255),  # hue
                       ))
    return arrows

def draw():
    background(200)
    # stroke(h, 255, 200, 200)
    rad = 100 + (mouseX / 10.) ** 2
    m = PI / 2 + mouseX / 50. 
    start, sweep, thick = -PI - HALF_PI/2 + m/2, PI + HALF_PI - m, 50
    pushMatrix()
    translate(width / 2, height / 2 + rad)
    # rotate(thick * frameCount / 1000.)
    arc_arrow(0, 0, rad, start, sweep, thick)
    popMatrix()

    # videoExport.saveFrame()


def keyPressed():
    if key == ' ':
        create_arrows()
    if key == 's':
        saveFrame('#####.png')

    # if key == 'q':
    #     videoExport.endMovie()
    #     exit()

def arc_arrow(x, y, radius, start_ang, sweep_ang,
              thickness=None, correction=1):
    """
    Draws an arrow in a circular arc shape
    """
    if thickness is None:
        thickness = radius / 2
    if radius * .75 < abs(thickness / 2):
        thickness = radius * 1.5 if thickness > 0 else -radius * 1.5

    beginShape()
    b_circle_arc(x, y, radius + thickness / 2,
                 start_ang, sweep_ang, mode=2)
    mid_ending(x, y, radius, start_ang + sweep_ang, thickness, correction)
    b_circle_arc(x, y, radius - thickness / 2,
                 start_ang + sweep_ang, -sweep_ang, mode=2)
    mid_ending(x, y, radius, start_ang, thickness, correction)
    endShape(CLOSE)

def mid_ending(x, y, radius, angle, thickness, correction):
    half_thick = thickness / 2.
    pa = point_on_arc(x, y, radius + half_thick, angle)
    pb = point_on_arc(x, y, radius - half_thick, angle)
    mp = mid_point(pa, pb)
    tangent_ep = point_on_arc(mp[0], mp[1], half_thick, angle + HALF_PI)
    offset = half_thick / radius
    midline_ep = point_on_arc(x, y, radius, angle + offset)
    if correction == 0:  # tangent
        vertex(*tangent_ep)
    elif correction == 2:  # on mid-line
        vertex(*midline_ep)
    else:  # half-way
        vertex(*mid_point(tangent_ep, midline_ep))

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
