# based on Randomized Prim's algorithm https://en.wikipedia.org/wiki/Maze_generation_algorithm

from random import randint

def setup():
    global m, dim, Z, C
    size(400, 400)
    rectMode(CENTER)
    colorMode(HSB)
    noLoop()
    noStroke()
    # Only odd dims
    dim = ((101 // 2) * 2 + 1, (101 // 2) * 2 + 1)
    Z = [[0] * dim[1] for _ in range(dim[0])]
    C = [[0] * dim[1] for _ in range(dim[0])]
    m = maze(101,101)
    w, h = 4, 4
    for x in range(len(m)):
        for y in range(len(m[0])):
            if m[x][y]==1: fill(C[x][y])
            else: fill(255)
            rect(w/2 + w * x, h/2 + h * y, w, h)

def maze(mh, mw, complexity=.51, density=2):
    # Adjust complexity and density relative to maze size
    complexity = int(complexity * (5 * (dim[0] + dim[1]))) # number of components
    density    = int(density * ((dim[0] // 2) * (dim[1] // 2))) # size of components
    # Build actual maze

    # Make aisles
    for i in range(density):
        x = randint(0, dim[1] // 2) * 2
        y = randint(0, dim[0] // 2) * 2 # pick a random position
        Z[y][x] = 1
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < dim[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < dim[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                y_,x_ = neighbours[randint(0, len(neighbours) - 1)]
                if Z[y_][x_] == 0:
                    Z[y_][x_] = 1
                    C[y_][x_] = color(i+j % 256, 255, 200)
                    Z[y_ + (y - y_) // 2][ x_ + (x - x_) // 2] = 1
                    C[y_ + (y - y_) // 2][ x_ + (x - x_) // 2] = 0
                    x, y = x_, y_
            redraw()
    return Z
