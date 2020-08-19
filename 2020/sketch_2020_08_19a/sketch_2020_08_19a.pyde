from __future__ import print_function, division
from random import choice
from graph import Graph
from grid import *  # setup_grid, grid_swap, edge_distances
from arcs import var_bar
# import cPickle as pickle
import pickle

thread_running = False
gx, gy = 0, 100
viz_stat = False
selected_v = None
margin = 10
num_nodes = 100

def setup():
    size(700, 700)
    colorMode(HSB)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 12)
    textFont(f)    
    global cols, rows, w, h
    cols, rows = dim_grid(num_nodes)
    w, h = (width - margin * 2) / cols, (height - margin * 2) / rows
    Grid.w, Grid.h = w, h
    setup_graph()

def setup_graph(mode=0):
    # create a random graph and a dict of grid postions for its vertices
    global graph, grid, m, d
    graph = Graph.random_graph(range(num_nodes),
                               connect_rate=.95,
                               allow_loops=False,
                               connected=True,
                               allow_cyclic=False)
    grid = Grid(graph,
                cols,
                rows,
                mode=mode)
    global w, h
    d = recalculate_sizes_from_v_deg(graph, grid)
    m = edge_distances(graph, grid)  # "metric", sum of edge distances
    print("Cyclic: " + str(graph.is_cyclic()))
    
def draw():
    background(0)
    for e in graph.edges():
        va = e.pop()
        xa, ya, za = grid[va]
        if len(e) == 1:
            vb = e.pop()
            xb, yb, zb = grid[vb]
            fill(255, 200)
            degree = ((za + zb) / 2) / d
            strokeWeight(map(degree, 1.5, 5, 1, 5))
            x1 = margin + w * 0.5 + xa * w  # - 14 * (r % 2) + 7
            y1 = margin + h * 0.5 + ya * h  # - 14 * (c % 2) + 7
            x2 = margin + w * 0.5 + xb * w  # - 14 * (r % 2) + 7
            y2 = margin + h * 0.5 + yb * h  # - 14 * (c % 2) + 7
            var_bar(x1, y1, x2, y2, za, zb)

    for v in grid.keys():
        x, y, z = grid[v]
        if v == selected_v:
            fill(0)
        elif mouse_near(v):
            fill(128)
        else:
            noFill()
        strokeWeight(1)
        circle(x, y, 10)
        if viz_stat:
            fill(255)
            text("{}:{}".format(v, graph.vertex_degree(v)).upper(),
                 x - 15, y - 5)
    fill(100)
    text(int(m / 200), 20, 20)

    if selected_v:
        x, y, _ = grid[selected_v]
        stroke(0)
        strokeWeight(5)
        line(x, y, mouseX, mouseY)


def keyTyped():
    global gx, gy, viz_stat, grid
    if key == 'r':
        setup_graph(mode=0)
        gx, gy = 0, 100
    elif key == 'e':
        setup_graph(mode=1)
        gx, gy = 0, 100
    elif key == 'R':
        setup_graph(mode=2)
        gx, gy = 0, 100
    elif key == 'v':
        viz_stat = not viz_stat
    elif key == 'p':
        saveFrame("####.png")    
    elif key == 'd':
        with open("data/grid.data", "w") as f:
            pickle.dump(grid, f)
            print("dump grid.data")
    elif key == 'l':
        import encodings
        with open("data/grid.data", "rb") as f2:
            grid = pickle.load(f2)
            print("load grid.data")
 
            # except Exception as e:
            #     print("Erro ({0}): {1}".format(e, e))
               
    

    else:
        if not thread_running:
            thread("swapping")

def swapping():
    global grid, thread_running, gx, gy, m
    if str(key) not in 'sc23456789':
        return
    thread_running = True
    m = edge_distances(graph, grid)
    len_graph = len(graph)
    multiple = 1 if mousePressed else 100
    for _ in range(multiple):
        if key == 's':
            grid.swap(num=len_graph)
        if key in '234556789':
            grid.swap(num=int(key))
        n = edge_distances(graph, grid)
        gx += 1
        if n < m:
            gy -= gy * (m - n) / m
            m = n
    thread_running = False

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
    global selected_v, u
    if selected_v:
        for v in grid.keys():
            if mouse_near(v):
                grid[selected_v], grid[v] = grid[v], grid[selected_v]
                u = recalculate_sizes_from_v_deg(graph, grid)
    selected_v = None


# TODO IDEAS:
# Find distance outliers and try to shuffle them closer
# Run many times without visualisation on Python 3 to get some huge samples
