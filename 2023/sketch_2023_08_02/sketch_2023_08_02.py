import random  # sample, shuffle, seed
import py5     # https://py5coding.org

nodes = {}
nodes2 = {}
unvisited_nodes = []
un2 = []
step = 6
NBS = ((-2, -2), (-2, 0), (-2, 2), (0, -2),
       (0, 2), (2, -2), (2, 0), (2, 2))

COLORS = [py5.color(i * 64, 128, 255 - i * 32) for i in range(5)]

ox = oy = 10
save_pdf = False
grow_on = True

def setup():
    global w, h, f
    py5.size(750, 750)
    w, h = int(py5.width / 2 / step - 5), int(py5.height / 2 / step - 5)
    start(100)
    
def start(rnd_seed):
    global s, nbs, colors
    s = rnd_seed
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    colors = list(COLORS) 
    random.shuffle(colors)
    nodes.clear()
    unvisited_nodes[:] = []
    x1, y1 = -ox, -oy
    unvisited_nodes.extend((
        (x1 + 0, y1 + 1),
        (x1 + 1, y1 + 0),
        (x1, y1),
    ))
    un2[:] = []
    un2.extend((
        (x1 + 1, y1 + 0),
        (x1 - 1, y1 + 1),
        (x1, y1),
    ))

def draw():
    global save_pdf, ox, oy
    if save_pdf:
        py5.begin_record(py5.PDF, f'PCD-Coimbra-seed{s}.pdf')
    py5.stroke_weight(2)
    py5.background(250, 250, 240)
    py5.translate(py5.width / 2 + ox * step, py5.height / 2 + oy * step)
    for n, v in list(nodes.items()):
        xa, ya = n
        xb, yb, c, gen = v
        vis_a, vis_b = visible(xa, ya), visible(xb, yb)
        if vis_a and vis_b:
            py5.stroke(colors[c % 4])
            py5.line(xa * step, ya * step, xb * step, yb * step)
        elif not vis_a and not vis_b:
            del nodes[n]
    if grow_on:
        unvisited_nodes[:] = grow(unvisited_nodes, nodes)
        un2[:] = grow(un2, nodes2)
    if save_pdf:
        py5.end_record()
        save_pdf = False
    ox += 1
    print(len(unvisited_nodes), len(nodes))

def grow(unvisited_nodes, nodes):
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
    global save_pdf, grow_on
    if py5.key == 's':
        start(s + 10)
    elif py5.key == 'p':
        save_pdf = True
    elif py5.key == ' ':
        grow_on = not grow_on

py5.run_sketch()