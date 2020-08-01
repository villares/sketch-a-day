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
    background(200)
    for v in grid.keys():
        xa, ya = grid[v]
        for e in graph[v]:
            xb, yb = grid[e]
            line(xa, ya, xb, yb)
    
    for v in grid.keys():
        x, y = grid[v]
        text(v, x, y)

#    saveFrame("sketch_2020_07_14b.png")

def setup_graph(g):
    global cols, rows, grid
    cols, rows = dimensionar_grade(len(g))
    w, h = width / cols, height / rows
    grid = {}
    v_list = g.vertices() 
    for c in range(cols):
        for r in range(rows):
            if v_list:
                v = v_list.pop()
                grid[v] = (w /2 + c * w + random(-10, 10),
                           h /2 + r * h + random(-10, 10))
                

def dimensionar_grade(n):
    a = int(sqrt(n))
    b = n / a
    if a * b < n:
        b += 1
    print(u'{}: {} × {} ({})'.format(n, a, b, a * b))
    return a, b
