from random import sample, shuffle, seed
import py5_tools

nodes = {}
unvisited_nodes = []
step = 8
NBS = (
    (-2, -2), (-1,  0),
    (-2,  2), ( 0, -1),
    ( 0,  1), ( 2, -2),
    ( 1,  0), ( 2,  2)
)
nbs = []
ox = oy = 0
def setup():
    global w, h
    size(800, 800)
    #no_smooth()
    w, h = int(width / 2 / step - 5), int(height / 2 / step - 5)
    start(268)
    no_fill()
    
def start(rnd_seed):
    global s
    s = rnd_seed
    seed(s)
    random_seed(s)
    nbs[:] = NBS
    shuffle(nbs)
    nodes.clear()
    unvisited_nodes[:] = []
    x1, y1 = 0, 0
    unvisited_nodes.extend((int(random(-20, 21)),int(random(-20, 21)))
                           for _ in range(9))
    py5_tools.animated_gif(
        sketch_path() / f'animated-seed{s}.gif',
        50, 0.25, 0.25, loop=0, optimize=True)



def draw():
    background(200)
    translate(width / 2 + ox * step, height / 2 + oy * step)
    for n, v in nodes.items():
        xa, ya = n
        xb, yb, c, gen = v
        if visible(xa, ya) and visible(xb, yb):
            stroke((
                color(128, 0, 0),
                color(0, 128, 0),
                color(0, 0, 128)
                )[c % 3])
            circle(xa * step, ya * step, sqrt(gen) * 2)
            line(xa * step, ya * step, xb * step, yb * step)
    unvisited_nodes[:] = grow()

def grow():
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, c, gen = nodes.get((x, y), (0, 0, len(unvisited_nodes), 0))
        seed(gen // 13 + c)
        xnbs = sample(nbs, 5)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, c, gen + 1)
                if visible(xnx, yny):
                    yield xnx, yny
    
    
def visible(x, y):
    return (abs((x + ox) * step) < width / 2 - step * 5 and
            abs((y + oy) * step) < height / 2 - step * 5)

def key_pressed():
    if key == ' ':
        start(frame_count)
