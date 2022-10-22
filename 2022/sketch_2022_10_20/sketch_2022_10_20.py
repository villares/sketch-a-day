import py5
import random  # sample, shuffle, seed

nodes = {}
unvisited_nodes = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))

W = 18
H = W * py5.sqrt(3) / 2  # sin(radians(60))
OX, OY = W / 2, H / 2  # deslocamento (offset)

def setup():
    py5.size(600, 600)
    generate(2022)

def draw():
    py5.background(240)
    py5.translate(py5.width / 2, py5.height / 2)
    draw_nodes()
    
def draw_nodes():
    for n, v in nodes.items():
        ia, ja, ka = n
        ib, jb, gen = v
        if ka % 2:
            py5.fill(200, 0, 0, 64)
        else:
            py5.fill(0, 0, 200, 64)

        w = py5.remap(gen, 0, 50, 0, W)
        xa, ya = ij_to_xy(ia, ja)
        xb, yb = ij_to_xy(ib, jb)
        py5.stroke_weight(min(abs(W / 30 + 3 - w / 5), 1))
        py5.line(xa, ya, xb, yb)
        hexagon(xa, ya, w)

def generate(s):
    global rnd_seed
    rnd_seed = s
    random.seed(s)
    print(f'seed: {s}')
    nodes.clear()
    unvisited_nodes[:] = []
    add_starting_points()
    previous_len_nodes = -1
    while previous_len_nodes != len(nodes):
        previous_len_nodes = len(nodes)
        unvisited_nodes[:] = grow()

def add_starting_points():
    for k in range(4):
        limit = py5.width // W // 2 - 1
        i = random.randint(-limit, limit)
        j = random.randint(-limit, limit)
        nodes[(i, j, k % 2)] = (i, j, 0)
        unvisited_nodes.append((i, j, k % 2))

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

def ij_to_xy(i, j):
    y = j * H + OY if i % 2 == 0 else j * H + H / 2 + OY
    x = i * W * 3 / 4 + OX
    return x, y

def visible(i, j):
    x, y = ij_to_xy(i, j)
    return (abs(x) < py5.width / 2 - W * 2 and
            abs(y) < py5.width / 2 - W * 2)  # square 

def hexagon(xo, yo, r):
    ang = py5.TWO_PI / 6
    with py5.begin_closed_shape():  # começa a desenhar a forma
         for i in range(6):
            py5.vertex(xo + py5.cos(i * ang) * r,
                       yo + py5.sin(i * ang) * r)

def key_pressed():
    if py5.key == ' ':
        generate(py5.frame_count)
    elif py5.key == 'a':
        add_starting_points()
    elif py5.key == 's':
        py5.save_frame(f'{rnd_seed}.png')

py5.run_sketch()

