# Baseado do sketch 2021_11_15a atualizada para py5

from random import sample, seed, shuffle, randint
from py5_tools import animated_gif

nodes = {}
unvisited_nodes = []                   
step = 8

D_NBS = ((-1, -1), (1, 1), (-1, 1), (1, -1))
O_NBS = ((0, 1), (0, -1), (1, 0), (-1, 0))
nbs = []

color_dict = {}
seed_step = 20
INSTANT_GROWTH = True

def setup():
    global w, h
    size(800, 800, P3D)
    w = width / 2 / step - 2
    h = height / 2 / step - 2
    color_mode(HSB)
    seed_and_start(5)  # set global rnd_seed and starts growth
    animated_gif('out.gif', frame_numbers=range(180, 360 + 180, 10), duration=0.2, optimize=True)
    
def seed_and_start(s):
    global rnd_seed
    seed(s)
    rnd_seed = s
    print(rnd_seed)

    nbs[:] = O_NBS + D_NBS
    shuffle(nbs)
    color_dict.update({nb:  color(i * 32, 255, 128)  # HSB color dict
                      for i, nb in enumerate(nbs)})  # for shuffled nbs
    nodes.clear()
    unvisited_nodes[:] = [(randint(-w, w), randint(-h, h))
                              for _ in range(4)]
       
def draw():
    background(240)
    ortho()
    stroke_weight(2)
    translate(width / 2, height / 2)
    rotate_y(radians(30) * sin(radians(frame_count)))
    for n, v in nodes.items():
        xa, ya = n
        if v:        # v is origin + color
            xb, yb, c, za = v
            _, _, _, zb = nodes.get((xb, yb), (0, 0, 0, 0))
        else:        # v is None
            continue # skip inital nodes 
        #no_stroke()
        # stroke(c)
        line(
            xa * step, ya * step, za * step,
            xb * step, yb * step, zb * step,
             )

    if INSTANT_GROWTH:
        nl = -1
        while nl != len(nodes):
            nl = len(nodes)
            unvisited_nodes[:] = grow()
    else:
        unvisited_nodes[:] = grow()

def key_pressed():
    global seed_step
    if key == ' ':
        seed_and_start(rnd_seed + 1)
    elif key == '-':
        seed_step += 5
        seed_and_start(rnd_seed)
        
    elif key == 's':
        save_frame('###.png')
                
def grow():
    NBS = O_NBS * 2 + D_NBS
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, _, z = nodes.get((x, y), (0, 0, 0, 0))
        seed(len(unvisited_nodes) // (seed_step * 2) + int(y / seed_step) + int(x / (seed_step * 2)))
        xnbs = sample(NBS, randint(5, 7))
        for nx, ny in xnbs:            
            xnx, yny = x + nx, y + ny
            visible = ( #dist(xnx, yny, 0, 0) < 100
                (abs(xnx * step) < width / 2 - step * 1 and
                 abs(yny * step) < height / 2 - step * 1 )
                     )
            if visible and (xnx, yny) not in nodes:
                c = color_dict[(nx, ny)]
                nodes[(xnx, yny)] = (x, y, c, z + 1)
                yield xnx, yny
                
def my_box(x, y, z, w):
    with push_matrix():
        translate(x, y, z)
        box(w)
      

