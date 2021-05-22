from itertools import combinations, product
from random import shuffle
from villares.arcs import arc_augmented_poly
from villares.gif_export import gif_export
add_library('gifAnimation')

def setup():
    global points
    size(800, 800, P2D)
    # frameRate(2) 
    background(200)
    fill(255, 100)
    strokeJoin(ROUND)
    strokeWeight(3)
    grid = list(product(range(220, width-100, 180), repeat=2))
    tri_combo = combinations(grid, 3)
    points = [(a, b, c) for a, b, c in tri_combo
              if area(a, b, c)]
    shuffle(points)
    print(len(points))

def area(a, b, c): 
    return (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))

def draw():
    bckgnd = this.g.copy()
    background(200)
    translate(50, 50)
    # bckgnd.filter(INVERT)
    image(bckgnd, 0, 0)
    translate(-50, -50)
    tri_a = points[frameCount % len(points)]
    tri_b = points[(frameCount  + 1) % len(points)]
    for i in range(10):
        fill(i * 28, 200)
        va, vb, vc = lerp_tuple(tri_b, tri_a, (i + 1) / 10.0)
        draw_triangle(va, vb, vc)
        translate(-5, -5)
    if frameCount > 5:
        # if frameCount % 3 == 0:
            gif_export(GifMaker, "fun")
    if frameCount > 5 + 76:
        gif_export(GifMaker, finish=True)
    print(frameCount)
        
    
def draw_triangle(va, vb, vc):
    arc_augmented_poly((va, vb, vc), (15, 15, 15))

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))
    

    
    
    
    
