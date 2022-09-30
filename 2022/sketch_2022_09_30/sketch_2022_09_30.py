# depends on py5 (py5coding.org) imported mode

import random  # import sample, shuffle, seed
from functools import lru_cache

nodes = {}
unvisited_nodes = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
W = 12
H = sqrt(3) * 0.5 * W 
nbs = []

palette =(
    color(0, 0, 100),
    color(100, 100, 0),
    color(0, 100, 100),
    color(100, 0, 100),
    color(100, 0, 0),
    color(0, 100, 0),
    )

def setup():
    size(800, 800)
    no_fill()
    start(268)

def start(rnd_seed):
    global s
    s = rnd_seed
    random_seed(rnd_seed)
    random.seed(rnd_seed)
    random.shuffle(nbs)
    nodes.clear()
    unvisited_nodes[:] = []
    for c in range(6):
        x1, y1 = random_int(-10, 10), random_int(-10, 10)
        unvisited_nodes.append((x1, y1, c))
    
def draw():
    background(200)
    translate(width / 2, height / 2)
    for (ia, ja, c), (ib, jb, gen, cc) in nodes.items():
            w = sin((gen + c) * 0.1 - radians(frame_count * 4)) * W 
            #fill(c, 255 - abs(w * 20))
            stroke(palette[cc % len(palette)])
            o =  w / 5 #; print(o)#(c % 3)- 1
            stroke_weight(2 - abs(o / 2))
            xa, ya = ij_to_xy(ia, ja)
            xb, yb = ij_to_xy(ib, jb)
            line(xa + o, ya + o, xb + o, yb + o)
            stroke_weight(1)
            circle(xa, ya, w * 2)
    unvisited_nodes[:] = list(grow(unvisited_nodes))
    if 145 > frame_count >= 100:
        save_frame(f'{frame_count - 100:02}.png', threading=True)
        print(frame_count)

@lru_cache   
def ij_to_xy(i, j):
    if i % 2 == 0:
        y = j * H * 2 + H
    else:
        y = j * H * 2 + H * 2
    x = i * W * 1.5 + W
    return x, y

def grow(unvisited_nodes):
    k = 0
    for i, j, c in unvisited_nodes:
        if not visible(i, j):
            continue
        _, _, gen, cc = nodes.get((i, j, c % 3), (0, 0, 0, k := k + 1))        
        random.seed(c + i // 10 + j // 5)
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        xnbs = random.sample(nbs, 3)
        for ni, nj in xnbs:
            ini, jnj= i + ni, j + nj
            if visible(ini, jnj) and (ini, jnj, c % 3) not in nodes:
                nodes[(ini, jnj, c % 3)] = (i, j, gen + 1, cc)
                yield (ini, jnj, c)
   
@lru_cache   
def visible(i, j):
    x, y = ij_to_xy(i, j) 
    return (abs(x) < width / 2 - W * 5 and
            abs(y) < height / 2 - W * 5)

def key_pressed():
    if key == ' ':
        print(frame_count)
        start(frame_count)
    elif key == 's':
        save_frame('###.png')

