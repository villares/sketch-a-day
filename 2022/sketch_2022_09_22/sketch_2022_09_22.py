import random  # import sample, shuffle, seed

SIN_60 = sqrt(3) * 0.5  # sin(radians(60))

nodes = {}
unvisited_nodes = []
EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
W = 6
H = SIN_60 * W 
nbs = []

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
    for _ in range(4):
        x1, y1 = random_int(-20, 20), random_int(-20, 20)
        unvisited_nodes.append((x1, y1))
    

def draw():
    background(0)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        ia, ja = n
        ib, jb, c, gen = v
        if visible(ia, ja) and visible(ib, jb):
            c =(
                color(0, 0, 128),
                color(0, 128, 0),
                color(0, 128, 128),
                color(128, 128, 0)
                )[c % 4]
            w = remap(gen, 1, 20, W, W / 3)
            fill(c, 255 - abs(w * 20))
            stroke(c)
            xa, ya = ij_to_xy(ia, ja)
            xb, yb = ij_to_xy(ib, jb)
            line(xa, ya, xb, yb)
            hexagon(xa, ya, w)
    grow()

def ij_to_xy(i, j):
    if i % 2 == 0:
        y = j * H * 2 + H
    else:
        y = j * H * 2 + H * 2
    x = i * W * 1.5 + W
    return x, y

def d(n): return n[0] * 2, n[1] * 2

def grow():
    new_nodes = []
    while unvisited_nodes:
        i, j = unvisited_nodes.pop()
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        #if len(unvisited_nodes) > 100:
        nbs = list(map(d, nbs))
        if not visible(i, j):
            continue
        _, _, c, gen = nodes.get((i, j), (0, 0, len(unvisited_nodes), 0))
        random.seed(gen // 13 + c)
        xnbs = random.sample(nbs, 4)
        for ni, nj in xnbs:
            ini, jnj= i + ni, j + nj
            if (ini, jnj) not in nodes:
                nodes[(ini, jnj)] = (i, j, c, gen + 1)
                new_nodes.append((ini, jnj))
    unvisited_nodes[:] = new_nodes
    
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

def hexagon(x, y, w):
    h = SIN_60 * w
    with push_matrix():
        translate(x, y)
        with begin_shape():
            vertex(-w, 0)
            vertex(-w / 2, -h)
            vertex(w / 2, -h)
            vertex(w, 0)
            vertex(w - w / 2, h)
            vertex(-w / 2, h)
            vertex(-w, 0)

