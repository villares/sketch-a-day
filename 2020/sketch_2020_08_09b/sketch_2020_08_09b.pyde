from __future__ import print_function, division
from random import choice
from graph import Graph
from grid import setup_grid, grid_swap, edge_distances

thread_count = 0
gx, gy = 0, 100000

def setup():
    size(400, 500)
    fill(0)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 14)
    textFont(f)
    setup_graph()
    
def setup_graph():    
    global graph, grid
    graph = Graph.random_graph(range(36), allow_loops=False)
    grid = setup_grid(graph, width=width, height=width, margin=10)
    global sel_v
    sel_v = graph.get_random_vertex()
    global path_walker, t_walker
    path_walker = []
    t_walker = 0
    print(graph)

def draw():
    noStroke()
    fill(150)
    rect(0, 0, width, width)
    noFill()
    for e in graph.edges():
        va = e.pop()
        xa, ya, za = grid[va]
        if len(e) == 1:
            vb = e.pop()
            xb, yb, zb = grid[vb]
            stroke(150)
            strokeWeight(6)
            line(xa, ya, xb, yb)
            stroke(255)
            strokeWeight(3)
            line(xa, ya, xb, yb)
        else:
            circle(20 + xa, ya, 30)
 
    for v in grid.keys():
        x, y, z = grid[v]
        fill(255)
        circle(x, y, 10)
        if keyPressed:
            fill(0)
            text("{}".format(v).upper(), x - 15, y - 3)

    walker()   
    # graph_edge_distances()
    stroke(0)
    strokeWeight(1)
    line(gx, height, gx, height - gy / 1000)

def walker():        
    global t_walker, path_walker, sel_v
    if path_walker and t_walker < 1:
        # print(t_walker, path_walker)
        p = lerpVectors(t_walker, path_walker)
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
        gx, gy = 0, 100000
    else:
        thread("swapping")
        
def swapping():
    global grid, thread_count, gx, gy
    thread_count += 1
    this_thread, this_key = thread_count, str(key)
    m = edge_distances(graph, grid)
    print("\nStarting thread:{} key:{}".format(this_thread, key), end="")
    len_graph = len(graph)
    for _ in range(len_graph):
        if this_key == 's':
            grid = grid_swap(graph, grid, num = len_graph)
        if this_key in '234556789':
            grid = grid_swap(graph, grid, num=int(this_key))
        n = edge_distances(graph, grid)
        gx += 1
        if n < m:
            gy -= gy * (m - n) / m
            m = n
    print("\nEnding thread :{}".format(this_thread), end="")
                            
                                                
def mousePressed():
    global path_walker, t_walker, sel_v
    for v in graph.vertices():
        x, y, _ = grid[v]
        if v != sel_v and dist(x, y, mouseX, mouseY) < 10:
            path = graph.find_shortest_path(sel_v, v)
            if path:
                path_walker = [PVector(*grid[pv]) for pv in path]
                t_walker = 0
                sel_v = v 
