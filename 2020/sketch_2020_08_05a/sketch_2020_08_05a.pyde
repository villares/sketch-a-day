from graph import Graph

MARGIN = 10

def setup():
    global graph, grid
    size(400, 400)
    graph = random_graph()
    grid = setup_grid(graph)
    fill(0)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 14)
    textFont(f) 

def draw():
    background(200)
    noFill()
    stroke(255)
    strokeWeight(4)
    for v in grid.keys():
        xa, ya, za = grid[v]
        for e in graph[v]:
            if e != v:
                xb, yb, zb = grid[e]
                line(xa + za, ya + za, xb + zb, yb + zb)
            else:
                circle(20 + xa + za, ya + za, 30)

    for v in grid.keys():
        x, y, z = grid[v]
        fill(200)
        stroke(0)
        strokeWeight(2)
        circle(x + z, y + z, 30)
        fill(0)
        text("{}:{}".format(v.upper(),graph.vertex_degree(v)), x + z, y + z - 3)

    # saveFrame('sketch_2020_08_04a.png')

def setup_grid(graph):
    cols, rows = dimensionar_grade(len(graph))
    w, h = (width - MARGIN * 2) / cols, (height - MARGIN * 2) / rows
    points = []
    for i in range(cols * rows):
        c = i % cols
        r = i // rows
        x = MARGIN + w * 0.1 + c * w
        y = MARGIN + h * 0.1 + r * h
        z = PVector(x, y) - PVector(width / 2, height / 2)
        z = z.mag() / 50  
        points.append((x, y, z * 10))
    # points = sorted(points, key=lambda p:dist(p[0], p[1], width / 2, height / 2))        
    # v_list = reversed(sorted(graph.vertices(), key=graph.vertex_degree)) 
    v_list = sorted(graph.vertices(), key=graph.vertex_degree)
    grid = {v : p for v, p in zip(v_list, points)}
    return grid

def random_graph(names="abcdefghijklmnop"):
    from random import choice
    graph = Graph()
    for v in names:
        graph.add_vertex(v)
        if random(100) < 90:
            graph.add_edge({v, choice(names)})
    return graph

def dimensionar_grade(n):
    a = int(sqrt(n))
    b = n / a
    if a * b < n:
        b += 1
    print(u'{}: {} × {} ({})'.format(n, a, b, a * b))
    return a, b

def keyPressed():
    global graph, grid
    graph = random_graph()
    grid = setup_grid(graph)
    print(graph)
