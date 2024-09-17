import py5

UNIT_SQR = 15
MAX_UNITS = 6

grid = {}

def setup():
    global w
    py5.size(840, 600)
    py5.color_mode(py5.HSB)
    py5.stroke_weight(3)
    py5.stroke(240)
     
def draw():
    global order
    order = 0
    py5.background(200)
    cols = py5.width // UNIT_SQR
    rows = py5.height // UNIT_SQR
    for j in range(rows):
        for i in range(cols):
            n_limit = min(MAX_UNITS, min(rows - j, cols - i))
            n = py5.random_int(1, n_limit)
            #for t in (n, 1):
            for t in range(n, 0, -1): # from n to 1
                if check_grid_space(i, j, t):
                    fill_grid(i, j, t)
                    
    for (i, j), (n, order) in grid.items():
        if n:
            draw_square(i, j, n, order)
    py5.save_frame('###.png')
    py5.no_loop()
                
def fill_grid(i, j, n):
    global order
    for di in range(n):
        for dj in range(n):
            grid[i + di, j + dj] = 0, 0
    grid[i, j] = n, order 
    order += 1


def draw_square(i, j, n, square_number):
    square_size = n * UNIT_SQR
    py5.fill(n * 32 - 16, 100, 240)
    py5.square(i * UNIT_SQR, j * UNIT_SQR, square_size)
    py5.fill(0)
    py5.text_size(6)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text(str(square_number),
             i * UNIT_SQR + square_size / 2,
             j * UNIT_SQR + square_size / 2)
      
def check_grid_space(i, j, n):
    for di in range(n):
        for dj in range(n):
            if grid.get((i + di, j + dj)) is not None:
                return False
    return True

def key_pressed():
    grid.clear()
    py5.redraw()

py5.run_sketch()