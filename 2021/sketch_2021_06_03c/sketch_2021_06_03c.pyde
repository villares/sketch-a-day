from itertools import product, combinations, permutations
from random import sample 

def setup():
    global grade, rects
    size(500, 500)
    grade = list(product(range(50, 500, 100), repeat=2))    
    frameRate(2)
    # all_polys = permutations(grade, 4)

        
def draw():
    colorMode(RGB)
    # background(200, 200, 180)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    fill(255, 100)
    
    a, b, c, d = sample(grade, 4)
    
    for i in range(20):
        t = i / 19.0
        m, n = lerpPoints((a, b), (c, d), t)
        line(m[0], m[1], n[0], n[1])          

    ab = degrees(atan2(a[1] - b[1], a[0] - b[0]))
    cd = degrees(atan2(c[1] - d[1], c[0] - d[0]))
    p = abs(ab - cd)


def lerpPoints(points_a, points_b, t):
    return [(lerp(a[0], b[0], t),
             lerp(a[1], b[1], t))
            for a, b in zip(points_a, points_b)]
