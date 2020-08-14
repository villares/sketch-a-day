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

def setup_graph():
    # create a random graph and a dict of grid postions for its vertices
    global graph, grid, m, d, display_text
    graph = Graph.random_graph(range(25), allow_loops=False, connected=True)
    grid = setup_grid(graph, width=width, height=width, margin=10)
    # display setup
    display_text = [""]
    m = edge_distances(graph, grid)  # "metric", sum of edge distances
    d = createGraphics(width, 100)  # canvas for data display
    d.beginDraw()
    d.background(150)
    d.endDraw()
    print(graph)

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

    if selected_v:
        x, y, _ = grid[selected_v]
        stroke(0, 64)
        strokeWeight(10)
        line(x, y, mouseX, mouseY)

    this.surface.setResizable(False)

    if viz_stat:
        image(d, 0, height - 100)
        fill(0)
        textAlign(LEFT)
        text(format(gy / 100, ".2%"), width - 100, height - 80)
        text(format(m, ".0f"), width - 100, height - 60)
        fill(255)
        text('\n'.join(display_text[-2:]), 20, height - 40)

def offscreen_draw():
    d.beginDraw()
    d.stroke(0)
    d.strokeWeight(1)
    d.line(gx, 100, gx, 100 - gy)
    d.noStroke()
    d.endDraw()

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
    global gx, gy, viz_stat
    if key == 'r':
        setup_graph()
        gx, gy = 0, 100
    elif key == 'v':
        viz_stat = not viz_stat
        this.surface.setResizable(True)
        if viz_stat:
            this.surface.setSize(400, 500)
        else:
            this.surface.setSize(400, 400)
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
        n = edge_distances(graph, grid)
        gx += 1
        if n < m:
            gy -= gy * (m - n) / m
            m = n
        offscreen_draw()
        if key == 'k':
            break
    t = "Ending thread: {}".format(this_thread)
    display_text.append(t)
    print("\n" + t, end="")


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
