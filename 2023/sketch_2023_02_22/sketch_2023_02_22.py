from itertools import combinations

combos = []

def setup():
    size(600, 600)
    n = 12
    step = TWO_PI / n
    pts = []
    for i in range(n):
        a = HALF_PI + i * step
        x = 300 + 250 * cos(a)
        y = 300 + 250 * sin(a)
        pts.append((x, y))
    combos[:] = list(combinations(pts, 2))

# def draw():
#     background(200)
#     scale(3)
#     stroke(0)
#     dashed(10, 10, mouse_x, mouse_y)
#     stroke(255, 0, 0)
#     point(10, 10)
#     point(mouse_x, mouse_y)
    for (ax, ay), (bx, by) in combos:
        dashed(ax, ay, bx, by)
#    save_frame('out.png')   

def dashed(ax, ay, bx, by, u=20, a=0.5):
    mx, my = (ax + bx) / 2, (ay + by) / 2
    h_dashed(ax, ay, mx, my)
    h_dashed(bx, by, mx, my)

def h_dashed(ax, ay, bx, by, u=20, a=0.5):
    d = dist(ax, ay, bx, by)               # Line length
    if d:
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
        #stroke(0, 0, 100)
        line(x, y, x + ux * ru, y + uy * ru)    
