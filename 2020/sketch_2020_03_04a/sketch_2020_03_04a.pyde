# add_library('GifAnimation')
# from gif_animation_helper import gif_export

from arcs import *

many_arrows = []
num_arrows, num_transitions = 3, 4
i, t = 0, 0

def setup():
    size(400, 400)
    # colorMode(HSB)
    strokeJoin(ROUND)
    frameRate(30)
    smooth(8)
    for _ in range(num_transitions):
        many_arrows.append(create_arrows())
    global starting_arrows
    many_arrows.append(many_arrows[0][:])


def create_arrows():
    arrows = []
    for _ in range(num_arrows):
        arrows.append(random_arrow())
    return arrows

def draw():
    global t, i
    background(200)
    if t <= width:
        tt = map(t, 0, width, 0, 1)
    else:
        tt = 1

    ini_arrows, fin_arrows = many_arrows[i], many_arrows[i + 1]
    for a, b in zip(ini_arrows, fin_arrows):
        mid_arrow = lerp_arrow(a, b, tt)
        rad, start, sweep, thick, h = mid_arrow
        noFill()
        strokeWeight(4)
        if thick > 0:
            start = TWO_PI * tt
        else:
            start = TWO_PI * -tt
        mid_arrow[1] = start
        if mouse_on_arrow(mid_arrow):
            stroke(255, 150)
        else:
            stroke(0, 150)
        noFill()
        arc_arrow(width / 2, height / 2, rad, start, sweep, thick)

    if t < width:
        t = lerp(t, width + 1, .01)
    else:
        t = 0
        i = (i + 1) % num_transitions
    #     if i == 0:
    #         gif_export(GifMaker, finish=True)
    # gif_export(GifMaker, filename="sketch")

def lerp_arrow(a, b, t):
    result = []
    for c_a, c_b in zip(a, b):
        result.append(lerp(c_a, c_b, t))
    return result

def random_arrow():
    d = -1 if random(100) >= 50 else 1
    return [int(random(10, height / 12)) * 5,
            radians(int(random(60)) * 5),  # start
            int(6 * random(QUARTER_PI, TWO_PI - QUARTER_PI) / 6),  # sweep
            int(random(2, height / 100)) * 10 * d,  # thickness
            random(256)  # hue
            ]

def mouse_on_arrow(a, precision=10):
    mx, my = width / 2, height / 2
    rad, start, sweep, thick, _ = a
    # start += thick * radians(frameCount % 361) / 10.
    same_rad = abs(abs(rad) - dist(mouseX, mouseY, mx, my)) < precision
    mouse_ang = atan2(mouseY - my, mouseX - mx)
    line(mouseX, mouseY, mx, my)
    textSize(14)
    fill(255, 0, 0)
    text(str(int(degrees(mouse_ang))), mouseX, mouseY)
    in_sweep = start < mouse_ang < degrees(start + sweep)
    x, y = point_on_arc(mx, my, abs(rad), start)
    text(str(int(degrees(start))), x, y)
    x, y = point_on_arc(mx, my, abs(rad), start + sweep)
    text(str(int(degrees(start+sweep))), x, y)
    # return same_rad and in_sweep
    return in_sweep


def keyPressed():

    if key == 's':
        saveFrame('#####.png')

# def mouseWheel(e):
#     w = e.getAmount()
#     player_arrow[3] += int(w) * 10
#     if player_arrow[3] < 10:
#         player_arrow[3] = 10

# def mouseDragged():
#     dx = mouseX - pmouseX
#     dy = mouseY - pmouseY
#     player_arrow[2] += radians(dx)
#     player_arrow[0] += dy

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
