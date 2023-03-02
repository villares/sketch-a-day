from itertools import combinations, product

combos = []

def setup():
    size(600, 600, P3D)
    n = 6
    step = TWO_PI / n
    pts = list(product((-250, 250), repeat=3))
    combos[:] = [(a, b) for a, b in combinations(pts, 2)
                 if dist(*a, *b) < 708]
  
def draw():
    #ortho()
    background(200)
    translate(300, 300, -300)
    rotate_y(mouse_x / 12)
    rotate_x(mouse_y / 12)
    stroke_weight(3)
    for c, s in (('yellow', True), ('darkblue', False)):  
        stroke(c)
        for (ax, ay, az), (bx, by, bz) in combos:
            dashed(ax, ay, az, bx, by, bz, solid_start=s)
    rotate_x(QUARTER_PI)


def dashed(ax, ay, az, bx, by, bz, dash=20, solid_start=True):
    a = Py5Vector(ax, ay, az)
    b = Py5Vector(bx, by, bz)    
    v = b - a
    d = v.mag
    if d:
        uv = v.norm # A "unit vector" of the line
        n = d // (uv.mag * dash)
        if n == 0:
           solid_start = True  
        elif n % 2 == 0:
           n = n - 1            
        small_dash = d - n * dash
        start = a + uv * small_dash / 2
        if solid_start:
            line(*a, *start) 
        for i in range(int(n)):
            if i % 2 == (1 if solid_start else 0):
                end = start + uv * dash
                line(*start, *end)
            start += uv * dash
        if solid_start:
            line(*start, *b)