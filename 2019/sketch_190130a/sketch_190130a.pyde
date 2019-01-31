def setup():
    size(500, 500)
    
def draw():
    background(200)
    r = 200
    p1 = PVector(200, 250)
    p2 = PVector(mouseX, mouseY)
    ellipse(p1.x, p1.y, r, r)
    line(p1.x, p1.y, p2.x, p2.y)
    d = dist(p1.x, p1.y, p2.x, p2.y)
    theta = asin(r / d)
    beta = TWO_PI - HALF_PI - theta
    print(degrees(theta))
