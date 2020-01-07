from random import choice

graph = []

def setup():
    size(500, 500)
    global grid
    grid = make_grid(width, height, 100)
    
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
        circle(x, y, 10) 
    for i, j in graph:
        x, y = grid[(i, j)]
        fill(0)
        circle(x, y, 10)    
    if len(graph) > 1:
        noFill()
        stroke(0)
        beginShape()
        for i, j in graph:
            x, y = grid[(i, j)]
            vertex(x, y)
        endShape()
        
    
def keyPressed():
    if key == ' ':
        graph[:] = []
    if key == 'n':
        if len(graph) < len(grid):
            k = choice(grid.keys())
            while k in graph:
                k = choice(grid.keys())
            graph.append(k)
        else:
            print("completo")        
    if key == 's':
        saveFrame("s####.png")
