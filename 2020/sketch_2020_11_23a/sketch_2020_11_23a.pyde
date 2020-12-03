from villares.line_geometry import draw_poly, poly_edges, Line
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
            for e in poly_edges(r)[::3]]
    angs = {ang if ang < 180 else
            ang - 180 if ang < 360 else
            ang - 360
            for ang in angs}
    # text(str(angs), 30, 30)
    for ang in angs:
        hatch_poly(r, radians(ang), spacing=15, function=circ_line)
        
    # I have modifierd Line .plot method to accept a custom drawing function
    # and also also the hatch_poly, both at github.com/villares/villares    
        
def circ_line(xa, ya, xb, yb, **kwargs):
    divisions = kwargs.get('divisions', 12.5)
    for i in range(0, int(divisions * 2), 2):
        ts = i / float(divisions * 2)
        te = (i + 1) / float(divisions * 2)
        xs, ys, _ = Line(xa, ya, xb, yb).line_point(ts)
        xe, ye, _ = Line(xa, ya, xb, yb).line_point(te)
        # line(xs, ys, xe, ye)
        noStroke()
        fill(0)
        circle(xs, ys, 3)
        circle(xe, ye, 3)
                    

def dash_line(xa, ya, xb, yb, divisions=12.5):
    for i in range(0, int(divisions * 2), 2):
        ts = i / float(divisions * 2)
        te = (i + 1) / float(divisions * 2)
        xs, ys, _ = Line(xa, ya, xb, yb).line_point(ts)
        xe, ye, _ = Line(xa, ya, xb, yb).line_point(te)
        line(xs, ys, xe, ye)
        # circle(xe, ye, 5)
        # circle(xs, ys, 5)

def hatch_poly(*args, **kwargs):
    if len(args) == 2:
        points, angle = args
    else:
        x, y, w, h, angle = args
        points = rect_points(x, y, w, h, kwargs.pop('mode', CORNER))
    spacing = kwargs.get('spacing', 5)
    function = kwargs.pop('function', None)
    base = kwargs.pop('base', False)
    odd_function = kwargs.pop('odd_function', False)

    kwargs['ps'] = ps =  createShape(GROUP) if kwargs.get('ps', False) else False  
    if len(args) == 2:
        d = dist(points[0][0], points[0][1], points[2][0], points[2][1]) + EPSILON
        cx = (points[0][0] + points[1][0]) / 2.0
        cy = (points[1][1] + points[2][1]) / 2.0
    else:
        bound = min_max(points)
        diag = Line(bound) 
        d = diag.dist() + EPSILON
        cx, cy, _ = diag.midpoint()
    num = int(d / spacing)
    rr = [rotate_point(x, y, angle, cx, cy)
          for x, y in rect_points(cx, cy, d, d, mode=CENTER)]
    # stroke(255, 0, 0)   # debug mode
    ab = Line(rr[0], rr[1])   #;ab.plot()  # debug mode
    cd = Line(rr[3], rr[2])   #;cd.plot()  # debug mode
    for i in range(num + 1):
        if odd_function is not False and i % 2:
            kwargs['function'] = odd_function 
        else:
            kwargs['function'] = function
        abp = ab.line_point(i / float(num) + EPSILON)
        cdp = cd.line_point(i / float(num) + EPSILON)
        if base == True:
            kwargs['base_line'] = Line(abp, cdp)
        for hli in inter_lines(Line(abp, cdp), points):
            hli.plot(**kwargs)
    return ps
            
