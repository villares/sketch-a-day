# https://tinyurl.com/feliz-natal-com-pyp5js
# Variante com tamanho da fonte variável https://tinyurl.com/feliz-natal-2022-abav

from random import seed, sample, randint
from random import shuffle as rnd_shu

texto = 'Feliz Natal'

NBS = ((-1, -1), (-2,  0), (-1, 1), (0, -2),
       (0,  2), (1, -1), (2, 0), (1,  1))

step = 8
rnd_seed = 32

nodes = {}
unvisited_nodes = []
message = {}

def setup():
    global img, rnd_seed
    
    size(windowWidth - 50, windowHeight - 100)
    colorMode(HSB, 255)
    noStroke()
    
    img = createGraphics(width, height)
    img.background(255)
    img.textAlign(CENTER, CENTER)
    img.fill(0)
    img.textFont('Mono', 150)
    img.text(texto, width / 2, height / 2)
    rnd_seed = 1000 * day() + 100 * minute() + second()
    
    global nbs, colors, orientation_offset
    w = int(width / 2 / step - 5)
    h = int(height / 2 / step - 5)

    seed(rnd_seed)
    nbs = list(NBS)
    rnd_shu(nbs)
    colors = {nb: color(i * 16, 200, 200)
              for i, nb in enumerate(nbs)}
    rnd_shu(nbs)
    orientation_offset = {nb: i * PI
                          for i, nb in enumerate(nbs)}
    unvisited_nodes[:] = [(randint(-w, w), randint(-h, h))
                          for _ in range(8)]

    for x in range(-w, w):
        for y in range(-h, h):
            if img.get(x * step + width / 2, y * step + height / 2)[0] != 0:
                message[(x, y)] = True

def draw():
    unvisited_nodes[:] = grow()

    background(0)
    #image(img, 0, 0)
    translate(width / 2, height / 2)
    for (x, y), (x0, y0, c, gen) in nodes.items():
        orientation = (x - x0, y - y0)  # delta/direction
        d = (2 + sin(gen / 5 + orientation_offset[orientation])) / 3
        if message.get((x, y)):
            fill(colors[orientation])
        else:
            d  += 0.5
            fill(255)
            #fill(hue(colors[orientation]), 255, 255)
        circle(x * step, y * step, d * step)
    textSize(30)
    fill(255)
    textFont('Mono')
    text('com pyp5js!', 50 - width / 2,  height / 2 - 30)

def grow():
    while unvisited_nodes:
        x, y = unvisited_nodes.pop()
        _, _, i, gen = nodes.get((x, y), (0, 0, len(unvisited_nodes), 0))
        if (abs(x * step) > width / 2 - step * 8 or
                abs(y * step) > height / 2 - step * 8):
            continue
        seed(rnd_seed + i)
        xnbs = sample(nbs, 5)
        for nx, ny in xnbs:
            xnx, yny = x + nx, y + ny
            if (xnx, yny) not in nodes:
                nodes[(xnx, yny)] = (x, y, i, gen + 1)
                yield xnx, yny




