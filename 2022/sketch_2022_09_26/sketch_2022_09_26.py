import random  # import sample, shuffle, seed

SIN_60 = sqrt(3) * 0.5  # sin(radians(60))

nodes = {}
unvisited_nodes = []
step = 8

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
W = 12
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
    for c in range(4):
        x1, y1 = random_int(-10, 10), random_int(-10, 10)
        unvisited_nodes.append((x1, y1, c))
    

def draw():
    background(200)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        ia, ja, c = n
        ib, jb, gen = v
        if visible(ia, ja) and visible(ib, jb):
            c =(
                color(0, 0, 100),
                color(100, 100, 0),
                color(0, 100, 0),
                color(100, 0, 100)
                )[c % 4]
            w = remap(gen, 1, 20, W, W / 3)
            #fill(c, 255 - abs(w * 20))
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
        i, j, c = unvisited_nodes.pop()
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        #if len(unvisited_nodes) > 100:
#         if is_mouse_pressed:
#             nbs = list(map(d, nbs))
        if not visible(i, j):
            continue
        _, _, gen = nodes.get((i, j, c), (0, 0, 0))
        random.seed(gen // 5 + c)
        xnbs = random.sample(nbs, 3)
        for ni, nj in xnbs:
            ini, jnj= i + ni, j + nj
            if (ini, jnj, c) not in nodes:
                nodes[(ini, jnj, c)] = (i, j, gen + 1)
                new_nodes.append((ini, jnj, c))
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

