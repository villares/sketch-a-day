from itertools import permutations, product

def setup():
    global points
    size(800, 800, P2D)
    background(200)
    grid = list(product(range(220, width-100, 180), repeat=2))
    tri_perm = permutations(grid, 3)
    points = [(a, b, c) for a, b, c in tri_perm
              if area(a, b, c)]
    frameRate(20) 
    print(len(points))

def area(a, b, c): 
    return (a[0] * (b[1] - c[1]) +
            b[0] * (c[1] - a[1]) +
            c[0] * (a[1] - b[1]))

def draw():
    bckgnd = this.g.copy()
    background(200),
    translate(10, 10)
    image(bckgnd, 0, 0)
    translate(-10, -10)
    vr, vg, vb = points[frameCount % len(points)]
    beginShape()
    fill(200, 0, 0)
    vertex(vr[0], vr[1])
    fill(0, 200, 0)
    vertex(vg[0], vg[1])
    fill(0, 0, 200)
    vertex(vb[0], vb[1])
    endShape(CLOSE)
    
    
    
    
