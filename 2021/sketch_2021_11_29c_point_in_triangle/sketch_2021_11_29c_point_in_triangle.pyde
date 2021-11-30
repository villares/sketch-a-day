def setup():
    size(550, 550)
    tri = (100, 100), (500, 200), (250, 500)
    (xa, ya), (xb, yb), (xc, yx) = tri
    noStroke()
    fill(255)
    triangle(xa, ya, xb, yb, xc, yx)
    print(millis())
    for i in range(100000):
        x, y = random(width), random(height)
        if point_in_triangle(x, y, tri):
            stroke(0)
        else:
            stroke(255, 0, 0)
        point(x, y)
    print(millis())
    
def point_in_triangle(_x, _y, tri):  # ~3 to 4 seconds
    (ax, ay), (bx, by), (cx, cy) = tri
    abc = abs(ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    pbc = abs(_x * (by - cy) + bx * (cy - _y) + cx * (_y - by))
    apc = abs(ax * (_y - cy) + _x * (cy - ay) + cx * (ay - _y))
    abp = abs(ax * (by - _y) + bx * (_y - ay) + _x * (ay - by))
    return not (pbc + apc + abp) > abc

def point_in_triangle2(x, y, tri):
    (ax, ay), (bx, by), (cx, cy) = tri
    ab = (x - bx) * (ay - by) - (ax - bx) * (y - by)
    bc = (x - cx) * (by - cy) - (bx - cx) * (y - cy)
    ca = (x - ax) * (cy - ay) - (cx - ax) * (y - ay)
    return (ab < 0) == (bc < 0) == (ca < 0)
