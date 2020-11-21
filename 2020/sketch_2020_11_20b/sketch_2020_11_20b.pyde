from villares.line_geometry import inter_lines, draw_poly, Line, min_max

def setup():
    size(400, 400)

def draw():
    background(200, 200, 230)
    stroke(0)
    fill(255)
    r = rect_points(75, 100, 200, 155)
    r.append((100, 150))
    r.insert(3, (150, 300))
    # r.extend(rect_points(150, 120, 50, 50))

    draw_poly(r)
    hatch_poly(r, radians(mouseX))

def hatch_poly(points, angle, **kwargs):
    spacing = kwargs.get('spacing', 5)
    bound = min_max(points)
    diag = Line(bound)
    d = diag.dist()
    cx, cy, _  = diag.midpoint()
    num = int(d / spacing)
    rr = [rotp(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])  # ;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])  # ;cd.plot()  # debug mode
    for i in range(num + 1):
        abp = ab.line_point(i / float(num) + EPSILON)
        cdp = cd.line_point(i / float(num) + EPSILON)
        for hli in inter_lines(Line(abp, cdp), points):
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
