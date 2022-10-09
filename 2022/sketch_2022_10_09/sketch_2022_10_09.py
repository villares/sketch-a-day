import py5
import random  # sample, shuffle, seed

nodes = {}
unvisited_nodes = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))

W = 25
H = W * py5.sqrt(3) / 2  # sin(radians(60))
OX, OY = W / 2, H / 2  # deslocamento (offset)

def setup():
    py5.size(1000, 1000)
    py5.no_fill()
    start(2022)

def start(s):
    global rnd_seed
    rnd_seed = s
    random.seed(s)
    nodes.clear()
    unvisited_nodes[:] = []
    add_starting_points()

def add_starting_points():
    for k in range(4):
        limit = py5.width / W / 2 - 1
        i = random.randint(-limit, limit)
        j = random.randint(-limit, limit)
        nodes[(i, j, k % 2)] = (i, j, 0)
        unvisited_nodes.append((i, j, k % 2))

def draw():
    py5.background(240)
    py5.translate(py5.width / 2, py5.height / 2)
    for n, v in nodes.items():
        ia, ja, ka = n
        ib, jb, gen = v
        #w = W - W * py5.sin(gen / 10) 
        w = py5.remap(gen, 0, 50, 0, W)
        py5.stroke(0)
        xa, ya = ij_to_xy(ia, ja)
        xb, yb = ij_to_xy(ib, jb)
        if gen < 40:
            py5.stroke_weight(W / 15)
            py5.line(xa, ya, xb, yb)
        py5.stroke_weight(W / 30)
        py5.fill(0, 255 - w * 15)
        hexagon(xa, ya, w)
    unvisited_nodes[:] = grow()


def ij_to_xy(i, j):
    if i % 2 == 0:
        y = j * H + OY
    else:
        y = j * H + H / 2 + OY
    x = i * W * 3 / 4 + OX
    return x, y

def grow():
    for i, j, k in unvisited_nodes:
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        _, _, gen = nodes[(i, j, k)]
        random.seed(k + gen // 10)
        xnbs = random.sample(nbs, 3)
        random.shuffle(xnbs)
        for ni, nj in xnbs:
            ini, jnj = i + ni, j + nj
            if (ini, jnj, k) not in nodes and visible(ini, jnj):
                nodes[(ini, jnj, k)] = (i, j, gen + 1)
                yield ini, jnj, k

def visible(i, j):
    x, y = ij_to_xy(i, j)
    return (abs(x) < py5.width / 2 - W * 2 and
            abs(y) < py5.height / 2 - W * 2)


def key_pressed():
    if py5.key == ' ':
        print(py5.frame_count)
        start(py5.frame_count)
    elif py5.key == 'a':
        add_starting_points()
    elif py5.key == 's':
        py5.save_frame(f'{rnd_seed}.png')

def hexagon(xo, yo, r):
    with py5.begin_closed_shape():  # começa a desenhar a forma
        for i in range(6):
            ang = i * py5.TWO_PI / 6
            x = xo + py5.cos(ang) * r
            y = yo + py5.sin(ang) * r
            py5.vertex(x, y)

py5.run_sketch()
