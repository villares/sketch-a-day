# based on Randomized Prim's algorithm https://en.wikipedia.org/wiki/Maze_generation_algorithm

from random import randint

def setup():
    size(400, 400)
    rectMode(CENTER)
    noLoop()
    noStroke()
    
def draw():
    m = maze(100,100)
    w, h = 4, 4
    for x in range(len(m)):
        for y in range(len(m[0])):
            if m[x][y]==1: fill(0)
            else: fill(255,0,0)
            rect(w/2 + w * x, h/2 + h * y, w, h)

def maze(mh, mw, complexity=.01, density=10):
    # Only odd shapes
    shape = ((mh // 2) * 2 + 1, (mw // 2) * 2 + 1)
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (shape[0] + shape[1]))) # number of components
    density    = int(density * ((shape[0] // 2) * (shape[1] // 2))) # size of components
    # Build actual maze
    Z = [[0] * shape[1] for _ in range(shape[0])]
    # Make aisles
    for i in range(density):
        x = randint(0, shape[1] // 2) * 2
        y = randint(0, shape[0] // 2) * 2 # pick a random position
        Z[y][x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[randint(0, len(neighbours) - 1)]
                if Z[y_][x_] == 0:
                    Z[y_][x_] = 1
                    Z[y_ + (y - y_) // 2][ x_ + (x - x_) // 2] = 1
                    x, y = x_, y_
    return Z
