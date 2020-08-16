from __future__ import print_function, division
from random import choice
from graph import Graph
from grid import *  # setup_grid, grid_swap, edge_distances
from arcs import var_bar

thread_count = 0
gx, gy = 0, 100
viz_stat = False
selected_v = None

def setup():
    size(400, 400)
    colorMode(HSB)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 12)
    textFont(f)
    setup_graph()

def setup_graph(mode=0):
    # create a random graph and a dict of grid postions for its vertices
    global graph, grid, m, d, display_text
    graph = Graph.random_graph(range(25), allow_loops=False, connected=True)
    grid = setup_grid(graph, width=width, height=width, margin=10, mode=mode)
    # display setup
    display_text = [""]
    m = edge_distances(graph, grid)  # "metric", sum of edge distances
    print(graph.is_cyclic())

def draw():
    background(240)
    for e in graph.edges():
        va = e.pop()
        xa, ya, za = grid[va]
        if len(e) == 1:
            vb = e.pop()
            xb, yb, zb = grid[vb]
            noStroke()
            fill(((za + zb) / (width / 200)) * 10, 255, 255, 128)
            var_bar(xa, ya, xb, yb, za, zb)

    for v in grid.keys():
        x, y, z = grid[v]
        if v == selected_v:
            fill(255)
        elif mouse_near(v):
            fill(255)
        else:
            fill(64)
        circle(x, y, 10)
        if viz_stat:
            fill(0)
            text("{}".format(v).upper(), x - 15, y - 5)
    fill(100)
    text(int(m / 200), 20, 20)

    if selected_v:
        x, y, _ = grid[selected_v]
        stroke(0, 64)
        strokeWeight(10)
        line(x, y, mouseX, mouseY)



def keyTyped():
    global gx, gy, viz_stat
    if key == 'r':
        setup_graph(mode=0)
        gx, gy = 0, 100
    if key == 'e':
        setup_graph(mode=1)
        gx, gy = 0, 100
    if key == 'R':
        setup_graph(mode=2)
        gx, gy = 0, 100
    elif key == 'v':
        viz_stat = not viz_stat
    else:
        swapping()

def swapping():
    global grid, thread_count, gx, gy, m, t
    if str(key) not in 'sc23456789':
        return
    thread_count += 1
    this_thread, this_key = thread_count, str(key)
    m = edge_distances(graph, grid)
    len_graph = len(graph)
    multiple = 10 if mousePressed else 1
    for _ in range(multiple):
        if this_key == 's':
            grid = grid_swap(graph, grid, display_text, num=len_graph)
        if this_key in '234556789':
            grid = grid_swap(graph, grid, display_text, num=int(this_key))
        n = edge_distances(graph, grid)
        gx += 1
        if n < m:
            gy -= gy * (m - n) / m
            m = n


def mouse_near(v):
    x, y, _ = grid[v]
    return dist(x, y, mouseX, mouseY) < 12

def mousePressed():
    global selected_v
    for v in grid.keys():
        if mouse_near(v):
            selected_v = v
            return

def mouseReleased():
    global selected_v
    if selected_v:
        for v in grid.keys():
            if mouse_near(v):
                grid[selected_v], grid[v] = grid[v], grid[selected_v]
                recalculate_sizes_from_v_deg(graph, grid)
    selected_v = None


# TODO IDEAS:
# Find distance outliers and try to shuffle them closer
# Run many times without visualisation on Python 3 to get some huge samples
