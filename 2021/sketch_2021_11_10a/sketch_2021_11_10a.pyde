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
    strokeWeight(2)
    setup_seed(15406)  # 23698  
    start()
    
def start():
    nbs[:] = NBS
    shuffle(nbs)
    color_dict.update({nb:  color(i * 32, 255, 128)  # HSB color dict
                      for i, nb in enumerate(nbs)})  # for shuffled nbs
    nodes.clear()
    initial_nodes = {(int(random(-w, w)), int(random(-h, h))): None for _ in range(10)} 
    nodes.update(initial_nodes)     
       
def draw():
    background(240)
    # background(40, 140, 240)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        xa, ya = n
        if v:
            xb, yb, c = v
        else:
            continue
        stroke(c)
        line(xa * step, ya * step, xb * step, yb * step)
        noStroke()
        fill(c)
        circle(xa * step, ya * step, n_size * 2)
    
def keyPressed():
    if key == ' ':
        nbs[:] = NBS         # refresh, full neighbourhood
        for _ in range(8):   # 8 times 5 iteration steps
            nbs[:] = sample(NBS, max(2, len(nbs) - 1))
            for i in range(5):
                grow()
    elif key == ENTER:      
        setup_seed()
        start()
    elif key == 's':
        saveFrame('{}.png'.format(random_seed))
                
def grow():    
    nks = nodes.keys()
    # nks.sort()  # hmmm. not that nice
    shuffle(nks)
    for x, y in nodes.keys():
        for nx, ny in nbs:            
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
    
       
