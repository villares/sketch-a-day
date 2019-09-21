from random import choice

cell_size = 10
clr = 255
NEIGHBOURS = ((-2,  0), ( 2,  0),
              (-1, -1), ( 0, -2),
              ( 1, -1), (-1,  1),
              ( 0,  2), ( 1,  1)) 

def rule(s, v):
    if v < 2 or v > 3:
        return 0
    elif v == 3:
        return 1
    else:
        return s

play = False

def setup():
    global grid, next_grid, rows, cols
    size(800, 500)
    colorMode(HSB)
    rows = height / cell_size
    cols = width / cell_size
    grid = empty_grid()
    next_grid = empty_grid()
    noStroke()
    println("Press 'space' to start/stop")
    println("'e' to clear all cells")
    println("'r' to randomize grid")

def draw():
    background(0) # clear canvas
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y  = j * cell_size
            current_state = grid[i][j]        
            ngbs_alive = calc_ngbs_alive(i, j)
            result = rule(current_state, ngbs_alive)
            next_grid[i][j] = result  
            if current_state:
                fill((clr + next_grid[i][j]*128) % 255, 255, 255)
                square(x, y, cell_size)    
    if play:
        step()

def calc_ngbs_alive(i, j):
    alive = 0
    for iv, jv  in NEIGHBOURS:
        alive += grid[(i + iv) % cols][(j + jv) % rows]
    return alive

def empty_grid():
    grid = []
    for _ in range(cols):
        grid.append([0] * rows)
    return grid

def randomize_grid():
    global clr
    clr = random(255)
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = choice((0, 1))

def step():
    global grid, next_grid
    grid = next_grid
    next_grid = empty_grid()

def keyPressed():
    global grid
    if key == "e":
        grid = empty_grid()
    if key == "r":
        randomize_grid()
    if key == " ":
        global play
        play = not play
    if key == "s":
        saveFrame("#####.png")        
                
def mouseReleased():
    invert_on_mouse()

def mouseDragged():    
    invert_on_mouse()
    
def invert_on_mouse():    
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y  = j * cell_size
            current_state = grid[i][j]
            if mouse_over(x, y):
                grid[i][j] = (1, 0)[current_state]
                
def mouse_over(x, y):
    return x < mouseX < x + cell_size and y < mouseY < y + cell_size
