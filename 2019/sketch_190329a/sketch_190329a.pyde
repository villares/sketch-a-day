from arcs import poly_rounded2

rad_list = [10, 20, 30, 40]

def setup():
    size(500, 500)
    create_list()

def create_list():
    global p_list
    p_list = [PVector(random(r * 2, width  - r * 2),
                      random(r * 2, height - r * 2))
              for r in rad_list]
def draw():
    background(200)

    noFill()
    strokeWeight(1)
    poly_rounded2(p_list, rad_list, open_poly=False)
    strokeWeight(2)
    poly_rounded3(p_list, rad_list)

def poly_rounded3(p_list, r_list):
    a_list = []
    for i1 in range(len(p_list)):
        i2 = (i1 + 1) % len(p_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(a)
        ellipse(p1.x, p1.y, 2, 2)

    for i1 in range(len(a_list)):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        #ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
        a1 = a_list[i1]
        a2 = a_list[i2]
        if a1 and a2:
            start = a1 if a1 < a2 else a1 - TWO_PI
            arc(p2.x, p2.y, r2 * 2, r2 * 2, start, a2)
        elif a1:
            println((a1, a2))
            ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
        else:
            ellipse(p2.x, p2.y, r2 * 2, r2 * 2)
            println((a1, a2))


def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1.x, p1.y, p2.x, p2.y)
    ri = r1 - r2
    line_angle = atan2(p1.x - p2.x, p2.y - p1.y)
    if d > abs(ri):
        theta = asin(ri / float(d))

        x1 = cos(line_angle - theta) * r1
        y1 = sin(line_angle - theta) * r1
        x2 = cos(line_angle - theta) * r2
        y2 = sin(line_angle - theta) * r2
        # line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)

        x1 = -cos(line_angle + theta) * r1
        y1 = -sin(line_angle + theta) * r1
        x2 = -cos(line_angle + theta) * r2
        y2 = -sin(line_angle + theta) * r2
        line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)
        return (line_angle + theta)
    else:
        line(p1.x, p1.y, p2.x, p2.y)
        return line_angle

def mouseClicked():
    create_list()

def keyPressed():
    saveFrame("s####.png")
