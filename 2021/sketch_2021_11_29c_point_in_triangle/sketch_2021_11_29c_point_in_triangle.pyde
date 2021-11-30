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

def point_in_triangle2(x, y, tri):
    ax, ay = tri[0]
    bx, by = tri[1]
    cx, cy = tri[2]
    # Segment A to B
    side_1 = (x - bx) * (ay - by) - (ax - bx) * (y - by)
    # Segment B to C
    side_2 = (x - cx) * (by - cy) - (bx - cx) * (y - cy)
    # Segment C to A
    side_3 = (x - ax) * (cy - ay) - (cx - ax) * (y - ay)
    # All the signs must be positive or all negative
    return (side_1 < 0.0) == (side_2 < 0.0) == (side_3 < 0.0)
