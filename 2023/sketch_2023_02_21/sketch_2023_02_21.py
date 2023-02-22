from itertools import combinations

combos = []

def setup():
    size(600, 600)
    n = 7
    step = TWO_PI / n
    pts = []
    for i in range(n):
        a = HALF_PI + i * step
        x = 300 + 200 * cos(a)
        y = 300 + 200 * sin(a)
        pts.append((x, y))
    combos[:] = list(combinations(pts, 2))

def draw():
    background(200)
    for (ax, ay), (bx, by) in combos:
        dashed(ax, ay, bx, by)

def dashed(ax, ay, bx, by, u=20, a=0.5):
    d = dist(ax, ay, bx, by)               # Line length
    ux, uy = (bx - ax) / d, (by - ay) / d  # A "unit vector" of the line
    nx, ny = uy, -ux                       # Normal direction
    n = d // u
    stroke(0)
    ru = min(u * a, (d - u * n)) 
    x, y = ax, ay
    for i in range(int(n)):
        xd, yd = x + ux * u * a, y + uy * u * a
        line(x, y, xd, yd)
        x += ux * u
        y += uy * u
    stroke(0, 0, 100)
    line(x, y, x + ux * ru, y + uy * ru)    
