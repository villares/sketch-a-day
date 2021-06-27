from __future__ import division

from itertools import product
from itertools import combinations
from random import choice

add_library('peasycam')

def setup():
    global span, nodes, nodes_set, pairs, quads
    size(600, 600, P3D)
    colorMode(HSB)
    cam = PeasyCam(this, 1200)
    span = 120
    row = range(-300, 301, span)
    nodes = list(product(row, repeat=3))  
    nodes_set = set(nodes)
    x_pairs = [((x, y, z), (x + span, y, z)) for x, y, z in nodes
              if (x + span, y, z) in nodes_set]
    y_pairs = [((x, y, z), (x, y + span, z)) for x, y, z in nodes
              if (x, y  + span, z) in nodes_set]
    # z_pairs = [((x, y, z), (x, y, z + span)) for x, y, z in nodes
    #           if (x, y, z + span) in nodes_set]
    pairs = x_pairs + y_pairs 
    quads = generate_quads(span)
    
def generate_quads(span, n=25):
    quads = set()
    verticals = set()
    while len(quads) < n:
        a, b = choice(pairs)
        offset = choice((span, -span))
        if a[0] == b[0]:
            c = (a[0] + offset, a[1], a[2] + span) 
            d = (b[0] + offset, b[1], b[2] + span) 
        else:
            c = (a[0], a[1] + offset, a[2] + span) 
            d = (b[0], b[1] + offset, b[2] + span) 
        q = (a, b, d, c)
        centroid_xy = centroid(q)[:2]
        if (c in nodes_set and d in nodes_set
            and centroid_xy not in verticals):    
                quads.add(q) 
                verticals.add(centroid_xy)
    return quads        

def draw():
    # ortho()
    # scale(0.7)
    # rotateX(HALF_PI)
    background(200)
    fill(255)
    for x, y, z in nodes:
        node(x, y, z)
    for (xa, ya, za), (xb, yb, zb) in pairs:
        line(xa, ya, za, xb, yb, zb)
    for i, q in enumerate(quads):
        fill(centroid(q)[1] * 0.3 % 256, 255, 255, 200)
        beginShape()
        for x, y, z in q:
             vertex(x, y, z)
        endShape(CLOSE)

def node(x, y, z):
    pushMatrix()
    translate(x, y, z),
    box(5)
    popMatrix()
    
def centroid(points):
    xs, ys, zs = zip(*points)
    return (sum(xs) / len(xs),
            sum(ys) / len(ys),
            sum(zs) / len(zs)) 

def keyPressed():
    global quads
    quads = generate_quads(span)
    
    
