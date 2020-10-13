

from villares.arcs import arc_filleted_poly

# ps = [(0, 48), (26, 0), (106, 0), (132, 48)]
ps = [(0, 48), (0, 0), (48, 0), (48, 48)]


def setup():
    global logos
    size(600, 600)
    noStroke()

    logos = []
    for i in range(12):
        r = color(128, 128, random(255))
        b = color(random(255), 129, 129)
        for j in range(8):
            pushMatrix()
            translate(-140 + i * 60 - 5 * j, -60 + j * 96)
            logos.append((rdc_s(100, 0), r))
            translate(60, 0)
            logos.append((rdc_s(100, 0), r))
            translate(-50, 112)
            logos.append((rdc_s(100, 0, 180), b))
            translate(60, 0)
            logos.append((rdc_s(100, 0, 180), b))
            popMatrix()

def draw():
    background(250)
    global t, d_factor
    t = frameCount / 300.
    d_factor = map(mouseX, 0, width, 1, 0)

    for i, logo in enumerate(distorter(logos)):
        pts, c = logo
        other = color(100, 255)
        if 67 < i < 72:
            fill(lerpColor(c, other, d_factor))
        else:
            fill(lerpColor(other, c, d_factor))
        arc_filleted_poly(pts, [8] * 4)
        fill(0)
        # text(str(i), pts[2][0], pts[2][1])


def distorter(inter):
    return (([distort(pt) for pt in pts], c)
            for pts, c in logos)

def distort(pt):
    # x = pt[0] - 5 + 10 * sin(t)
    # y = pt[1] - 10 + 50 * cos(t)
    s = 0.002
    id = 10 / (1 + dist(mouseX, mouseY, pt[0], pt[1]))
    x = pt[0] + (300 * noise(pt[0] * s, pt[1] * s, t) - 150) * d_factor
    y = pt[1] + (300 * noise(pt[0] * s, pt[1] * s, t) - 150) * d_factor
    return (x, y)

def rdc_s(x, y, r=0):
    new_ps = []
    pushMatrix()
    translate(x, y)
    rotate(radians(-300 + r))
    for xp, yp in ps:
        new_ps.append((screenX(xp, yp), screenY(xp, yp)))
    popMatrix()
    return new_ps

# def rdc(x, y, r=0):
#     pushMatrix()
#     translate(x, y)
#     rotate(radians(-300 + r))
#     arc_filleted_poly(ps, [8]*4)
#     popMatrix()
