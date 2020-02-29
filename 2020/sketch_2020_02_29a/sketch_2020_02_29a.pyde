add_library('gifAnimation')
from gif_animation_helper import gif_export

from arcs import *

many_arrows = []
num_arrows, num_transitions = 6, 3
i, t = 0, 0

def setup():
    global player_arrow
    size(400, 400)
    colorMode(HSB)
    strokeJoin(ROUND)
    frameRate(30)
    background(200)
    for _ in range(num_transitions):
        many_arrows.append(create_arrows())
    player_arrow = list(random_arrow())

def create_arrows():
    arrows = []
    for _ in range(num_arrows):
        arrows.append(random_arrow())
    return arrows

def draw():
    global t, i
    fill(200, 2)
    rect(0, 0, width, height)

    if t <= width:
        tt = map(t, 0, width, 0, 1)
    else:
        tt = 1

    ini_arrows, fin_arrows = many_arrows[i], many_arrows[i - 1]
    for a, b in zip(ini_arrows, fin_arrows):
        rad, start, sweep, thick, h = lerp_arrow(b, a, tt)
        fill(h, 255, 200, 25)
        # noStroke()
        stroke(0, 200)
        player_arrow[0] = int(dist(mouseX, mouseY, width / 2, height / 2))

        if compare_arrows(a, player_arrow):
            fill(255)
        display_arrow(rad, start, sweep, thick)

    print t
    if t <= width:
        t = lerp(t, width + 1, .05)
    elif t > width:
        t += 2
    if t > 1.1 * width:
        t = 0
        i = (i + 1) % num_transitions
        if i == 0:
            gif_export(GifMaker, finish=True)
    if frameCount % 2 == 0:
        gif_export(GifMaker, filename="sketch")

def lerp_arrow(a, b, t):
    c = []
    for c_a, c_b in zip(a, b):
        c.append(lerp(c_a, c_b, t))
    return c

def display_arrow(rad, start, sweep, thick, rot=True):
    if rot:
        start += thick * radians(frameCount % 361) / 10.
    arc_arrow(width / 2, height / 2, rad, start, sweep, thick)

def random_arrow():
    d = -1 if random(100) >= 50 else 1
    return [int(random(2, height / 11)) * 5,
            0,  # start
            int(6 * random(QUARTER_PI, PI) / 6),  # sweep
            int(random(2, height / 100)) * 10 * d,  # thickness
            random(255),  # hue
            ]

def keyPressed():
    if key == ' ':
        many_arrows[:] = []
        for _ in range(3):
            many_arrows.append(create_arrows())
        player_arrow[:] = list(random_arrow())

    if key == 's':
        saveFrame('#####.png')

def arc_arrow(x, y, radius, start_ang, sweep_ang,
              thickness=None, correction=1):
    """
    Draws an arrow in a circular arc shape
    """
    if thickness is None:
        thickness = radius / 2
    if abs(radius) * .75 < abs(thickness / 2):
        thickness = radius * 1.5 if thickness > 0 else -radius * 1.5
    if radius < 0:
        thickness = -thickness

    beginShape()
    b_circle_arc(x, y, radius + thickness / 2,
                 start_ang, sweep_ang, mode=2)
    mid_ending(x, y, radius, start_ang + sweep_ang, thickness, correction)
    b_circle_arc(x, y, radius - thickness / 2,
                 start_ang + sweep_ang, -sweep_ang, mode=2)
    mid_ending(x, y, radius, start_ang, thickness, correction)
    endShape(CLOSE)

def mid_ending(x, y, radius, angle, thickness, correction):
    if radius == 0:
        radius = 1
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

def compare_arrows(a, b, t=10):
    rad, start, sweep, thick, _ = a
    brad, bstart, bsweep, bthick, _ = b
    return (abs(rad - brad) < t)
