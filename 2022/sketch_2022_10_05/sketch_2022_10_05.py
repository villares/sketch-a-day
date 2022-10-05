import random  # import sample, shuffle, seed


nodes = {}
unvisited_nodes = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
SIN_60 = sqrt(3) / 2 # sin(radians(60))
W = 30
H = SIN_60 * W 
OX, OY = W / 2, H / 2  # deslocamento (offset)

def setup():
    global w, h
    size(900, 900)
    no_fill()
    w, h = int(width / 2 / W - 5), int(height / 2 / W - 5)
    start(268)

    
def start(rnd_seed):
    random.seed(rnd_seed)
    nodes.clear()
    unvisited_nodes[:] = []
    for _ in range(4):
        x1, y1 = random.randint(-10, 10), random.randint(-10, 10)
        unvisited_nodes.append((x1, y1))
    

def draw():
    background(240)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        ia, ja = n
        ib, jb, gen = v
        if visible(ia, ja) and visible(ib, jb):
            w = W * sqrt(gen) / sqrt(W)
            fill(0, 255 - w * 15)
            stroke(0)
            xa, ya = ij_to_xy(ia, ja)
            xb, yb = ij_to_xy(ib, jb)
            stroke_weight(2)
            line(xa, ya, xb, yb)
            stroke_weight(1)
            hexagon(xa, ya, w)
    grow()

def ij_to_xy(i, j):
    if i % 2 == 0:
        y = j * H  + OY
    else:
        y = j * H + H / 2 + OY
    x = i * W * 3 / 4 + OX
    return x, y

def grow():
    new_nodes = []
    while unvisited_nodes:
        i, j = unvisited_nodes.pop()
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        #if len(unvisited_nodes) > 100:
        if not visible(i, j):
            continue
        _, _, gen = nodes.get((i, j), (0, 0, 0))
        #random.seed(gen // 13 + c)
        random.seed(i + j)
        xnbs = random.sample(nbs, 4)
        for ni, nj in xnbs:
            ini, jnj= i + ni, j + nj
            if (ini, jnj) not in nodes:
                nodes[(ini, jnj)] = (i, j, gen + 1)
                new_nodes.append((ini, jnj))
    unvisited_nodes[:] = new_nodes
    
def visible(i, j):
    x, y = ij_to_xy(i, j) 
    return (abs(x) < width / 2 - W * 2 and
            abs(y) < height / 2 - W * 2)

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

