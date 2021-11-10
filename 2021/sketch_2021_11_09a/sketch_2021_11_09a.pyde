from random import sample, seed, shuffle

nodes = {}
step = 8
n_size = 2
NBS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
nbs = list(NBS)
sample_size = 3

def setup():
    global w, h
    size(1600, 800)
    w = width / 2 / step - 1
    h = height / 2 / step - 1
    strokeWeight(2)
    setup_seed(15406)  # 23698  
    start()
    
def start():
    nodes.clear()
    initial_nodes = {(int(random(-w, w)), int(random(-h, h))): None for _ in range(10)} 
    nodes.update(initial_nodes)
        
def draw():
    background(240)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        xa, ya = n
        if v:        # v is origin + color
            xb, yb, c = v
        else:        # v is None
            continue # skip inital nodes 
        stroke(c)
        line(xa * step, ya * step, xb * step, yb * step)
        noStroke()
        fill(c)
        circle(xa * step, ya * step, n_size * 2)
    
def keyPressed():
    global nbs
    if key == ' ':
        nbs = NBS
        for _ in range(8):
            nbs = sample(NBS, max(2, len(nbs) - 1))
            for i in range(5):
                grow()
    elif key == ENTER:
        nbs = list(NBS)
        setup_seed()
        start()
    elif key == 's':
        saveFrame('{}.png'.format(random_seed))
                
def grow():    
    for x, y in nodes.keys():  # maybe I should shuffle these...
        for i, (nx, ny) in enumerate(nbs):
            c = color(0, i * 10, 128 - i * 16)
            xnx, yny = x + nx, y + ny
            visible = (abs(xnx * step) < width / 2 - step and
                       abs(yny * step) < height / 2 - step )
            if visible and (xnx, yny) not in nodes:
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
    
       
