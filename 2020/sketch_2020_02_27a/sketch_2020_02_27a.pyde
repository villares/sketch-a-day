# add_library('gifAnimation')
# from gif_animation_helper import gif_export

from arcs import *

many_arrows = []
player_arrow = []
i = 0
t = 0

def setup():
    size(400, 400)
    colorMode(HSB)
    noFill()
    strokeWeight(1)
    strokeJoin(ROUND)
    frameRate(30)
    # smooth(4)
    for _ in range(3):
        many_arrows.append(create_arrows())
    player_arrow[:] = list(random_arrow())

def create_arrows():
    arrows = []
    for _ in range(5):
        arrows.append(random_arrow())
    return arrows

def draw():
    global t, i
    background(200)
    if t <= width:
        tt = map(t, 0, width, 0, 1)
    else:
        tt = 1

    ini_arrows, fin_arrows = many_arrows[i], many_arrows[i - 1]
    for a, b in zip(ini_arrows, fin_arrows):
        rad, start, sweep, thick, h = lerp_arrow(b, a, tt)
        fill(h, 255, 200, 150)
        stroke(0)
        strokeWeight(2)
        if compare_arrows(a, player_arrow):
            fill(255)
            ini_arrows.remove(a)
        update_arrow(rad, start, sweep, thick)

    noFill()
    stroke(255)
    strokeWeight(2)
    rad, start, sweep, thick, _ = player_arrow
    update_arrow(rad, start, sweep, thick)

    # t += (1 + width - t) / 300.
    print t
    if t <= width:
        t = lerp(t, width + 1, .05)
    elif t > width:
        t += 2
    if t > 1.5 * width:
        t = 0
        i = (i + 1) % 3
    #     if i == 0:
    #         gif_export(GifMaker, finish=True)
    # if frameCount % 2 == 0:
    #     gif_export(GifMaker, filename="sketch")


def lerp_arrow(a, b, t):
    c = []
    for c_a, c_b in zip(a, b):
        c.append(lerp(c_a, c_b, t))
    return c

def update_arrow(rad, start, sweep, thick):
    start += thick * radians(frameCount % 361) / 10.
    arc_arrow(width / 2, height / 2, rad, start, sweep, thick)

def random_arrow():
    d = -1 if random(100) >= 50 else 1
    return [int(random(10, height / 10)) * 5 * d,
            0,  # start
            int(6 * random(QUARTER_PI, TWO_PI - QUARTER_PI) / 6),  # sweep
            int(random(2, height / 100)) * 10,  # thickness
            random(255),  # hue
            ]

def compare_arrows(a, b, t=3):
    rad, _, sweep, thick, _ = a
    brad, _, bsweep, bthick, _ = b
    return (abs(rad - brad) < t and
            abs(sweep - bsweep) < radians(t) and
            abs(thick - bthick) < t)

def keyPressed():
    if key == ' ':
        many_arrows[:] = []
        for _ in range(3):
            many_arrows.append(create_arrows())
        player_arrow[:] = list(random_arrow())

    if key == 's':
        saveFrame('#####.png')
    if key == 'a':
        player_arrow[3] += 10
    if key == 'z' and player_arrow[3] > 10: 
        player_arrow[3] -= 10

def mouseWheel(e):
    w = e.getAmount()
    player_arrow[3] += int(w) * 10
    if player_arrow[3] < 10:
        player_arrow[3] = 10

def mouseDragged():
    dx = mouseX - pmouseX
    dy = mouseY - pmouseY
    player_arrow[2] += radians(dx)
    player_arrow[0] += dy

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
