from villares.line_geometry import hatch_poly, draw_poly, poly_edges, Line
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

            
