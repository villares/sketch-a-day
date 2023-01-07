# using py5 (py5coding.org) imported mode

from itertools import product

def setup():
    size(600, 600)
    no_loop()
    
def draw():
    circles = []
    for x, y in product(range(100, 550, 50), repeat=2):
        r = random(10, 60)
        circles.append((x, y, r))

    intersections = []
    for xa, ya, ra in circles:
        for xb, yb, rb in circles[1:]:
            if (xa, ya) != (xb, yb):
                pts = calc_cci(xa, ya, ra, xb, yb, rb)
                intersections.extend(pts)

    background(0, 0, 100)
    stroke(255)
    no_fill()
    for x, y, r in circles:
        circle(x, y, r * 2)
    no_stroke()
    fill(255, 0, 0)
    for x, y in intersections:
        circle(x, y, 5)
    
def calc_cci(x0, y0, r0, x1 ,y1, r1):
    d = dist(x0, y0, x1, y1)
    a = (r0 ** 2-r1 ** 2+d ** 2) / (2 * d)
    hsqd = r0 ** 2 - a ** 2
    if hsqd == 0:
        return [(x0 + a * (x1 - x0) / d, y0 + a * (y1 - y0) / d)]
    elif hsqd > 0:
        h = sqrt(hsqd)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        xa, ya = x2 + h * (y1 - y0) / d, y2 - h * (x1 - x0) / d 
        xb, yb = x2 - h * (y1 - y0) / d, y2 + h * (x1 - x0) / d
        return[(xa, ya), (xb, yb)]
    else:
        return []
    
def key_pressed(): redraw()
        