from villares.line_geometry import draw_poly, poly_edges, Line
from villares.line_geometry import hatch_poly, hatch_rect, rect_points

def setup():
    size(400, 400)
    noSmooth()

def draw():
    background(130, 130, 100)
    # fixed_dash_line (100, 100, mouseX, mouseY)
    angs = (0, 45, 90, 134)

    stroke(0)
    fill(255)
    for i in range(4):
        r = rect_points(10 + i * 60, 100, 60, 60)
        draw_poly(r)
        for ang in angs:
            hatch_rect(r, radians(angs[i % len(angs)]),
                        spacing=8.0,
                        # proportion=0.25,
                        function=circ_line if mousePressed else None,
                        circ_size=4,
                        base=True,
                        )
                

def dash_line(xa, ya, xb, yb, **kwargs):
    spacing = kwargs.pop('spacing', 20)
    divisions = int(dist(xa, ya, xb, yb) / spacing)
    for i in range(0, int(divisions * 2), 2):
        ts = i / float(divisions * 2)
        te = (i + 1) / float(divisions * 2)
        xs, ys, _ = Line(xa, ya, xb, yb).line_point(ts)
        xe, ye, _ = Line(xa, ya, xb, yb).line_point(te)
        line(xs, ys, xe, ye)

def circ_line(xa, ya, xb, yb, **kwargs):
    spacing = kwargs.pop('spacing', 20)
    circ_size = kwargs.pop('circ_size', 5)
    divisions = int(dist(xa, ya, xb, yb) / spacing) + 1
    for i in range(1, divisions):
        t = i / float(divisions)
        x, y, _ = Line(xa, ya, xb, yb).line_point(t)
        circle(x, y, circ_size)

def fixed_dash_line(xa, ya, xb, yb, base_line=None, spacing=20, proportion=0.5):
    inside = Line(xa, ya, xb, yb)
    base_line = base_line or inside
    v = base_line.as_PVector()
    base_length = v.mag()
    divisions = int(base_length / spacing)
    v = v.normalize() * spacing
    xs, ys = base_line[0][0], base_line[0][1]
    for i in range(0, int(divisions) + 1):
        xe, ye = xs + v.x * proportion, ys + v.y * proportion
        start_in, end_in = inside.contains_point(
            xs, ys), inside.contains_point(xe, ye)
        if start_in and end_in:
            line(xs, ys, xe, ye)
        elif end_in:
            ending = Line(xe, ye, inside[1][0], inside[1][1])
            if ending.dist() <= v.mag():
                ending.plot()
        elif start_in:
            starting = Line(xs, ys, inside[0][0], inside[0][1])
            if starting.dist() <= v.mag():
                starting.plot()
        xs += v.x
        ys += v.y
