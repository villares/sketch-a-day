from random import randint

def setup():
    size(800, 800)
    strokeWeight(2)
    noFill()
    background(200)
    translate(width / 2, height / 2)
    x, y = 0, 0
    for n in range(1, 100):
        x, y = path(x, y,
                    w=randint(5, 20),
                    h=randint(5, 40),
                    n=randint(1, 5))
    
def path(x, y, w, h, n=10):
    translate(x, y)
    rotate(QUARTER_PI)
    points= [(0, 0)]
    for _ in range(n):
        step(points, w, h)
    draw_poly(points)
    return points[-1]
    
def step(pts, w, h):
    x, y = pts[-1]
    pts.append((x + w, y))
    pts.append((x + w, y + h))
    pts.append((x + w * 2, y + h))
    pts.append((x + w * 2, y))
             
def draw_poly(pts, closed=False):
    beginShape()
    for x, y in pts:
        vertex(x, y)    
    if closed:
        endShape(CLOSE)
    else:
        endShape()
