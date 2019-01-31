def setup():
    size(500, 500)
    
def draw():
    background(200)
    strokeWeight(3)
    r1 = 75.
    r2 = 25.
    ri = r1 - r2
    p1 = PVector(200, 250)
    p2 = PVector(mouseX, 250)
    ellipse(p2.x, p2.y, r2*2, r2*2)
    ellipse(p1.x, p1.y, r1*2, r1*2)
    ellipse(p1.x, p1.y, ri*2, ri*2)
    line(p1.x, p1.y, p2.x, p2.y)
    d = dist(p1.x, p1.y, p2.x, p2.y)
    theta = asin(ri / d)
    beta = 3 * HALF_PI - theta
    x = cos(beta) * ri
    y = sin(beta) * ri
    line(p1.x - x, p1.y - y, p1.x, p1.y)
    line(p1.x - x, p1.y - y, p2.x, p2.y)
    x1 = cos(beta) * r1
    y1 = sin(beta) * r1
    x2 = cos(beta) * r2
    y2 = sin(beta) * r2
    line(p1.x - x1, p1.y - y1, p2.x - x2, p2.y - y2)
    
    
