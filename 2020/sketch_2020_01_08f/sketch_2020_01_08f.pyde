from random import choice, shuffle

NODE_SIZE = 15

nodes, edges = [], set()

# NGBS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
NGBS = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
ONGBS = [(-1, 0), (0, 1)] #, (0, -1), (1, 0)]


def setup():
    size(500, 500)
    global grid
    grid = make_grid(width, height, 40, margin=10)
    strokeWeight(5)
    
def make_grid(w, h, s, margin=None):
    off = s / 2
    margin = off if margin is None else margin
    cols, rows = (w - margin * 2) // s, (h - margin * 2) // s
    points = dict()
    for i in range(cols):
        x = off + i * s + margin
        for j in range(rows):
            y = off + j * s + margin
            points[(i, j)] = (x, y)
    return points
    
def draw():
    background(170, 170, 200)
    for i, j  in grid.keys():
        x, y = grid[(i, j)]
        noStroke()
        fill(255)
        circle(x, y, NODE_SIZE * 2) 
    for i, j in nodes:
        x, y = grid[(i, j)]
        fill(0)
        circle(x, y, NODE_SIZE)    
    for a, b in edges:
        noFill()
        stroke(0)
        x0, y0 = grid[a]
        x1, y1 = grid[b]
        line(x0, y0, x1, y1)
    
    add_connected(ONGBS)
        

def keyPressed():
    if key == ' ':
        nodes[:] = []
        edges.clear()
    if key == 'n':
        add_random_node()
    if key == 's':
        saveFrame("s####.png")
    if key == 'm':
        add_connected(NGBS)  
          
def add_connected(nbs):
    if nodes:
        i, j = nodes[-1]
        shuffle(nbs)
        for ni, nj in nbs:
            other = i + ni, j + nj
            if grid.get(other, None) and other not in nodes:
                nodes.append(other)
                edges.add(((i, j), other))
                break
        else:
            if len(nodes) < len(grid):
                nodes[:] = [nodes[-1]] + nodes[:-1]
                add_connected(NGBS)  
                println("ops!")
                
        
def add_random_node():
    if len(nodes) < len(grid):
        k = choice(grid.keys())
        while k in nodes:
            k = choice(grid.keys())
        nodes.append(k)        
