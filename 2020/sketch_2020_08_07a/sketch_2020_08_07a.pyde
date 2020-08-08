from random import choice
from graph import Graph

MARGIN = 10

def setup():
    size(400, 400)
    fill(0)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 14)
    textFont(f)
    setup_graph()
    
def setup_graph():    
    global graph, grid
    graph = random_graph()
    grid = setup_grid(graph)
    global sel_v
    sel_v = select_random_vertex(graph)
    global path_walker, t_walker
    path_walker = []
    t_walker = 0
    print(graph)

def draw():
    background(150)
    noFill()
    stroke(255)
    strokeWeight(4)
    for e in graph.edges():
        va = e.pop()
        xa, ya, za = grid[va]
        if len(e) == 1:
            vb = e.pop()
            xb, yb, zb = grid[vb]
            line(xa, ya, xb, yb)
        else:
             circle(20 + xa, ya, 30)

    for v in grid.keys():
        x, y, z = grid[v]
        fill(255)
        circle(x, y, 10)
        fill(0)
        text(v.upper(), x - 15, y - 3)
        
    noStroke()
    fill(255, 0, 0)
    x, y, _ = grid[sel_v]
    circle(x, y, 10)    
    walker()
        
def walker():        
    global t_walker, path_walker, sel_v
    if path_walker:
        p = lerpVectors(t_walker, path_walker)
        noFill()
        stroke(0, 0, 255)
        circle(p.x, p.y, 10)
        if t_walker < 1:
            t_walker += .01
        else:
            path_walker = []
    
def setup_grid(graph):
    cols, rows = dimensionar_grade(len(graph))
    w, h = (width - MARGIN * 2) / cols, (height - MARGIN * 2) / rows
    points = []
    for i in range(cols * rows):
        c = i % cols
        r = i // rows
        x = MARGIN + w * 0.5 + c * w - 20 * (r % 2) + 5 * r
        y = MARGIN + h * 0.5 + r * h - 20 * (c % 2) + 5 * c
        z = 0
        points.append((x, y, z))
    points = sorted(
        points, key=lambda p: dist(p[0], p[1], width / 2, height / 2))
    v_list = reversed(sorted(graph.vertices(), key=graph.vertex_degree))
    # v_list = sorted(graph.vertices(), key=graph.vertex_degree)
    grid = {v: p for v, p in zip(v_list, points)}
    return grid

def random_graph(names="abcdefghijklmnop"):
    graph = Graph()
    for v in names:
        graph.add_vertex(v)
        if random(100) < 90:
            graph.add_edge({v, choice(names)})
    return graph

def select_random_vertex(graph):
    return choice(graph.vertices())

def dimensionar_grade(n):
    a = int(sqrt(n))
    b = n / a
    if a * b < n:
        b += 1
    print(u'{}: {} × {} ({})'.format(n, a, b, a * b))
    return a, b

def keyPressed():
    setup_graph()
    # saveFrame('##_sketch_2020_08_04a.png')
        
def mousePressed():
    global path_walker, t_walker, sel_v
    for v in graph:
        x, y, _ = grid[v]
        if v != sel_v and dist(x, y, mouseX, mouseY) < 10:
            path = graph.find_path(sel_v, v)
            if path:
                path_walker = [PVector(*grid[pv]) for pv in path]
                t_walker = 0
                sel_v = v 

def lerpVectors(amt, vecs):
    """ from Jeremy Douglass """
    if len(vecs) == 1:
        return vecs[0]
    cunit = 1.0 / (len(vecs) - 1)
    return PVector.lerp(vecs[floor(amt / cunit)],
                        vecs[ceil(amt / cunit)],
                        amt % cunit / cunit)
