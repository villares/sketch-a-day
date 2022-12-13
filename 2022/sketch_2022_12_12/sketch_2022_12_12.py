import random  # sample, shuffle, seed
import py5     # https://py5coding.org
from villares.arcs import arc_augmented_poly as aap

nodes = {}
unvisited_nodes = []
step = 40
NBS = ((-1, -1), (-2, 0), (-1, 1), (0,-2),
      (0, 2), (1, -1), (2,0), (1, 1))

polys = []

COLORS = ( # PCD Coimbra colors!
    '#f2647a',
    '#eb9e5a',
    '#53c7ab',
    '#4955bf',
    '#8043d7'
    )

ox = oy = 0
save_pdf = False

def setup():
    global w, h, f
    py5.size(900, 900)
    w, h = int(py5.width / 2 / step - 5), int(py5.height / 2 / step - 5)
    start(100)

def start(rnd_seed):
    global s, nbs, colors
    s = rnd_seed
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    colors = list(COLORS) # I changed this, so not the same colors combos as in expo!
    random.shuffle(colors)
    nodes.clear()
    unvisited_nodes[:] = []
    x1, y1 = 0, 0
    unvisited_nodes.extend((
        (x1 + 0, y1 + random.randint(-3, 3)),
        (x1 + random.randint(-3, 3), y1 + 0),
        (x1 - 3, y1 + 3),
    ))



def draw():
    global save_pdf
    if save_pdf:
        py5.begin_record(py5.PDF, f'seed{s}.pdf')
    py5.stroke_weight(5)
    py5.background(0)
    py5.translate(py5.width / 2 + ox * step, py5.height / 2 + oy * step)
    unvisited_nodes[:] = grow()

    polys[:] = encontra_poligonos(nodes) 
    for i, pts in enumerate(polys):
        if pts:
            #cor = py5.color((128 + (i // 24) * 16) % 255, 250, 100)
            py5.no_fill()
            py5.stroke(100, 100)
            py5.stroke_weight(2)
            #draw_poly(pts)
            py5.stroke_weight(2)
            py5.stroke(colors[(i // 10) % 4])
            py5.no_fill()
            scaled_pts = [(x * step, y * step) for x, y in pts]
            aap(scaled_pts, radius=15)# + i * 0.5)
            py5.no_stroke()
            py5.fill(colors[(i // 10) % 4])
            py5.circle(*scaled_pts[0], 6)
            py5.circle(*scaled_pts[-1], 6)
    for n, v in nodes.items():
        xa, ya = n
        xb, yb, c, gen = v
#        if visible(xa, ya) and visible(xb, yb):
        py5.stroke(255)
        py5.line(xa * step, ya * step, xb * step, yb * step)

    if save_pdf:
        py5.end_record()
        py5.save(f'seed{s}.png')

        save_pdf = False


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
        xnbs = random.sample(nbs, 6 - c * 2)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c, gen + 1)
                yield xnx, yny

def visible(x, y):
    return (abs((x + ox) * step) < py5.width / 2 - step * 5 and
            abs((y + oy) * step) < py5.height / 2 - step * 5)

def key_pressed():
    global save_pdf
    if py5.key == ' ':
        start(s + 10)
    elif py5.key == 'p':
        save_pdf = True

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

