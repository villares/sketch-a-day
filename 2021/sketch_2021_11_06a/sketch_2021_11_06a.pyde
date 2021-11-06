from random import sample, seed, shuffle

nodes = {}
step = 10
n_size = 4
NBS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
nbs = NBS

def setup():
    size(600, 600)
    strokeWeight(2)
    setup_seed(14220)
    nodes.clear()
    nodes[(0, 0)] = (0, 0, 0)
            
def draw():
    background(240)
    # background(40, 140, 240)
    translate(width / 2, height / 2)
    
    for n, v in nodes.items():
        xa, ya = n
        xb, yb, c = v
        stroke(c)
        line(xa * step, ya * step, xb * step, yb * step)
    for n, v in nodes.items():
        xa, ya = n
        xb, yb, c = v
        noStroke()
        fill(0)
        circle(xa * step, ya * step, n_size)

def keyPressed():
    global nbs
    if key == ' ':
        nbs = sample(NBS, 4)
        c =  color(random(128) * 2, 0, 255)
        for _ in range(5):
            grow(c)
    elif key == ENTER:
        setup_seed()
        nodes.clear()
        nodes[(0, 0)] = (0, 0, 0)
                
def grow(c):    
    nks = nodes.keys()
    shuffle(nks)
    for x, y in nodes.keys():
        for nx, ny in nbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c)
  
def setup_seed(s=None):
    global random_seed
    if s is None:
        random_seed = int(random(100000))
    else:
        random_seed = s
    seed(random_seed)       # Python's random
    randomSeed(random_seed) # Processing's random
    print(random_seed)
    
