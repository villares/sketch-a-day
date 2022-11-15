from random import sample, seed, randint
from villares.helpers import save_png_with_src

nodes = {}
unvisited_nodes = []

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
W = 6
H = W * (3 ** 0.5) * 0.5


def setup():
    global w, h
    size(800, 800)
    w, h = int(width / 2 / W - 5), int(height / 2 / W - 5)
    start(268)


def start(rnd_seed):
    global s
    s = rnd_seed
    seed(rnd_seed)
    nodes.clear()
    unvisited_nodes[:] = []
    for i in range(4):
        x, y = randint(-20, 20), randint(-20, 20)
        unvisited_nodes.append((x, y))
        nodes[(x, y)] = (x, y, i, 1)


def draw():
    background(240)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        ia, ja = n
        ib, jb, c, gen = v
        if visible(ia, ja) and visible(ib, jb):
            stroke((
                color(0, 0, 128),
                color(0, 128, 0),
                color(0, 0, 0),
                color(0, 64, 64)
            )[c % 4])
            xa, ya = ij_to_xy(ia, ja)
            xb, yb = ij_to_xy(ib, jb)
            stroke_weight(max(1, 6 / sqrt(gen)))
            line(xa, ya, xb, yb)
    unvisited_nodes[:] = grow()


def ij_to_xy(i, j):
    if i % 2 == 0:
        y = j * H * 2 + H
    else:
        y = j * H * 2 + H * 2
    x = i * W * 1.5 + W
    return x, y


def grow():
    for i, j in unvisited_nodes:
        if not visible(i, j):
            continue
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        #nbs = [(n[0] * 2, n[1] * 2) for n in nbs]
        _, _, c, gen = nodes[(i, j)]
        seed(gen // 5 + c)
        xnbs = sample(nbs, 3)
        for ni, nj in xnbs:
            ini, jnj = i + ni, j + nj
            if (ini, jnj) not in nodes:
                nodes[(ini, jnj)] = (i, j, c, gen + 1)
                yield ini, jnj


def visible(i, j):
    x, y = ij_to_xy(i, j)
    return (abs(x) < width / 2 - W * 5 and
            abs(y) < height / 2 - W * 5)


def key_pressed(e):
    if key == ' ':
        start(frame_count)
    elif key == 's':
        save_png_with_src()