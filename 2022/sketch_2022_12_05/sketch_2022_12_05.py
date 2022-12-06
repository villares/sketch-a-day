from random import sample, seed, randint, shuffle
from villares.helpers import save_png_with_src
from villares.arcs import arc_filleted_poly as afp

nodes = {}
unvisited_nodes = []

polys = []

EVN_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2, -2), (2, -2))
ODD_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2,  2), (2,  2))

#EVN_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2, -2), (2, -2))
#ODD_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2,  2), (2,  2))
W = 6
H = W * (3 ** 0.5) * 0.5

def setup():
    global w, h
    size(800, 800)
    w, h = int(width / 2 / W - 1), int(height / 2 / W - 1)
    start(1)
    color_mode(HSB)
    
def start(rnd_seed):
    global s
    s = rnd_seed
    seed(rnd_seed)
    nodes.clear()
    polys[:]=[]
    unvisited_nodes[:] = []
    for i in range(3):
        x, y = randint(-20, 20) * 1, randint(-20, 20) * 1
        unvisited_nodes.append((x, y))
        nodes[(x, y)] = (x, y, i, 1)
    

def gerar_poligonos():
    polys[:] = encontra_poligonos(nodes) 

        
def draw():
    background(240)
    translate(width / 2, height / 2)
    if len(nodes) < 6000: unvisited_nodes[:] = grow()
    gerar_poligonos()
    stroke_weight(2)
    for i, pts in enumerate(polys):
        stroke((128 + (i // 24) * 16) % 255, 250, 100)
        if pts:
            no_fill()
            draw_poly(pts)
            #scaled_pts = [ij_to_xy(*p) for p in pts]
            #afp(scaled_pts, radius=0, open_poly=True)
            fill(240)
            circle(*ij_to_xy(*pts[0]), 6)
            circle(*ij_to_xy(*pts[-1]), 6)
        
def draw_poly(pts):
    begin_shape()
    curve_vertex(*ij_to_xy(*pts[0]))
    for j, (ia, ja) in enumerate(pts[:]):
        if is_mouse_pressed: text(j, *ij_to_xy(ia, ja))
        curve_vertex(*ij_to_xy(ia, ja))
    curve_vertex(*ij_to_xy(*pts[-1]))
    end_shape()
        
def ij_to_xy(i, j):
    if i % 2 == 0:
        y = j * H * 2 + H
    else:
        y = j * H * 2 + H * 2
    x = i * W * 1.5 + W
    return x, y


def grow():
#    shuffle(unvisited_nodes)
#        for i, j in sorted(unvisited_nodes):

    for i, j in unvisited_nodes:
        if not visible(i, j):
            continue
        nbs = EVN_NBS if i % 2 == 0 else ODD_NBS
        #nbs = [(n[0] * 2, n[1] * 2) for n in nbs]
        _, _, c, gen = nodes[(i, j)]
        seed(gen // 2 + c)
        xnbs = sorted(sample(nbs, 3))
        #shuffle(xnbs)
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
    global s
    if key == 's':
        save_png_with_src()
    elif key == ' ':
        s += 1 
        start(s)

def encontra_poligonos(ns):
    todos = ns.copy()
    polys = []
    while todos:
        k, v = list(todos.items()).pop()
        ps = []
        ps.append(k)
        while k in todos:
            ib, jb, c, gen = todos.pop(k)
            k = ib, jb
            ps.append(k)
        polys.append(ps)
    return polys
