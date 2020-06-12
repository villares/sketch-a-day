# add_library('gifAnimation')
# from gif_export import gif_export

def setup():
    size(400, 400)
    noStroke()
    colorMode(HSB)
    blendMode(ADD)

def draw():
    f = radians(frameCount - 1)
    background(0)
    noStroke()
    tc = poly_points(200, 200, 80, n=12, rot=-f)
    for i, p in enumerate(tc):
        fill(i *21, 255, 255)
        t(p[0], p[1], 120,
          1 * i * radians(60) + f,
          d=61)

    # if frameCount < 360:
    #    if frameCount % 2 == 0:
    #        gif_export(GifMaker,
    #                   "sketch_2020_06_12b",
    #                   quality=0,  # compression 0
    #                   # I used gifsicle aftewards:
    #                   # -03 -- colors 51
    #                   )
    # else:
    #     gif_export(GifMaker, finish=True)


def t(x, y, s, rot=0, d=71):
    pp = poly_points(x, y, s, 3, rot + PI)
    e0 = div_points(pp[0], pp[1], d)
    e1 = div_points(pp[1], pp[2], d)[::-1]
    lines = zip(e0, e1)
    for la, lb in zip(lines[:-1:2], lines[1::2]):
        (x0, y0), (x1, y1) = la
        (x3, y3), (x2, y2) = lb
        quad(x0, y0, x1, y1,
             x2, y2, x3, y3)

def div_points(a, b, d=10):
    return [(lerp(a[0], b[0], float(i) / d),
             lerp(a[1], b[1], float(i) / d))
            for i in range(d + 1)]

def poly_points(x, y, r, n, rot=0):
    a = TWO_PI / n
    points = []
    for i in range(n):
        px = x + r * cos(a * i + rot)
        py = y + r * sin(a * i + rot)
        points.append((px, py))
    return points
