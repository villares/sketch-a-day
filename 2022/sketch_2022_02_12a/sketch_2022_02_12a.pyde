from random import randint

def setup():
    size(800, 400)
    strokeWeight(2)
    noFill()
    for y in range(25, height - 50, 10):
        path(10, y,  w=randint(10, 40), h=randint(5, 40))
    
def path(x, y, w, h, n=10):    
    points= [(x, y)]
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
