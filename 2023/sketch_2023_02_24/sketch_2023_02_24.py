from itertools import combinations

combos = []

def setup():
    size(600, 600)
    n = 8
    step = TWO_PI / n
    pts = []
    for i in range(n):
        a = HALF_PI + i * step
        # radius 250 causes weird diagonal behaviour!
        x = 300 + 256 * cos(a)
        y = 300 + 256 * sin(a) 
        pts.append((x, y))
    combos[:] = list(combinations(pts, 2))

def draw():
    background(200)
#     scale(3)
#     stroke(0)
#     dashed(10, 10, mouse_x, mouse_y, bs=is_key_pressed)
#     stroke(255, 0, 0)
#     point(10, 10)
#     point(mouse_x, mouse_y)
    for (ax, ay), (bx, by) in combos:
        dashed(ax, ay, bx, by, solid_start=is_key_pressed)
#     no_loop()
#     save_frame('out.png')   


def dashed(ax, ay, bx, by, u=20, solid_start=True):
    d = dist(ax, ay, bx, by)     # Line length
    if d:
        ux, uy = (bx - ax) / d, (by - ay) / d  # A "unit vector" of the line
        #nx, ny = uy, -ux                       # Normal direction
        n = d // u
        if n == 0:
           solid_start = True  
        elif n % 2 == 0:
           n = n - 1            
        ru = d - u * n
        x, y = ax + ux * ru /  2, ay + uy * ru / 2
        if solid_start:
            line(ax, ay, x, y) 
        for i in range(int(n)):
            if i % 2 == (1 if solid_start else 0):
                xd, yd = x + ux * u, y + uy * u
                line(x, y, xd, yd)
            x += ux * u
            y += uy * u
        if solid_start:
            line(x, y, bx, by)    
