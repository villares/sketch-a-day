def setup():
    size(500, 500)
    
def draw():
    background(200)
    r = 100
    p1 = PVector(200, 250)
    p2 = PVector(mouseX, 250)
    ellipse(p1.x, p1.y, r * 2, r * 2)
    line(p1.x, p1.y, p2.x, p2.y)
    d = dist(p1.x, p1.y, p2.x, p2.y)
    theta = asin(r / d)
    beta = TWO_PI - HALF_PI - theta
    print(degrees(theta))
    x = cos(beta) * r
    y = sin(beta) * r
    line(p1.x, p1.y, p1.x - x, p1.y - y)
    line(p2.x, p2.y, p1.x - x, p1.y - y)
