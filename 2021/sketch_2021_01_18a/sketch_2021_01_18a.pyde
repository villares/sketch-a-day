from random import choice, sample

w = 10
walkers = (lambda: (choice((-w, 0, 0, w)), choice((-w, 0, 0, w)), 0),
           lambda: sample((-w, -w, 0, 0, 0, w, w), 2) + [0]
           )
growth_points = []

def setup():
    size(500, 500)
    background(150)
    strokeWeight(2)
    growth_points.append(make_gp())

def make_gp():
    mover = choice(walkers)
    return [width / 2, height / 2, mover]

def draw():
    new_gps = []
    print len(growth_points)
    for gp in growth_points:
        x, y, mover = gp
        mx, my, _ = mover()
        gp[0] += mx
        gp[1] += my
        a, b = mx / 2, my / 2
        stroke((a * a + b * b) * 4)
        line(x, y, x + mx, y + my)
        
        for other in reversed(growth_points):
            if other is not gp and dist(x, y, other[0], other[1]) < w / 2: #sqrt(w):
                growth_points.remove(other) 
            
        if not 0 < x < width or not 0 < y < height:
             gp[0], gp[1] = width / 2, height / 2
            
        if frameCount % 200 == 0:
            new_gp = make_gp()
            gp[0], gp[1] = x - mx, y - my
            new_gps.append(new_gp)
            
            for _ in range(10):
                ex = int(random(width // w)) * w
                noStroke(); fill(150, 100)
                rect(ex, 0, w, height)
                
    growth_points.extend(new_gps)
