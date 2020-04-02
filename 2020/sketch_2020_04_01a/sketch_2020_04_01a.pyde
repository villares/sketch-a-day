cell_size = 5
sample = 10
play = False   # simulation is running
last_cell = 0
INFECTION_RATE = 1


def setup():
    global grid, next_grid, rows, cols
    size(500, 500)
    noStroke()
    rows = height / cell_size
    cols = width / cell_size
    grid = empty_grid()
    next_grid = empty_grid()
    # randomize_grid()
    grid[40][25] = 1

    println("Press 'space' to start/stop")
    println("'e' to clear all cells")
    println("'r' to randomize grid")
    println("'+' and '-' to change speed")

def draw():
    background(0)
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y = j * cell_size
            current_state = grid[i][j]
            fill(255)
            if current_state:
                ellipse(x, y, cell_size, cell_size)
            if play and frameCount % sample == 0 and not mousePressed:
                ngbs_alive = calc_ngbs_alive(i, j)
                result = rule(current_state, ngbs_alive)
                next_grid[i][j] = result

    if play and frameCount % sample == 0 and not mousePressed:
        step()

def rule(current, ngbs):

    infection = 0
    for _ in range(ngbs):
        if random(100) < INFECTION_RATE:
            infection = 1
    return current or infection


def calc_ngbs_alive(i, j):
    NEIGHBOURS = ((-1, 00), (01, 00),  # a tuple describing the neighbourhood of a cell
                  (-1, -1), (00, -1),
                  (01, -1), (-1, 01),
                  (00, 01), (01, 01))
                  # (00, 01), (00, -1))

    alive = 0
    for iv, jv in NEIGHBOURS:
        alive += grid[(i + iv) % cols][(j + jv) % rows]
    return alive

def empty_grid():
    grid = []
    for _ in range(cols):
        grid.append([0] * rows)
    return grid

def randomize_grid():
    from random import choice
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = choice((0, 1))

def step():
    global grid, next_grid
    grid = next_grid
    next_grid = empty_grid()

def keyReleased():
    global grid, play, sample
    if key == "e":
        grid = empty_grid()
    if key == "r":
        randomize_grid()
    if key == " ":
        play = not play
    if str(key) in '+=':
        sample = max(sample - 1, 1)
    if key == '-':
        sample += 1

def mousePressed():
    paint()

def mouseDragged():
    paint()

def paint():
    global last_cell
    i, j = mouseX // cell_size, mouseY // cell_size
    p = j * cols + i
    if p != last_cell:
        last_cell = p
        grid[i][j] = (1, 0)[grid[i][j]]
