from itertools import product
from random import sample, seed, shuffle

nodes = {}
step = 30
n_size = 2
NBS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
nbs = list(NBS)
color_dict = {}
sample_size = 3
zf = 1

def setup():
    global w, h
    size(800, 800, P3D)
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
    nodes[(5, 5, -4)] = None
    nodes[(-5, -5, 4)] = None
       
def draw():
    background(240)
    translate(width / 2, height / 2)
    rotateX(radians(mouseY))
    for n, v in nodes.items():
        xa, ya, za = n
        if v:        # v is origin + color
            xb, yb, zb, c = v
        else:        # v is None
            continue # skip inital nodes 
        stroke(c)
        line(xa * step, ya * step, za * step * zf,
             xb * step, yb * step, zb * step * zf,)
    for n, v in nodes.items():
        xa, ya, za = n
        noStroke()
        fill(0)
        push()
        translate(xa * step, ya * step, za * step * zf)
        box(n_size * 1.5)
        pop()
    if frameCount % 10 == 0: grow(frameCount // 40)
    
def keyPressed():
    if key == ENTER:      
        setup_seed()
        start()
    elif key == 's':
        saveFrame('{}.png'.format(random_seed))
                
def grow(s):    
    nks = nodes.keys()
    shuffle(nks)
    for x, y, z in nks:
        # seed(s + int(x / 20) + y / 20)
        seed(s + int(y / 20))
        xnbs = sample(NBS, int(map(x, -w, w, 2, 7)))
        for (nx, ny), nz in product(xnbs, [-1, 0, 1]):            
            xnx, yny, znz = x + nx, y + ny, z + nz
            visible = (abs(xnx * step) < width / 2 - step * 5 and
                       abs(yny * step) < height / 2 - step * 5
                       and -5 < znz < 5 )
            if visible and (xnx, yny, znz) not in nodes:
                c = color_dict[(nx, ny)]
                nodes[(xnx, yny, znz)] = (x, y, z, c)
   
# def mouseDragged():
#     i = (mouseX - width / 2) // step
#     j = (mouseY - height / 2) // step
#     nodes.update({(i, j, 0): None})     
      
def setup_seed(s=None):
    global random_seed
    if s is None:
        random_seed = int(random(100000))
    else:
        random_seed = s
    seed(random_seed)       # Python's random
    randomSeed(random_seed) # Processing's random
    print(random_seed)
