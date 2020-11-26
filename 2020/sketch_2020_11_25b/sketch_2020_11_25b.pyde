from villares.line_geometry import draw_poly, poly_edges, Line, min_max, rect_points, rotate_point, inter_lines

def setup():
    size(400, 400)
    strokeWeight(2)

def draw():
    background(100, 130, 100)
    stroke(0)
    fill(255)
    r = [(75, 150), (350, 50), (350, 350), (50, 350)]
    r[0] = (mouseX, mouseY)
    # dash_line (100, 100, mouseX, mouseY)
    draw_poly(r)
    angs = [int(degrees(atan2(e[0][1] - e[1][1], e[0][0] - e[1][0]) + PI + HALF_PI))
    for e in poly_edges(r)[::2]]
    angs = {ang if ang < 180 else
            ang - 180 if ang < 360 else
            ang - 360
            for ang in angs}
    # text(str(angs), 30, 30)
    for ang in angs:
        hatch_poly2(r, radians(ang), spacing=8, function=fixed_dash_line)
        # hatch_poly(r, radians(ang), spacing=5, function=dash_line2)

def hatch_poly2(points, angle, **kwargs):
    spacing = kwargs.get('spacing', 5)
    function = kwargs.pop('function', None)
    bound = min_max(points)
    diag = Line(bound)
    d = diag.dist()
    cx, cy, _  = diag.midpoint()
    num = int(d / spacing)
    rr = [rotate_point(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])  # ;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])  # ;cd.plot()  # debug mode
    for i in range(num + 1):
        abp = ab.line_point(i / float(num) + EPSILON)
        cdp = cd.line_point(i / float(num) + EPSILON)
        base_line = Line(abp, cdp)
        if function:
            kwargs['function'] = function
            for hli in inter_lines(base_line, points):
                kwargs['inside'] = hli
                base_line.plot(**kwargs)
        else:
            for hli in inter_lines(base_line, points):
                hli.plot()
                
def fixed_dash_line(xa, ya, xb, yb, inside=None, spacing=12):
    inside = inside or Line(xa, ya, xb, yb)
    v = PVector(xb, yb) - PVector(xa, ya)
    d = v.mag()
    divisions = int(d / spacing)
    v = v.normalize() * spacing    
    xs, ys = xa, ya 
    for i in range(0, int(divisions * 2) + 1, 2):
    # for i in range(0, int(divisions) + 1):
        xe, ye = xs + v.x / 2, ys + v.y / 2
        start_in, end_in = inside.contains_point(xs, ys), inside.contains_point(xe, ye)
        if start_in and end_in:   
            line(xs, ys, xe, ye)     
        elif start_in:
            line(xs, ys, inside[0][0], inside[0][1])
        elif end_in:
            line(xe, ye, inside[1][0], inside[1][1])            
        xs += v.x  
        ys += v.y
