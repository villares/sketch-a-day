from graph import Graph
from random import sample

graph = Graph()


def setup():
    
    for v in "abcdefghijklmnopq":
        graph.add_vertex(v)
    for _ in range(20):
        s = sample(graph, 2)
        graph.add_edge(s)
        
    
    size(500, 500)
    noLoop()
    setup_graph(graph)
    fill(0)
    textSize(18)
    textAlign(CENTER, CENTER)
    stroke(255)
    strokeWeight(3)

def draw():
    for v in grid.keys():
        xa, ya = grid[v]
        for e in graph[v]:
            xb, yb = grid[e]
            line(xa, ya, xb, yb)

    for v in grid.keys():
        x, y = grid[v]
        text(v, x, y)

    saveFrame("sketch_2020_07_16a.png")

def setup_graph(g):
    global cols, rows, grid
    n = len(g)

    grid = {}
    v_list = g.vertices()
    v_list.sort(key=g.vertex_degree)
    b = n // 2
    a = n - b
    
    ang = TWO_PI / a
    for i in range(a):
        v = v_list[i]
        x = cos(ang * i) * width * .4 + width / 2
        y = sin(ang * i) * height * .4 + height / 2
        grid[v] = (x, y)

    ang = TWO_PI / b
    for i in range(a, a + b):
        v = v_list[i]
        x = cos(ang * i) * width * .2 + width / 2
        y = sin(ang * i) * height * .2 + height / 2
        grid[v] = (x, y)



def dimensionar_grade(n):
    a = int(sqrt(n))
    b = n / a
    if a * b < n:
        b += 1
    print(u'{}: {} × {} ({})'.format(n, a, b, a * b))
    return a, b

def keyPressed():
    global n
    redraw()
    if str(key) in '+=':
        n += 1
    if key == '-' and n > 2:
        n -= 1
