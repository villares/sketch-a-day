import py5


import random  # sample, shuffle, seed
# import py5     # https://py5coding.org

from villares.helpers import save_png_with_src


NBS = ((-1, -1), (-2, 0), (-1, 1), (0, -2),
       (0, 2), (1, -1), (2, 0), (1, 1))
step = 8
rnd_seed = 350

nodes = {}
unvisited_nodes = []


#ox = oy = 0
#save_pdf = False


def setup():
    global w, h, f
    py5.size(900, 900)
    w, h = int(py5.width / 2 / step - 5), int(py5.height / 2 / step - 5)
    py5.color_mode(py5.HSB)
    py5.rect_mode(py5.CENTER)
    py5.no_stroke()
    start()

def start():
    global nbs, colors, orientation_offset
    nodes.clear()
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    unvisited_nodes[:] = []
    colors = {nb: py5.color(i * 16, 200, 200) for i, nb in enumerate(nbs)}
    random.shuffle(nbs)
    orientation_offset = {nb: i * py5.PI for i, nb in enumerate(nbs)}
    for _ in range(8):
        unvisited_nodes.append((random.randint(-w, w), random.randint(-h, h)))


def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2)
    unvisited_nodes[:] = grow()
    for (x, y), (x0, y0, c, gen) in nodes.items():
        orientation = (x - x0, y - y0)  # delta/direction
        py5.fill(colors[orientation])
        d = (2 + py5.sin(gen / 5 + orientation_offset[orientation])) / 3
        py5.circle(x * step, y * step, d * step)


def grow():
    print('grow')
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, c, gen = nodes.get((x, y), (0, 0, len(unvisited_nodes), 0))
        if (abs(x * step) > py5.width / 2 - step * 4 or
            abs(y * step) > py5.height / 2 - step * 4):
            continue
        random.seed(rnd_seed)
        xnbs = random.sample(nbs, 5)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c, gen + 1)
                yield xnx, yny


def key_pressed():
    global rnd_seed
    if py5.key == ' ':
        rnd_seed += 10
        start()
    elif str(py5.key) in 'sS':
        save_png_with_src(f'seed{rnd_seed}.png')


py5.run_sketch()
