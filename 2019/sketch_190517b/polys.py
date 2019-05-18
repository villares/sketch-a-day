# -*- coding: utf-8 -*-

def poly(p_list, closed=True):
    beginShape()
    for p in p_list:
        if p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)
    if closed:
        endShape(CLOSE)
    else:
        endShape()

def poly_arc_augmented(p_list, r_list):
    a_list = []
    for i1 in range(len(p_list)):
        i2 = (i1 + 1) % len(p_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        a = circ_circ_tangent(p1, p2, r1, r2)
        a_list.append(a)
        # ellipse(p1.x, p1.y, 2, 2)

    for i1 in range(len(a_list)):
        i2 = (i1 + 1) % len(a_list)
        p1, p2, r1, r2 = p_list[i1], p_list[i2], r_list[i1], r_list[i2]
        #ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
        a1 = a_list[i1]
        a2 = a_list[i2]
        if a1 and a2:
            start = a1 if a1 < a2 else a1 - TWO_PI
            arc(p2.x, p2.y, r2 * 2, r2 * 2, start, a2)
        else:
            # println((a1, a2))
            ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
            ellipse(p2.x, p2.y, r2 * 2, r2 * 2)


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
        return None
