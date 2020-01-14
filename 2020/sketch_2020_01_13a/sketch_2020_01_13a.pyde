from random import choice, shuffle

NODE_SIZE = 5
nodes, edges = [], set()
# NGBS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
ONGBS = [(0, 1), (1, 0), (-1, -1), (0, -1)]


def setup():
    size(500, 500)
    global grid, f
    f = createFont("Free Sans Bold", 100)
    strokeWeight(1)
    # fontList = PFont.list()
    # for f in fontList:
    #     print(f)

    imagem = draw_text('PCD', 250, 225, text_size=225)
    grid = make_grid(imagem, width, height, 25, margin=10)

def draw():
    background(170, 170, 200)

    for a, b in edges:
        noFill()
        x0, y0, c1 = grid[a]
        x1, y1, c2 = grid[b]
        if c1 != 0 and c2 != 0:
            stroke(255)
        else:
            # stroke(0)
            stroke(lerpColor(c1, c2, 0.5))
        line(x0, y0, x1, y1)
        
    for n in nodes:
        x, y, c = grid[n]
        noStroke()
        if c != 0:
            c = 255
        fill(c)
        circle(x, y, NODE_SIZE)

    add_connected(ONGBS)


def keyPressed():
    if key == ' ':
        nodes[:] = []
        edges.clear()
    if key == 'n':
        add_random_node()
    if key == 's':
        saveFrame("s####.png")


def add_connected(nbs):
    if nodes:
        i, j = nodes[-1]
        shuffle(nbs)
        for ni, nj in nbs:
            other = i + ni, j + nj
            if grid.get(other, None) and other not in nodes:
                nodes.append(other)
                edges.add(((i, j), other))
                break
        else:
            if len(nodes) < len(grid):
                # add_random_node()
                # shuffle(nodes)
                nodes[:] = [nodes[-1]] + nodes[:-1]
                # println("ops!")

def add_random_node():
    if len(nodes) < len(grid):
        k = choice(grid.keys())
        while k in nodes:
            k = choice(grid.keys())
        nodes.append(k)

def draw_text(txt, x, y, text_size=120):
    img = createGraphics(width, height)
    img.beginDraw()
    img.textFont(f)
    img.textAlign(CENTER, CENTER)
    img.textSize(text_size)
    # img.textFont(f)
    img.text(txt, x, y)
    img.endDraw()
    return img


def make_grid(p_graphics, w, h, s, margin=None):
    off = s / 2
    margin = off if margin is None else margin
    cols, rows = (w - margin * 2) // s, (h - margin * 2) // s
    points = dict()
    for i in range(cols):
        x = off + i * s + margin
        for j in range(rows):
            y = off + j * s + margin
            bc = p_graphics.get(x, y)
            points[(i, j)] = (x, y, bc)

    return points
