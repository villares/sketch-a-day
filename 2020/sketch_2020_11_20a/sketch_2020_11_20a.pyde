from villares.line_geometry import inter_lines, draw_poly, Line

def setup():
    size(400, 400)

def draw():
    background(200, 230, 200)
    stroke(0)
    fill(255)
    r = rect_points(75, 100, 200, 155)
    draw_poly(r)
    hatch_rect(r, radians(mouseX))
    # fill(100, 20)
    # rect(100, 100, 200, 200)
    # hatch_rect(100, 100, 200, 200, radians(mouseY))

def hatch_rect(*args, **kwargs):
    if len(args) == 2:
        r, angle = args
    else:
        x, y, w, h, angle = args
        r = rect_points(x, y, w, h, kwargs.get('mode', CORNER)) 
    spacing = kwargs.get('spacing', 10)
    d = dist(r[0][0], r[0][1], r[2][0], r[2][1])
    cx = (r[0][0] + r[1][0]) / 2.0
    cy = (r[1][1] + r[2][1]) / 2.0
    num = int(d / spacing)
    rr = [rotp(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])  # ;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])  # ;cd.plot()  # debug mode
    for i in range(num + 1):
        abp = ab.line_point(i / float(num) + EPSILON)
        cdp = cd.line_point(i / float(num) + EPSILON)
        for hli in inter_lines(Line(abp, cdp), r):
            hli.plot()

def rect_points(x, y, w, h, mode=CORNER):
    if mode == CENTER:
        x, y = x - w / 2.0, y - h / 2.0
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]

def rotp(xp, yp, angle, x0=0, y0=0):
    x, y = xp - x0, yp - y0  # translate to origin
    rx = x0 + x * cos(angle) - y * sin(angle)
    ry = y0 + y * cos(angle) + x * sin(angle)
    return (rx, ry)
