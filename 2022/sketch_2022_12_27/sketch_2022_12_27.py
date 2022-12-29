import random  # sample, shuffle, seed
import py5     # https://py5coding.org

from villares.helpers import save_png_with_src

NBS = ((-2, -2), (-2,  0), (-2, 2), (0, -2),
       ( 0,  2), ( 2, -2), ( 2, 0), (2,  2))

step = 8
rnd_seed = 100
scale_factor = 4

ox = oy = 0

nodes = {}
unvisited_nodes = []
save_png = False
move = True

def setup():
    global w, h, f
    py5.size(900, 900)
    w, h = int(py5.width / 2 / step - 5), int(py5.height / 2 / step - 5)
    py5.color_mode(py5.HSB)
    py5.rect_mode(py5.CENTER)
    py5.no_stroke()
    start()
    f = py5.create_font('Source Code Pro Medium', 16)
    
def start():
    global nbs, colors, orientation_offset
    nodes.clear()
    random.seed(rnd_seed)
    nbs = list(NBS)
    random.shuffle(nbs)
    colors = {nb: py5.color(i * 16, 200, 200)
              for i, nb in enumerate(nbs)}
    random.shuffle(nbs)
    orientation_offset = {nb: i * py5.PI
                          for i, nb in enumerate(nbs)}
    unvisited_nodes[:] = []
    for _ in range(4):
        x = random.randint(-w, w) - ox // step
        y = random.randint(-h, h)
        unvisited_nodes.append((x, y))
        unvisited_nodes.append((x + 1, y + 1))
        unvisited_nodes.append((x + 1, y))
        unvisited_nodes.append((x , y + 1))

def draw():
    global ox, oy
    py5.background(0)
    py5.translate(py5.width / 2 + ox, py5.height / 2 + oy)
    unvisited_nodes[:] = grow()

    for (x, y), (x0, y0, c, gen) in nodes.items():
        orientation = (x - x0, y - y0)  # delta/direction
        py5.fill(colors[orientation])
        d = (2 + py5.sin(gen / 5 + orientation_offset[orientation])) / 3
        py5.circle(x * step, y * step, d * step)
    
    if move:
        ox -= step

def grow():
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, i, gen = nodes.get((x, y), (0, 0, len(unvisited_nodes), 0))
        if (abs(x * step) > -ox + py5.width / 2 - step * 8 or
            abs(y * step) > -oy + py5.height / 2 - step * 8):
            if (x, y) in nodes: nodes.pop((x, y))
            continue
        random.seed(rnd_seed + i)
        xnbs = random.sample(nbs, 5)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, i, gen + 1)
                yield xnx, yny

def key_pressed():
    global rnd_seed, move
    if py5.key == ' ':
        rnd_seed += 10
        start()
    elif str(py5.key) in 'sS':
        save_png_with_src(f'seed{rnd_seed}.png')
    elif py5.key == 'm':
        move = not move

py5.run_sketch()

