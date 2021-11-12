from itertools import product
from random import sample, seed, shuffle

nodes = {}
step = 8
n_size = 2
NBS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
nbs = list(NBS)
color_dict = {}
sample_size = 3

def setup():
    global w, h
    size(1600, 800)
    colorMode(HSB)
    w = width / 2 / step - 5
    h = height / 2 / step - 5
    strokeWeight(4)
    setup_seed(15406)  # 23698  
    start()
    
def start():
    nbs[:] = NBS
    shuffle(nbs)
    color_dict.update({nb:  color(i * 32, 255, 128)  # HSB color dict
                      for i, nb in enumerate(nbs)})  # for shuffled nbs
    nodes.clear()
    # initial_nodes = {(int(random(-w, w)), int(random(-h, h))): None for _ in range(10)} 
    grid = product(range(2 - w, w, 20), range(2 - h, h, 30)) 
    initial_nodes = {(i, j): None for i, j in grid} 
    
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
    for n, v in nodes.items():
        xa, ya = n
        noStroke()
        fill(0)
        circle(xa * step, ya * step, n_size * 2)
    
def keyPressed():
    if key == ' ':
        nbs[:] = NBS         # refresh, full neighbourhood
        for i in range(10):   # 10 times 5 iteration steps
            s = int(random(10000))
            for _ in range(5):
                grow(s)
    elif key == ENTER:      
        setup_seed()
        start()
    elif key == 's':
        saveFrame('{}.png'.format(random_seed))
                
def grow(s):    
    nks = nodes.keys()
    shuffle(nks)
    for x, y in nks:
        # seed(s + int(x / 20) + y / 20)
        seed(s + int(y / 20))
        xnbs = sample(NBS, int(map(x, -w, w, 2, 7)))
        for nx, ny in xnbs:            
            xnx, yny = x + nx, y + ny
            visible = (abs(xnx * step) < width / 2 - step * 5 and
                       abs(yny * step) < height / 2 - step * 5 )
            if visible and (xnx, yny) not in nodes:
                c = color_dict[(nx, ny)]
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
