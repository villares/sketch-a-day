import random  # import sample, shuffle, seed
from villares.helpers import save_png_with_src
nodes = {}
unvisited_nodes = []
step = 8
NBS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
nbs = []
ox = oy = 0

def setup():
    global w, h
    size(800, 800)
    no_smooth()
    #color_mode(HSB)
    w, h = int(width / 2 / step - 5), int(height / 2 / step - 5)
    stroke_weight(2)
    start(257)

def start(rnd_seed):
    global fc, s
    s = rnd_seed
    fc = 0
    random.seed(rnd_seed)
    nbs[:] = NBS
    random.shuffle(nbs)
    nodes.clear()
    x1, y1 = random.randint(-w, w), random.randint(-h, h)
    x2, y2 = random.randint(-w, w), random.randint(-h, h)
    unvisited_nodes[:] = [(x1, y1), (x2, y2), ]  # (x3, y3)]


def draw():
    background(200)
    translate(width / 2 + ox * step, height / 2 + oy * step)
    for n, v in nodes.items():
        xa, ya = n
        xb, yb, c, g = v
        if visible(xa, ya) and visible(xb, yb):
            stroke(c)
            line(xa * step, ya * step, xb * step, yb * step)
    grow()


def key_pressed():
    if key == ' ':
        print(frame_count)
        start(frame_count)
    elif key == 's':
        save_png_with_src(f'seed{s}', timestamp=True)

def visible(x, y):
    return (abs((x + ox) * step) < width / 2 - step * 5 and
            abs((y + oy) * step) < height / 2 - step * 5)

def grow():
    global fc
    fc += 1
#     if fc % 70 == 0:
#         random.shuffle(unvisited_nodes)
    new_nodes = []
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, _, g = nodes.get((x, y), (0, 0, 0, 0))
        if not visible(x, y):
            new_nodes.append((x, y))
            continue
        random.seed(g // 13)
        # int(map(x, -w, w, 2, 7)))
        
        xnbs = random.sample(NBS, random.randint(3, 6))
        for nx, ny in xnbs:
            #c = random.choice((255, 255, 0, 64, 128))
            c = (255, 128, 64, 0)[3 - (g // 7) % 4]
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c, g + 1)
                new_nodes.append((xnx, yny))
    unvisited_nodes[:] = new_nodes
