from graph import Graph

graph = Graph({"g": ["d", "f"],
               "i": ["c"],
               "c": ["i", "c", "d", "e"],
               "d": ["f", "c"],
               "e": ["c"],
               "f": ["d", "h"],
               "a": ["b"],
               "h": ["f"],
               "b": ["a"]
               })


def setup():
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

    saveFrame("sketch_2020_07_14c.png")

def setup_graph(g):
    global cols, rows, grid
    n = len(g)
    ang = TWO_PI / n
    grid = {}
    v_list = g.vertices()
    for i in range(n):
        v = v_list[i]
        x = cos(ang * i) * width * .4 + width / 2
        y = sin(ang * i) * height * .4 + height / 2
        grid[v] = (x, y)
