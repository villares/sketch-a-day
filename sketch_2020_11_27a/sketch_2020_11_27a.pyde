from villares.line_geometry import draw_poly, poly_edges, Line
from villares.line_geometry import hatch_poly

def setup():
    size(400, 400)

def draw():
    background(100, 130, 100)
    stroke(0)
    fill(255)
    poly = [(75, 150), (350, 50), (350, 350), (50, 350)]
    poly[0] = (mouseX, mouseY)
    # dash_line (100, 100, mouseX, mouseY)
    draw_poly(poly)
    angs = [int(degrees(atan2(e[0][1] - e[1][1], e[0][0] - e[1][0]) + PI + HALF_PI))
            # for e in poly_edges(r)[:1]]
            for e in poly_edges(poly)[::3]]
    angs = {ang if ang < 180 else
            ang - 180 if ang < 360 else
            ang - 360
            for ang in angs}
    # text(str(angs), 30, 30)
    for ang in angs:
        hatch_poly(poly, radians(ang),
                    spacing=10,
                    # proportion=0.25,
                    function=fixed_dash_line if mousePressed else dash_line,
                    # function=circ_line,
                    base=True,
                    )

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

# from villares.line_geometry import min_max, rect_points, rotate_point, inter_lines
 
# def hatch_poly(points, angle, **kwargs):
#     spacing = kwargs.get('spacing', 5)
#     function = kwargs.pop('function', None)
#     base = kwargs.pop('base', False)
#     bound = min_max(points)
#     diag = Line(bound)
#     d = diag.dist()
#     cx, cy, _ = diag.midpoint()
#     num = int(d / spacing)
#     rr = [rotate_point(x, y, angle, cx, cy)
#           for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
#     # stroke(255, 0, 0)   # debug mode
#     ab = Line(rr[0], rr[1])  # ;ab.plot()  # debug mode
#     cd = Line(rr[3], rr[2])  # ;cd.plot()  # debug mode
#     for i in range(num + 1):
#         abp = ab.line_point(i / float(num) + EPSILON)
#         cdp = cd.line_point(i / float(num) + EPSILON)
#         if not function:
#             for hli in inter_lines(Line(abp, cdp), points):
#                 hli.plot()
#         else:
#             kwargs['function'] = function
#             if base == True:
#                 # add back base kwarg as a line
#                 kwargs['base_line'] = Line(abp, cdp)
#                 for hli in inter_lines(Line(abp, cdp), points):
#                     hli.plot(**kwargs)
#             else:
#                 for hli in inter_lines(Line(abp, cdp), points):
#                     hli.plot(**kwargs)
    
