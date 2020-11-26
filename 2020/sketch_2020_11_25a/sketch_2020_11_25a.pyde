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
        hatch_poly(r, radians(ang), spacing=5, function=circ_line3)
        # hatch_poly(r, radians(ang), spacing=5, function=dash_line2)

    # I have modifierd Line .plot method to accept a custom drawing function
    # and also also the hatch_poly, both at github.com/villares/villares    
        
        
def circ_line3(xa, ya, xb, yb, spacing=12):
    v = PVector(xb, yb) - PVector(xa, ya)
    divisions = int(v.mag() / spacing)
    v = v.normalize() * spacing    
    xn, yn = xa, ya
    for i in range(0, int(divisions * 2), 2):
        xn += v.x
        yn += v.y
        noStroke()
        fill(0)
        circle(xn, yn, 3)
        
        
def circ_line2(xa, ya, xb, yb, spacing=12):
    divisions = int(dist(xa, ya, xb, yb) / spacing)
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
                    

def dash_line2(xa, ya, xb, yb, spacing=12):
    v = PVector(xb, yb) - PVector(xa, ya)
    d = v.mag()
    divisions = int(d / spacing)
    v = v.normalize() * spacing    
    xs, ys = xa, ya
    for i in range(0, int(divisions * 2) + 1, 2):
        xe, ye = xs + v.x / 2, ys + v.y / 2
        if dist(xa, ya, xe, ye) > d: xe, ye = xb, yb            
        line(xs, ys, xe, ye)
        xs += v.x  
        ys += v.y
