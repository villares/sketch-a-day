import random  # sample, shuffle, seed
import py5     # https://py5coding.org
from villares.arcs import arc_augmented_poly as aap
from villares.helpers import save_png_with_src

nodes = {}
unvisited_nodes = []
step = 20
NBS = ((-1, -1), (-1, 0), (-1, 1), (0,-1),
      (0, 1), (1, -1), (1,0), (1, 1))

polys = []

ox = oy = 0
save_pdf = False

def setup():
    global w, h, f
    py5.size(900, 900)
    w, h = int(py5.width / 2 / step - 5), int(py5.height / 2 / step - 5)
    start(100)
    py5.color_mode(py5.HSB)

def start(rnd_seed):
    global s, nbs
    s = rnd_seed
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    nodes.clear()
    unvisited_nodes[:] = []
    for _ in range(2):
        unvisited_nodes.append((random.randint(-w, w), random.randint(-h, h)))



def draw():
    global save_pdf

    py5.stroke_weight(5)
    py5.background(200)
    py5.translate(py5.width / 2 + ox * step, py5.height / 2 + oy * step)
    unvisited_nodes[:] = grow()

    polys[:] = encontra_poligonos(nodes)
    py5.no_fill()

    py5.fill(255, 100)
    py5.stroke_weight(2)
    py5.stroke(255)
    for pts in polys[1::2]:
        draw_stuff(pts)

    py5.fill(0, 100)
    py5.stroke(0)
    py5.stroke_weight(1)
    for pts in polys[::2]:
        draw_stuff(pts)
    
def draw_stuff(pts):
    if pts:
        py5.push()
        py5.no_fill()
        draw_poly(pts)
        py5.pop()
        scaled_pts = [(x * step, y * step) for x, y in pts]
        aap(scaled_pts, radius=step/3)

def draw_poly(pts):
    py5.begin_shape()
    #curve_vertex(*ij_to_xy(*pts[0]))
    for j, (ia, ja) in enumerate(pts[:]):
         py5.vertex(ia * step, ja * step)
    #curve_vertex(*ij_to_xy(*pts[-1]))
    py5.end_shape()
        
        

def grow():
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, c, gen = nodes.get((x, y), (0, 0, len(unvisited_nodes), 0))
        if not visible(x, y):
            continue
        random.seed(gen // 13 + c)
        xnbs = random.sample(nbs, 5)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c, gen + 1)
                yield xnx, yny

def visible(x, y):
    return (abs((x + ox) * step) < py5.width / 2 - step * 3 and
            abs((y + oy) * step) < py5.height / 2 - step * 3)

def key_pressed():
    global save_pdf
    if py5.key == ' ':
        start(s + 10)
    elif py5.key == 's':
        save_png_with_src(f'seed{s}.png')
    

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

py5.run_sketch()

