from __future__ import division

from itertools import product
from itertools import combinations
from random import choice

add_library('peasycam')

def setup():
    global nodes, nodes_set, pairs, quads
    size(600, 600, P3D)
    colorMode(HSB)
    cam = PeasyCam(this, 1000)
    row = range(-300, 301, 200)
    nodes = list(product(row, repeat=3))  
    nodes_set = set(nodes)
    pairs = [(a, b) for a, b in combinations(nodes, 2)
             if a[2] == b[2] 
             and (abs(a[0] - b[0]) <= 200
                ^ abs(a[1] - b[1]) <= 200)
             ]
    quads = generate_quads()
    
def generate_quads(n=9):
    quads = set()
    verticals = set()
    while len(quads) < n:
        a, b = choice(pairs)
        offset = choice((200, -200))
        if a[0] == b[0]:
            c = (a[0] + offset, a[1], a[2] + 200) 
            d = (b[0] + offset, b[1], b[2] + 200) 
        else:
            c = (a[0], a[1] + offset, a[2] + 200) 
            d = (b[0], b[1] + offset, b[2] + 200) 
        q = (a, b, d, c)
        centroid_xy = centroid(q)[:2]
        if (c in nodes_set and d in nodes_set
            and centroid_xy not in verticals):    
                quads.add(q) 
                verticals.add(centroid_xy)
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
        fill(centroid(q)[0] % 256, 255, 255, 200)
        beginShape()
        for x, y, z in q:
             vertex(x, y, z)
        endShape(CLOSE)

def node(x, y, z):
    pushMatrix()
    translate(x, y, z),
    box(10)
    popMatrix()
    
def centroid(points):
    xs, ys, zs = zip(*points)
    return (sum(xs) / len(xs),
            sum(ys) / len(ys),
            sum(zs) / len(zs)) 

def keyPressed():
    global quads
    quads = generate_quads()
    
    
