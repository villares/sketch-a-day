from itertools import product
from random import sample, seed, shuffle

nodes = {}
unvisited_nodes = []                   
step = 8
n_size = 2
NBS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
nbs = list(NBS)
color_dict = {}
sample_size = 3

def setup():
    global w, h
    size(1600, 800, FX2D)
    colorMode(HSB)
    noSmooth()
    w = width / 2 / step - 5
    h = height / 2 / step - 5
    strokeWeight(2)
    setup_seed(1)   
    start()
    
def start(seeds=False):
    nbs[:] = NBS
    shuffle(nbs)
    # color_dict.update({nb:  color(i * 32, 255, 128)  # HSB color dict
    #                   for i, nb in enumerate(nbs)})  # for shuffled nbs
    color_dict.update({(i, j):  color(128 + (i + j) * 16, 200, 100)  # HSB color dict
                      for n, (i, j) in enumerate(NBS)})  # for shuffled nbs
    nodes.clear()
    if seeds:
        unvisited_nodes[:] = [(int(random(-w, w)), int(random(-h, h)))
                              for _ in range(4)]
    else:
        unvisited_nodes[:] = []
        
       
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
    grow(frameCount // 50)
    
def keyPressed():
    if key == ' ':
        setup_seed()
        start(seeds=True)
    if key == ENTER:
        start()
    elif key == 's':
        saveFrame('{}.png'.format(random_seed))
                
def grow(s):
    new_nodes = []   
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        seed(s + int(y / 25))
        xnbs = sample(NBS, int(random(5, 7)))# int(map(x, -w, w, 2, 7)))
        for nx, ny in xnbs:            
            xnx, yny = x + nx, y + ny
            visible = (abs(xnx * step) < width / 2 - step * 5 and
                       abs(yny * step) < height / 2 - step * 5 )
            if visible and (xnx, yny) not in nodes:
                c = color_dict[(nx, ny)]
                nodes[(xnx, yny)] = (x, y, c)
                new_nodes.append((xnx, yny))
    unvisited_nodes[:] = new_nodes
      
def mouseDragged():
    i = (mouseX - width / 2) // step
    j = (mouseY - height / 2) // step
    if (i, j) not in nodes:
        nodes.update({(i, j): None})     
        unvisited_nodes.append((i, j))
      
def setup_seed(s=None):
    global random_seed
    if s is None:
        random_seed = int(random(100000))
    else:
        random_seed = s
    seed(random_seed)       # Python's random
    randomSeed(random_seed) # Processing's random
    print(random_seed)
