from __future__ import print_function, division
import pickle

from graph import Graph
from grid import Grid, dim_grid
from arcs import var_bar

thread_running = False
gx, gy = 0, 100
viz_stat = False
selected_v = None

def setup():
    size(600, 600)
    # colorMode(HSB)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 12)
    textFont(f)
    global graph, margin, w, h, cols, rows
    graph = Graph.random_graph(range(100),
                               connect_rate=.95,
                               allow_loops=False,
                               connected=True,
                               allow_cyclic=False)
    margin = width / 40
    cols, rows = dim_grid(len(graph))
    w, h = (width - margin * 2) / cols, (height - margin * 2) / rows
    setup_grid(cols, rows)

def setup_grid(cols, rows, mode=0):
    # create a random graph and a dict of grid postions for its vertices
    global grid, m
    grid = Grid(graph, cols, rows, mode=mode)
    m = grid.edge_distances()  # "metric", sum of edge distances
    print("Cyclic: " + str(graph.is_cyclic()))

def draw():
    # scale(.5)
    background(8, 0, 64)
    t = map(mouseX, 0, width, 0, 1)
    for e in reversed(grid.edges(t)):
        xa, ya, xb, yb, za, zb, deg = e
        strokeWeight(map(deg, 1.5, 5, 4, 1))
        fill(255, 200)
        var_bar(margin + w / 2 + xa * w,
                margin + h / 2 + ya * w,
                margin + w / 2 + xb * w,
                margin + h / 2 + yb * w,
                za * w / 10, zb * w / 10)
        strokeWeight(1)
        circle(margin + w / 2 + xa * w,
               margin + h / 2 + ya * h, 10)
        circle(margin + w / 2 + xb * w,
               margin + h / 2 + yb * h, 10)
        
    for v in grid.keys():
        x, y, z = grid[v]
        # if v == selected_v:
        #     fill(0)
        # elif mouse_near(v):
        #     fill(128)
        # else:
        #     noFill()
        # strokeWeight(1)
        # circle(margin + w / 2 + x * w,
        #        margin + h / 2 + y * h, 10)
        if viz_stat:
            fill(255, 0, 0)
            text("{}:{}".format(v, graph.vertex_degree(v)).upper(),
                 margin + w / 2 + x * w - 15, 
                 margin + h / 2 + y * h - 5)
    fill(100)
    text(int(m), 30, 20)

    if selected_v:
        x, y, _ = grid[selected_v]
        stroke(0)
        strokeWeight(5)
        line(margin + w / 2 + x * w,
             margin + h / 2 + y * h, mouseX, mouseY)


def keyTyped():
    global gx, gy, viz_stat, grid, graph
    if key == 'x':
        grid.grid, grid.other_grid = grid.other_grid, grid.grid
    elif key == 'r':
        setup_grid(cols, rows, mode=0)
        gx, gy = 0, 100
    elif key == 'e':
        setup_grid(cols, rows, mode=1)
        gx, gy = 0, 100
    elif key == 'R':
        setup_grid(cols, rows, mode=2)
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
        if str(key) in '234556789':
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
    return dist(margin + w / 2 + x * w,
                margin + h / 2 + y * h, mouseX, mouseY) < 12

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
