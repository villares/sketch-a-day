from graph import Graph

graph = Graph({
    'a': ['b', 'k'],
    'b': ['a'],
    'c': ['i', 'c', 'd', 'e'],
    'd': ['f', 'c'],
    'e': ['c'],
    'f': ['d', 'h', 'j', 'k'],
    'g': ['d', 'f'],
    'h': ['f'],
    'i': ['c'],
    'j': ['f'],
    'k': ['a', 'f'],
})

MARGIN = 50

def setup():
    size(600, 600)
    setup_grid(graph)
    fill(0)
    textSize(18)
    textAlign(CENTER, CENTER)
    stroke(255)
    strokeWeight(3)

def draw():
    background(200)
    for v in grid.keys():
        xa, ya, za = grid[v]
        for e in graph[v]:
            xb, yb, zb = grid[e]
            line(xa - za, ya - za, xb - zb, yb - zb)

    for v in grid.keys():
        x, y, z = grid[v]
        text(v, x - z, y - z)

    saveFrame('sketch_2020_08_01a.png')

def setup_grid(g):
    global cols, rows, grid
    cols, rows = dimensionar_grade(len(g))
    w, h = (width - MARGIN * 2) / cols, (height - MARGIN * 2) / rows
    grid = {}
    v_list = g.vertices()
    c, r = 0, 0
    next = None
    while v_list:
        if next is None:
            next = v_list.pop()
        else:
            v_list.remove(next)
        z = len(graph[next])
        grid[next] = (MARGIN + w / 2 + c * w,
                      MARGIN + h / 2 + r * h,
                      z * w / 10)
        for v in graph[next]:
            if v in v_list:
                next = v
                break
        else:
            if v_list:
                next = None
        c += 1
        if c == cols:
            c = 0
            r += 1


def dimensionar_grade(n):
    a = int(sqrt(n))
    b = n / a
    if a * b < n:
        b += 1
    print(u'{}: {} × {} ({})'.format(n, a, b, a * b))
    return a, b

def keyPressed():
    from random import choice
    global graph
    graph = Graph()
    names = "abcdefghijkl"
    for v in names:
        graph.add_vertex(v)
        if random(100) < 90:
            graph.add_edge((v, choice(names)))

    setup_grid(graph)
