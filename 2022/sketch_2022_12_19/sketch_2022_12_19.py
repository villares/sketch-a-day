import random  # sample, shuffle, seed
import py5     # https://py5coding.org

from villares.helpers import save_png_with_src

nodes = {}
unvisited_nodes = []
step = 10
NBS = ((-1, -1), (-1, 0), (-1, 1), (0,-1),
      (0, 1), (1, -1), (1,0), (1, 1))


ox = oy = 0
save_pdf = False

def setup():
    global w, h, f
    py5.size(900, 900)
    w, h = int(py5.width / 2 / step - 5), int(py5.height / 2 / step - 5)
    start(140)
    py5.color_mode(py5.HSB)

def start(rnd_seed):
    global s, nbs, colors, directions_offset
    s = rnd_seed
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    nodes.clear()
    unvisited_nodes[:] = []
    colors = {nb: i * 16 for i, nb in enumerate(nbs)}
    random.shuffle(nbs)
    directions_offset = {nb: i * py5.PI for i, nb in enumerate(nbs)}
    for _ in range(8):
        unvisited_nodes.append((random.randint(-w, w), random.randint(-h, h)))

def draw():
    py5.background(0)
    py5.translate(py5.width / 2 + ox * step, py5.height / 2 + oy * step)
    unvisited_nodes[:] = grow()
    for (x, y), (x0, y0, c, gen) in nodes.items():
        d = (x - x0, y - y0)  # delta/direction
        py5.fill(colors[d], 200, 200)
        diameter = step / 2 + step / 3 * py5.sin(gen / 5 + directions_offset[d])
        if py5.is_key_pressed:
            py5.stroke(255)
            py5.line(x * step, y * step, x0 * step, y0 * step)
        py5.no_stroke()
        py5.circle(x * step, y * step, diameter)

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
    if py5.key == ' ':
        start(s + 10)
    elif py5.key == 's':
        save_png_with_src(f'seed{s}.png')
    


py5.run_sketch()