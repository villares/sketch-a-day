import random  # sample, shuffle, seed

nodes = {}
unvisited_nodes = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
SIN_60 = sqrt(3) / 2  # sin(radians(60))
W = 30
H = SIN_60 * W 
OX, OY = W / 2, H / 2  # deslocamento (offset)

def setup():
    size(900, 900)
    no_fill()
    start(2022)

def start(s):
    global rnd_seed
    rnd_seed = s
    random.seed(s)
    nodes.clear()
    unvisited_nodes[:] = []
    for _ in range(6):
        i, j = random.randint(-12, 12), random.randint(-12, 12)
        nodes[(i, j)] = (i, j, 0)
        unvisited_nodes.append((i, j))
    

def draw():
    background(240)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        ia, ja = n
        ib, jb, gen = v
        w = W * sqrt(gen + 1) / sqrt(W)
        stroke(0)
        xa, ya = ij_to_xy(ia, ja)
        xb, yb = ij_to_xy(ib, jb)
        fill(0, 255 - w * 15)
        if gen % 2:
            stroke_weight(2)
            line(xa, ya, xb, yb)
            circle(xa, ya, 3)
            circle(xb, yb, 3)
        stroke_weight(1)
        hexagon(xa, ya, w)
        #fill(255, 0, 0)
        #text(gen, xa, ya)
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

    for n, (i, j) in enumerate(unvisited_nodes):
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        _, _, gen = nodes[(i, j)]
        random.seed(min(6, n) + gen // 10)
        xnbs = random.sample(nbs, 4)
        random.shuffle(xnbs)
        for ni, nj in xnbs:
            ini, jnj= i + ni, j + nj
            if (ini, jnj) not in nodes and visible(ini, jnj):
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
        save_frame(f'{rnd_seed}.png')

def hexagon(xo, yo, r):
    with begin_closed_shape(): # começa a desenhar a forma
        for i in range(6):
            ang = i * TWO_PI / 6 
            x = xo + cos(ang) * r
            y = yo + sin(ang) * r 
            vertex(x, y)
     
