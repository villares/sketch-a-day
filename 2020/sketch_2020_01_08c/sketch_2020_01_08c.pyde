from random import choice, shuffle

graph = []

ngbs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
# ngbs = ((-1, 0), (0, -1), (0, 1), (1, 0))

def setup():
    size(500, 500)
    global grid
    grid = make_grid(width, height, 50)
    
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
    background(240, 240, 230)
    for i, j  in grid.keys():
        x, y = grid[(i, j)]
        noStroke()
        fill(255)
        circle(x, y, 5) 
    for i, j in graph:
        x, y = grid[(i, j)]
        fill(0)
        circle(x, y, 5)    
    if len(graph) > 1:
        noFill()
        stroke(0)
        beginShape()
        for i, j in graph:
            x, y = grid[(i, j)]
            vertex(x, y)
        endShape()
        add_connected()
        

def keyPressed():
    if key == ' ':
        graph[:] = []
    if key == 'n':
        add_random_node()
    if key == 's':
        saveFrame("s####.png")
    if key == 'm':
        add_connected()  
          
def add_connected():
    if graph:
        i, j = graph[-1]
        shuffle(ngbs)
        for ni, nj in ngbs:
            other = i + ni, j + nj
            if grid.get(other, None) and other not in graph:
                graph.append(other)
                break
        else:
            if len(graph) < len(grid):
                graph[:] = [graph[-1]] + graph[:-1]
                println("ops!")
                
        
def add_random_node():
    if len(graph) < len(grid):
        k = choice(grid.keys())
        while k in graph:
            k = choice(grid.keys())
        graph.append(k)        
