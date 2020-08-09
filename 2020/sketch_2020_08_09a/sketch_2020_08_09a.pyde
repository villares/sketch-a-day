from random import choice
from graph import Graph
from grid import setup_grid, grid_swap, grid_shuffle, grid_swap_mult

thread_count = 0

def setup():
    size(400, 400)
    fill(0)
    textAlign(CENTER, CENTER)
    f = createFont("Source Code Pro Bold", 14)
    textFont(f)
    setup_graph()
    
def setup_graph():    
    global graph, grid
    graph = Graph.random_graph(range(36), allow_loops=False)
    grid = setup_grid(graph, margin=10)
    global sel_v
    sel_v = graph.get_random_vertex()
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
        text("{}".format(v).upper(), x - 15, y - 3)

    walker()   

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
    if key == 'r':
        setup_graph()
    else:
        thread("swapping")
        
def swapping():
    global grid, thread_count
    thread_count += 1
    print("Starting thread {}.".format(thread_count))
    if key == 's':
        for _ in range(len(graph)):
            grid = grid_swap(graph, grid)
    if key == 'S':
        for _ in range(len(graph)):
            grid = grid_shuffle(graph, grid)
    if key == '3':
        for _ in range(len(graph)):
            grid = grid_swap_mult(graph, grid, num=3)
    if key == '4':
        for _ in range(len(graph)):
            grid = grid_swap_mult(graph, grid, num=4)
    print("Ending thread {}.".format(thread_count))
                            
                                                
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
