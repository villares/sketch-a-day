
def setup():
    size(500, 500)
    p1 = PVector(100, 100)
    p2 = PVector(400, 200)
    p3 = PVector(200, 400)
    po = PVector(10, 10)
    r1 = 30
    r2 = 50
    r3 = 70
    noFill()
    strokeWeight(1)
    vec_bar(p1, p2, r1, r2)
    vec_bar(p2, p3, r2, r3)
    vec_bar(p1, p3, r1, r3)
    triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)
    strokeWeight(3)
    r1 += 10
    r2 += 10
    r3 += 10
    test(p1, p2, r1, r2)
    test(p2, p3, r2, r3)
    test(p3, p1, r3, r1)


def test(pa, pb, r1, r2):
    p1x, p1y = pa.x, pa.y
    p2x, p2y = pb.x, pb.y
    d = dist(p1x, p1y, p2x, p2y)
    if d > 0:
        with pushMatrix():
            translate(p1x, p1y)
            ang = atan2(p1x - p2x, p2y - p1y) + HALF_PI
            rotate(ang)
            ri = r1 - r2
            beta = asin(ri / d) + HALF_PI #+ ang
            a = PVector(cos(beta) * r1, sin(beta) * r1)
            #a = a.rotate(ang)
            x1, y1 = a.x, a.y
            b = PVector(cos(beta) * r2,  sin(beta) * r2)
            #b = b.rotate(ang)
            x2, y2 = b.x, b.y
            line(-x1, -y1, d - x2, -y2)
            #line(-x1, +y1, d - x2, +y2)
            arc(0, 0, r1 * 2, r1 * 2,
                -beta - PI, beta - PI )
            #arc(d, 0, r2 * 2, r2 * 2,
                # beta - PI, PI - beta)


def vec_bar(p1, p2, r1, r2):
    var_bar(p1.x, p1.y, p2.x, p2.y, r1, r2)

def var_bar(p1x, p1y, p2x, p2y, r1, r2=None):
    if r2 is None:
        r2 = r1
    d = dist(p1x, p1y, p2x, p2y)
    if d > 0:
        with pushMatrix():
            translate(p1x, p1y)
            angle = atan2(p1x - p2x, p2y - p1y)
            rotate(angle + HALF_PI)
            ri = r1 - r2
            beta = asin(ri / d) + HALF_PI
            x1 = cos(beta) * r1
            y1 = sin(beta) * r1
            x2 = cos(beta) * r2
            y2 = sin(beta) * r2
            line(-x1, -y1, d - x2, -y2)
            line(-x1, +y1, d - x2, +y2)
            arc(0, 0, r1 * 2, r1 * 2,
                -beta - PI, beta - PI)
            arc(d, 0, r2 * 2, r2 * 2,
                beta - PI, PI - beta)
            with pushStyle():
                noStroke()
                fill(0)
                ellipse(-x1, -y1, 5, 5)
                ellipse(d - x2, -y2, 5, 5)
                ellipse(-x1, +y1, 5, 5)
                ellipse(d - x2, +y2, 5, 5)
    
