from itertools import product
from itertools import combinations
from random import choice

add_library('peasycam')

def setup():
    global nodes, pairs, quads
    size(600, 600, P3D)
    cam = PeasyCam(this, 1000)
    row = range(-300, 301, 200)
    nodes = list(product(row, repeat=3))    
    pairs = [(a, b) for a, b in combinations(nodes, 2)
             if a[2] == b[2] 
             and (abs(a[0] - b[0]) <= 200
                ^ abs(a[1] - b[1]) <= 200)
             ]

    quads = [(a, b, c, d) for (a, b), (d, c) in combinations(pairs, 2)
             if abs(a[2] - d[2]) == 200
             and abs(a[0] - c[0]) == 0
             and abs(a[1] - c[1]) == 200
             and abs(b[0] - d[0]) == 0
            ]
            
def draw():
    rotateX(HALF_PI)
    background(200)
    fill(200, 0, 0)
    for x, y, z in nodes:
        node(x, y, z)
    for (xa, ya, za), (xb, yb, zb) in pairs:
        line(xa, ya, za, xb, yb, zb)
    for i, q in enumerate(quads):
        beginShape()
        for x, y, z in q:
             vertex(x, y, z)
        endShape(CLOSE)
        
    
def node(x, y, z):
    pushMatrix()
    translate(x, y, z),
    box(10)
    popMatrix()
