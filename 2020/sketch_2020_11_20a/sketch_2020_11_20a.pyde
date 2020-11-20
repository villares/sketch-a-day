from villares.line_geometry import inter_lines, draw_poly, Line

def setup():
    size(400, 400)
    fill(100, 20)
    smooth()

def draw():
    background(200, 230, 200)
    r = rect_points(75, 100, 200, 175)
    draw_poly(r)
    hatch(r, radians(mouseX))
    rect(175, 150, 10, 100)

def hatch(r, angle, e=10):
    d = dist(r[0][0], r[0][1], r[2][0], r[2][1])
    cx = (r[1][0] + r[2][0]) / 2.0
    cy = (r[0][1] + r[1][1]) / 2.0
    num = int(d / e)
    rr = [rotp(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # draw_poly(rr) # debug mode
    stroke(255, 0, 0)
    ab = Line(rr[0], rr[1])   .draw()  # debug mode
    cd = Line(rr[3], rr[2])   .draw()  # debug mode
    for i in range(num + 1):
        abp = ab.line_point(i / float(num) + EPSILON)
        cdp = cd.line_point(i / float(num) + EPSILON)
        for hli in inter_lines(Line(abp, cdp), r):
            hli.draw()
    stroke(0)

def rect_points(x, y, w, h, mode=CORNER):
    if mode == CENTER:
        x, y = x - w / 2.0, y - h / 2.0
    return [(x, y), (x, y + h), (x + w, y + h), (x + w, y)]

def rotp(xp, yp, angle, x0=0, y0=0):
    x, y = xp - x0, yp - y0  # translate to origin
    rx = x0 + x * cos(angle) - y * sin(angle)
    ry = y0 + y * cos(angle) + x * sin(angle)
    return (rx, ry)
