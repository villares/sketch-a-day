from __future__ import print_function, division
import pickle

from graph import Graph
from grid import Grid  
from arcs import var_bar

thread_running = False
gx, gy = 0, 100
viz_stat = False
selected_v = None

def setup():
    size(1000, 1000)
    colorMode(HSB)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 12)
    textFont(f)
    setup_graph()

def setup_graph(mode=0):
    # create a random graph and a dict of grid postions for its vertices
    global graph, grid, m
    graph = Graph.random_graph(range(100),
                               connect_rate=.95,
                               allow_loops=False,
                               connected=True,
                               allow_cyclic=False)
    grid = Grid(graph,
                width=width,
                height=width,
                margin=10,
                mode=mode)
    m = grid.edge_distances()  # "metric", sum of edge distances
    print("Cyclic: " + str(graph.is_cyclic()))

def draw():
    # scale(.5)
    background(0)
    for e in reversed(grid.edges()):
        xa, ya, xb, yb, za, zb, deg = e
        strokeWeight(map(deg, 1.5, 5, 4, 1))
        fill(255, 200)
        var_bar(xa, ya, xb, yb, za, zb)

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
            fill(255, 0, 0)
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
    global gx, gy, viz_stat, grid, graph
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
    elif key == 'p':
        saveFrame("####.png")    
    elif key == 'd':
        with open("data/grid.data", "w") as f:
            pickle.dump((graph, grid), f)
            print("dump grid.data")
    elif key == 'l':
        with open("data/grid.data", "rb") as f2:
            graph, grid = pickle.load(f2)
            print("load grid.data")
    else:
        if not thread_running:
            thread("swapping")
        else:
            print("\nalready swapping")

def swapping():
    global grid, thread_running, gx, gy, m
    if str(key) not in 's23456789':
        print("wrong key!")
        return
    thread_running = True
    print("starting thread.", end="")
    m = grid.edge_distances()
    len_graph = len(graph)
    multiple = 1 if mousePressed else 100
    for _ in range(multiple):
        if key == 's':
            grid.swap(num=len_graph)
        if key in '234556789':
            grid.swap(num=int(key))
        n = grid.edge_distances()
        gx += 1
        if n < m:
            gy -= gy * (m - n) / m
            m = n
    thread_running = False
    print("\nending thread.")

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
                grid.recalculate_d()
    selected_v = None


# TODO IDEAS:
# Find distance outliers and try to shuffle them closer
# Run many times without visualisation on Python 3 to get some huge samples
