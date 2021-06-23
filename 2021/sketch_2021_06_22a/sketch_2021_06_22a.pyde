from itertools import product
from itertools import combinations

add_library('peasycam')

def setup():
    global nodes, pairs
    size(600, 600, P3D)
    cam = PeasyCam(this, 1000)
    row = range(-300, 301, 200)
    nodes = list(product(row, repeat=3))    
    pairs = [(a, b) for a, b
             in combinations(nodes, 2)
             if a[2] == b[2] 
             and abs(a[0] - b[0]) <= 200
             and abs(a[1] - b[1]) <= 200
             ]
def draw():
    rotateX(HALF_PI)
    background(200)
    fill(200, 0, 0)
    for x, y, z in nodes:
        node(x, y, z)
    for (xa, ya, za), (xb, yb, zb) in pairs:
        line(xa, ya, za, xb, yb, zb)
        
def node(x, y, z):
    pushMatrix()
    translate(x, y, z),
    box(10)
    popMatrix()
    
    
