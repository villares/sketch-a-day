
def setup():
    size(500, 500)
    
def draw():
    background(230)
    path = (
        (50, 100),
        (250, 150),
        # (300, 450),
        (mouseX, mouseY),
        (450, 450),
    )
    noFill()
    beginShape()
    for x, y in path:
        vertex(x, y)
    endShape()
    offset = 20
    segments = []
    for (xa, ya), (xb, yb) in zip(path[:-1], path[1:]):
        angulo = atan2(yb - ya, xb - xa)
        v = PVector.fromAngle(angulo + HALF_PI) * offset 
        s1 = (xa + v.x, ya + v.y, xb + v.x, yb + v.y)
        s2 = (xa - v.x, ya - v.y, xb - v.x, yb - v.y)
        line(*s1)
        line(*s2)
        segments.append((xa, ya, xb, yb, angulo))
        
    for sa, sb in zip(segments[:-1], segments[1:]):
        angulo_m = (sa[-1] + sb[-1]) / 2
        v = PVector.fromAngle(angulo_m + HALF_PI) * offset
        xa, ya = sa[2:4]
        # xb, yb = sb[2:4]
        line(xa - v.x, ya - v.y, xa + v.x, ya + v.y)
