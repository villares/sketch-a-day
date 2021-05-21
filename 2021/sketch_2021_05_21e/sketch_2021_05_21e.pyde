from itertools import combinations, product
from random import shuffle
from villares.arcs import arc_augmented_poly


def setup():
    global lerped_triangles,points, grid
    size(800, 800)
    colorMode(HSB)
    background(200)
    strokeWeight(3)
    grid = list(product(range(220, width-100, 180), repeat=2))
    tri_combo = combinations(grid, 3)
    points = [(a, b, c) for a, b, c in tri_combo
              if area(a, b, c)]
    # shuffle(points)
    lerped_triangles = []
    for k, ta in enumerate(points):
        tb = points[k - 1]
        for i in range(10):
            lt = lerp_tuple(tb, ta, (i + 1) / 10.0)
            lerped_triangles.append(lt + ((i + 1) * 25.5,))
    
def area(a, b, c): 
    return (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))

def draw():
    bckgnd = this.g.copy()
    background(200)
    translate(5, 5)
    image(bckgnd, 0, 0)
    translate(-5, -5)
    for x, y in grid:
        fill(128)
        circle(x, y, 15)
    va, vb, vc, h = lerped_triangles[frameCount % len(lerped_triangles)]
    draw_triangle(va, vb, vc, h)
    
def draw_triangle(va, vb, vc, h):
    if h == 255:
        fill(0, 255, 255)
    else:
        fill(255, 100)
    arc_augmented_poly((va, vb, vc), (15, 15, 15))

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))
    

    
    
    
    
