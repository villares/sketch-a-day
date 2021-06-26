from itertools import product
from itertools import combinations
from random import choice

add_library('peasycam')

def setup():
    global nodes, pairs, quads
    size(600, 600, P3D)
    colorMode(HSB)
    cam = PeasyCam(this, 1000)
    row = range(-300, 301, 200)
    nodes = set(product(row, repeat=3))    
    pairs = [(a, b) for a, b in combinations(nodes, 2)
             if a[2] == b[2] 
             and (abs(a[0] - b[0]) <= 200
                ^ abs(a[1] - b[1]) <= 200)
             ]
    quads = generate_quads()
    
def generate_quads(n=10):
    quads = set()
    while len(quads) < n:
        a, b = choice(pairs)
        c = (a[0], a[1], a[2] + 200)
        d = (b[0], b[1], b[2] + 200) 
        if c in nodes and d in nodes:
            quads.add((a, b, d, c))
    return quads        

def draw():
    rotateX(HALF_PI)
    background(200)
    fill(255)
    for x, y, z in nodes:
        node(x, y, z)
    for (xa, ya, za), (xb, yb, zb) in pairs:
        line(xa, ya, za, xb, yb, zb)
    for i, q in enumerate(quads):
        fill(i * 16, 255, 255, 200)
        beginShape()
        for x, y, z in q:
             vertex(x, y, z)
        endShape(CLOSE)
        
def node(x, y, z):
    pushMatrix()
    translate(x, y, z),
    box(10)
    popMatrix()
    
def keyPressed():
    global quads
    quads = generate_quads()
    
    
