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
    p2 = PVector(mouseX, mouseY)
    # ellipse(p2.x, p2.y, r2 * 2, r2 * 2)
    # ellipse(p1.x, p1.y, r1 * 2, r1 * 2)
    strokeWeight(3)
    new_bar(p1, p2, r1, r2)


def new_bar(p1p, p2p, r1, r2):
    d = dist(p1p.x, p1p.y, p2p.x, p2p.y)
    p2 = PVector(d, 0)
    p1 = PVector(0, 0)
    ri = r1 - r2
    with pushMatrix():
        translate(p1p.x, p1p.y)
        angle = atan2(p1p.x - p2p.x, p2p.y - p1p.y)
        rotate(angle + HALF_PI)
        theta = asin(ri / d)
        beta = 3 * HALF_PI - theta
        x = cos(beta) * ri
        y = sin(beta) * ri
        x1 = cos(beta) * r1
        y1 = sin(beta) * r1
        x2 = cos(beta) * r2
        y2 = sin(beta) * r2
        line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)
        line(p1.x - x1, p1.y + y1, p2.x - x2, p2.y + y2)
        stroke(255, 0, 0)
        arc(p1.x, p1.y, r1 * 2, r1 * 2,
            -1.5 * PI - theta, -HALF_PI + theta)
        arc(p2.x, p2.y, r2 * 2, r2 * 2,
            -HALF_PI + theta, HALF_PI - theta)


def keyPressed():
    saveFrame("sketch-190131a.png")
