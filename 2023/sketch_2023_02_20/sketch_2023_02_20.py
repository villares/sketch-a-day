def setup():
    size(600, 600)
    no_cursor()

def draw():
    background(200)
    scale(3)
    dashed(20, 20, mouse_x, mouse_y)

def dashed(ax, ay, bx, by, u=20, a=0.5):
    stroke_weight(3)
    stroke(200, 0, 0)
    point(ax, ay)
    point(bx, by)
    stroke_weight(1)

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
