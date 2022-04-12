import py5

pts = [(100, 100), (500, 150), (500, 400), (200, 500)]

def setup():
    py5.size(600, 600)
    py5.no_fill()

def draw():
    py5.background(200)
    poly = pts + [(py5.mouse_x, py5.mouse_y)]
    draw_poly(poly)
    for _ in range(10):
        poly = offset(poly, -20)
        draw_poly(poly)

def draw_poly(poly):
    with py5.begin_closed_shape():
        py5.vertices(poly)

def offset(poly, off_d):
    result = []
    triples = zip([poly[-1]] + poly[:-1], poly, poly[1:] + [poly[0]])
    for i, ((xa, ya), (xb, yb), (xc, yc)) in enumerate(triples):
        r = -off_d if i == 0 else off_d
        ang0 = py5.atan2(ya - yb, xa - xb)
        ang1 = py5.atan2(yb - yc, xb - xc)
        ang = (ang0 + ang1) / 2 + py5.HALF_PI
        off_x = r * py5.cos(ang)
        off_y = r * py5.sin(ang)
        result.append((xb + off_x, yb + off_y))
    return result

py5.run_sketch()
