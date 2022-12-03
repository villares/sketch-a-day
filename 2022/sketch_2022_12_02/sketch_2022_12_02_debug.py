from random import sample, seed, randint
from villares.helpers import save_png_with_src

nodes = {}
unvisited_nodes = []

polys = [[]]

EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))

#EVN_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2, -2), (2, -2))
#ODD_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2,  2), (2,  2))
W = 5
H = W * (3 ** 0.5) * 0.5


def setup():
    global w, h, canvas
    size(600, 600)
    w, h = int(width / 2 / W - 5), int(height / 2 / W - 5)
    start(268)
    color_mode(HSB)

    
def start(rnd_seed):
    global s
    s = rnd_seed
    seed(rnd_seed)
    nodes.clear()
    unvisited_nodes[:] = []
    for i in range(10):
        x, y = randint(-20, 20) * 1, randint(-20, 20) * 1
        unvisited_nodes.append((x, y))
        nodes[(x, y)] = (x, y, i, 1)
    

def tentar():
    if nodes:
        todos = list(nodes.items())
        k, v = todos.pop()
        #print(k, v)
        polys[-1].append(k)
        while k in nodes:
            ib, jb, c, gen = nodes.pop(k)
            k = ib, jb
            polys[-1].append(k)
        polys.append([])
        
def draw():
    background(240)
    translate(width / 2, height / 2)
    for n, v in nodes.items():
        ia, ja = n
        ib, jb, c, gen = v
        if visible(ia, ja) and visible(ib, jb):
            xa, ya = ij_to_xy(ia, ja)
            xb, yb = ij_to_xy(ib, jb)
            stroke(0)
            stroke_weight(1.5 + 1 * sin((gen - PI/2) * 0.1))
            line(xa, ya, xb, yb)
    if frame_count < 50: unvisited_nodes[:] = grow()
    no_fill()
    for i, pts in enumerate(polys):
        stroke(i * 64 % 255, 100, 8)
        if pts:
            #curve_vertex(*pts[0])
            fill(0)
            circle(*ij_to_xy(*pts[0]), 5)
            no_fill()
            begin_shape()
            for ia, ja in pts[::]:
                curve_vertex(*ij_to_xy(ia, ja))
            #curve_vertex(*pts[-1])
            end_shape()
            fill(255)
            circle(*ij_to_xy(*pts[-1]), 5)
        
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
        seed(gen // 2 + c)
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
    if key == 's':
        save_png_with_src()
    elif key == ' ':
        while nodes:
            tentar()