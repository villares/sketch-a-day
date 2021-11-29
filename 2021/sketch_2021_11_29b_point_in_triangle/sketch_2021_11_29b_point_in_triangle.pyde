def setup():
    size(550, 550)
    noCursor()
    strokeWeight(5)

def draw():
    background(240)
    tri = (100, 100), (500, 200), (250, 500)
    if point_in_triangle(mouseX, mouseY, tri):
        fill(0, 200, 0)
    else:
        fill(0, 0, 200)
    (xa, ya), (xb, yb), (xc, yx) = tri
    noStroke()
    triangle(xa, ya, xb, yb, xc, yx)
    stroke(0)
    point(mouseX, mouseY)

def point_in_triangle(x, y, tri):
    p = x, y
    a, b, c = tri
    at = triangle_area(a, b, c)
    a1 = triangle_area(p, b, c)
    a2 = triangle_area(a, p, c)
    a3 = triangle_area(a, b, p)
    return (a1 + a2 + a3) == at

def triangle_area(a, b, c):
    return abs(a[0] * (b[1] - c[1]) +
               b[0] * (c[1] - a[1]) +
               c[0] * (a[1] - b[1]))
    
