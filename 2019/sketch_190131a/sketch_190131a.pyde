def setup():
    size(500, 500)

def draw():
    background(200)
    strokeWeight(1)
    stroke(0)
    r1 = 75.
    r2 = 25.
    ri = r1 - r2
    p1 = PVector(200, 250)
    p2 = PVector(map(mouseX, 0, width, p1.x + 1, width), 250)
    ellipse(p2.x, p2.y, r2 * 2, r2 * 2)
    ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
    #ellipse(p1.x, p1.y, ri*2, ri*2)
    #line(p1.x, p1.y, p2.x, p2.y)
    strokeWeight(3)
    d = dist(p1.x, p1.y, p2.x, p2.y)
    theta = asin(ri / d)
    beta = 3 * HALF_PI - theta
    x = cos(beta) * ri
    y = sin(beta) * ri
    #line(p1.x - x, p1.y - y, p1.x, p1.y)
    #line(p1.x - x, p1.y - y, p2.x, p2.y)
    x1 = cos(beta) * r1
    y1 = sin(beta) * r1
    x2 = cos(beta) * r2
    y2 = sin(beta) * r2
    line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)
    line(p1.x - x1, p1.y + y1, p2.x - x2, p2.y + y2)
    stroke(255, 0, 0)
    # rt_ang + sweep_ang)
    arc(p1.x, p1.y, r1 * 2, r1 * 2,
        -1.5 * PI - theta, -HALF_PI + theta)
    # rt_ang + sweep_ang)
    arc(p2.x, p2.y, r2 * 2, r2 * 2,
        -HALF_PI + theta, HALF_PI - theta)
    println((beta, PI + beta))

    # thickness = r2 * 2
    # with pushMatrix():
    #     translate(p1.x, p1.y)
    #     angle = atan2(p1.x - p2.x, p2.y - p1.y)
    #     rotate(angle)
    #     offset = 0
    #     line(thickness/2, offset, thickness/2, d - offset)
    #     line(-thickness/2, offset, -thickness/2, d - offset)
    # if ends[0]:
    # half_circle(0, offset, thickness/2, UP)
    # if ends[1]:
    # half_circle(0,  d - offset, thickness/2, DOWN)


def keyPressed():
    saveFrame("sketch-190131a.png")
