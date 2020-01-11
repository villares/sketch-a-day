from random import choice, shuffle

NODE_SIZE = 5

nodes, edges = [], set()

# NGBS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# ONGBS = [(-1, 0), (0, 1), (0, -1), (1, 0), (-1, -1)]

ONGBS = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1)]


def setup():
    size(500, 500)
    global grid
    strokeWeight(2)

    imagem = draw_text('PCD', 200, 100,text_size=100)    

    grid = make_grid(imagem, width, height, 20, margin=10)
    # pontos_fim[:] = set_points(fim, shuffle_points=True)
    

def draw():
    background(170, 170, 200)

    for i, j in nodes:
        x, y = grid[(i, j)]
        fill(0)
        circle(x, y, NODE_SIZE)
    for a, b in edges:
        noFill()
        stroke(0)
        x0, y0 = grid[a]
        x1, y1 = grid[b]
        line(x0, y0, x1, y1)

    add_connected(ONGBS)


def keyPressed():
    if key == ' ':
        nodes[:] = []
        edges.clear()
    if key == 'n':
        add_random_node()
    if key == 's':
        saveFrame("s####.png")
    # if key == 'm':
    #     add_connected(NGBS)

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
                nodes[:] = [nodes[-1]] + nodes[:-1]
                println("ops!")


def add_random_node():
    if len(nodes) < len(grid):
        k = choice(grid.keys())
        while k in nodes:
            k = choice(grid.keys())
        nodes.append(k)
        

def draw_text(txt, x, y, text_size=120): 
    img = createGraphics(width, height)
    img.beginDraw()
    img.textAlign(CENTER, CENTER)
    img.textSize(text_size)
    img.text(txt, x, y)
    img.endDraw()
    return img
                
                                
# def set_points(p_graphics, bg_points=False,  shuffle_points=True):
#     pontos = []
#     step = 4
#     i = 0
#     for y in range(0, width, step):
#         for x in range(0, width, step):
#             bc = p_graphics.get(x, y)
#             if bc != 0:
#                 pontos.append(Ponto(x, y, random(5, 10)))
#             else:
#                 if bg_points:
#                     pontos.append(Ponto(x, y, random(1, 5)))
#     if  shuffle_points:
#         shuffle(pontos)
#     return pontos

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
            if bc != 0:
                points[(i, j)] = (x, y)
    return points
