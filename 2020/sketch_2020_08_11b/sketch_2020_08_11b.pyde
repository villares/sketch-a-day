from __future__ import print_function, division
from random import choice
from graph import Graph
from grid import *  # setup_grid, grid_swap, edge_distances

thread_count = 0
gx, gy = 0, 100

def setup():
    size(400, 500)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 12)
    textFont(f)
    setup_graph()

def setup_graph():
    # create a random graph and a dict of grid postions for its vertices
    global graph, grid, m, d, display_text
    graph = Graph.random_graph(range(49), allow_loops=False, connected=True)
    grid = setup_grid(graph, width=width, height=width, margin=10)
    # display setup
    display_text = [""]
    m = edge_distances(graph, grid)  # "metric", sum of edge distances
    d = createGraphics(width, 100)  # canvas for data display
    d.beginDraw()
    d.background(150)
    d.endDraw()
    print(graph)
    # setup walker
    global sel_v, path_walker, t_walker
    sel_v = graph.get_random_vertex()
    path_walker = []
    t_walker = 0

def draw():
    background(200)
    noFill()
    for e in graph.edges():
        va = e.pop()
        xa, ya, za = grid[va]
        if len(e) == 1:
            vb = e.pop()
            xb, yb, zb = grid[vb]
            stroke(200)
            strokeWeight(6)
            line(xa, ya, xb, yb)
            stroke(0)
            strokeWeight(4)
            line(xa, ya, xb, yb)
        else:
            circle(20 + xa, ya, 24)

    for v in grid.keys():
        x, y, z = grid[v]
        fill(0)        
        circle(x, y, 10)
        if keyPressed:
            fill(255)
            text("{}".format(v).upper(), x - 15, y - 3)
            
    for v in grid.keys():
        x, y, z = grid[v]
        fill(0, 255, 0)
        if dist(mouseX, mouseY, x, y) < 30:
            ns = near_sample(graph, grid, 9, v)
            for n in ns:
                x, y, z = grid[n]  
                circle(x, y, 10)        

    walker()
    image(d, 0, height - 100)
    fill(0)
    textAlign(LEFT)
    text(format(gy / 100, ".2%"), width - 100, height - 80)
    text(format(m, ".0f"), width - 100, height - 60)
    fill(255)
    text('\n'.join(display_text[-2:]), 20, height - 40)

def display():
    d.beginDraw()
    d.stroke(0)
    d.strokeWeight(1)
    d.line(gx, 100, gx, 100 - gy)
    d.noStroke()
    d.endDraw()

def walker():
    global t_walker, path_walker, sel_v
    if path_walker and t_walker < 1:
        path_vectors = [PVector(*grid[pv]) for pv in path_walker]
        p = lerpVectors(t_walker, path_vectors)
        noFill()
        stroke(0, 0, 255)
        circle(p.x, p.y, 10)
        t_walker += .03 / len(path_walker)
    else:
        path_walker = []
        noStroke()
        fill(255, 0, 0)
        x, y, _ = grid[sel_v]
        circle(x, y, 10)

def lerpVectors(amt, vecs):
    """ from Jeremy Douglass """
    amt = constrain(amt, 0, 1)  # let's play safe
    if len(vecs) == 1:
        return vecs[0]
    cunit = 1.0 / (len(vecs) - 1)
    return PVector.lerp(vecs[floor(amt / cunit)],
                        vecs[ceil(amt / cunit)],
                        amt % cunit / cunit)

def keyTyped():
    global gx, gy
    if key == 'r':
        setup_graph()
        background(200)
        gx, gy = 0, 100
    else:
        thread("swapping")

def swapping():
    global grid, thread_count, gx, gy, m, t
    if str(key) not in 'sc23456789':
        return
    thread_count += 1
    this_thread, this_key = thread_count, str(key)
    m = edge_distances(graph, grid)
    t = "Starting thread:{} key:{}".format(this_thread, key)
    display_text.append(t)
    print("\n" + t, end="")
    len_graph = len(graph)
    for _ in range(len_graph):
        if this_key == 's':
            grid = grid_swap(graph, grid, display_text, num=len_graph)
        if this_key in '234556789':
            grid = grid_swap(graph, grid, display_text, num=int(this_key))
        if this_key == 'c':
            grid = grid_conv(graph, grid, display_text, num=9)
        n = edge_distances(graph, grid)
        gx += 1
        if n < m:
            gy -= gy * (m - n) / m
            m = n
        display()
        if key == 'k':
            break
    t = "Ending thread: {}".format(this_thread)
    display_text.append(t)
    print("\n" + t, end="")


def mousePressed():
    global path_walker, t_walker, sel_v
    for v in graph.vertices():
        x, y, _ = grid[v]
        if v != sel_v and dist(x, y, mouseX, mouseY) < 10:
            path = graph.find_shortest_path(sel_v, v)
            if path:
                path_walker = path
                t_walker = 0
                sel_v = v
                
# TODO IDEAS: 
# Show what "nearby" sample means
# Find distance outliers and try to shuffle them closer
# Run many times without visualisation on Python 3 to get some huge samples
