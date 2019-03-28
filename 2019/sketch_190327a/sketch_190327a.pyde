from arcs import poly_rounded2

p_list = [PVector(100, 100),
          PVector(400, 100),
          PVector(100, 400),
          PVector(400, 300)
          ]

rad_list = [10, 20, 30, 60]

def setup():
    size(500, 500)
    # smooth(16)
    noLoop()

def draw():
    noFill()
    strokeWeight(1)
    poly_rounded2(p_list, rad_list, open_poly=False)
    strokeWeight(2)
    poly_rounded3(p_list, rad_list)

def poly_rounded3(p_list, r_list):
    for p0, p1, p2, r0, r1, r2 in zip(p_list,
                                      [p_list[-1]] + p_list[:-1],
                                      [p_list[-2]] + [p_list[-1]] +
                                      p_list[:-2],
                                      r_list,
                                      [r_list[-1]] + r_list[:-1],
                                      [r_list[-2]] + [r_list[-1]] +
                                      r_list[:-2],
                                      ):
        circ_circ_tangent(p2, p1, r2, r1)
        ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
        ellipse(p1.x, p1.y, 2, 2)

def circ_circ_tangent(p1, p2, r1, r2):
    d = dist(p1.x, p1.y, p2.x, p2.y)
    ri = r1 - r2
    if d > abs(ri):
        line_angle = atan2(p1.x - p2.x, p2.y - p1.y)
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
        # return (PVector(x1, y1), PVector(x2, y2))
