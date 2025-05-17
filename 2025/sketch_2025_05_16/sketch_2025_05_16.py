import py5  # https://py5coding 
import random

rnd_seed = 1 

nodes = {}
unvisited_nodes = []
step = 6
NBS = (
   (-3, -3),
    (0,  -3),
    (3, -3),
     (-3,  0),           (3,  0),
    (-3,  3),
     (0, 3),
    (3,  3), 
)

PALETA = (
    py5.color(250, 100, 0, 150),
    py5.color(250, 250, 0, 150),
    py5.color(0, 100, 250, 150)
)

def setup():
    global w, h
    py5.size(1200, 400) 
    w, h = int(py5.width / 2 / step - 4), int(py5.height / 2 / step - 4)
    py5.no_loop()    
    
def draw():
    global nbs
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    paleta = list(PALETA)
    random.shuffle(paleta)
    # pontos iniciais
    x1, y1 = 0, 0
    unvisited_nodes.extend((
        (x1 + random.randint(-w, w), y1 + random.randint(-h, h)),
        (x1 + random.randint(-w, w), y1 + random.randint(-h, h)),
        (x1 + random.randint(-w, w), y1 + random.randint(-h, h)),
        ))
    # cresce a estrutura 
    nl = -1
    while nl != len(nodes):
        nl = len(nodes)
        unvisited_nodes[:] = grow(unvisited_nodes)
    # desenha a estrutura
    py5.stroke_weight(6)
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    for n, v in nodes.items():
        xa, ya = n
        xb, yb, c, gen = v
        if visible(xa, ya) and visible(xb, yb):
            py5.stroke(paleta[c % len(paleta)])
            py5.line(xa * step, ya * step, xb * step, yb * step)

    py5.save_frame(f'{rnd_seed}.png')

def grow(unvisited_nodes):
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        if not visible(x, y):
            continue
        _, _, c, gen = nodes.get((x, y), (0, 0, len(unvisited_nodes), 0))
        random.seed(gen // 11 + c + rnd_seed)
        xnbs = random.sample(nbs, 4)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c, gen + 1)
                yield xnx, yny

def visible(x, y):
    return (abs(x * step) < py5.width / 2 - step * 4 and
            abs(y * step) < py5.height / 2 - step * 4)

def key_pressed():
    global rnd_seed
    rnd_seed += 1
    nodes.clear()
    unvisited_nodes.clear()
    py5.redraw()
    
py5.run_sketch()

