import py5

UNIT_SQR = 30
MAX_UNITS = 4

grid = {}


def setup():
    global w
    py5.size(600, 600)
    py5.color_mode(py5.HSB)
    py5.stroke(100)
     
def draw():
    py5.background(200)
    cols = py5.width // UNIT_SQR
    rows = py5.height // UNIT_SQR
    for j in range(cols):
        for i in range(rows):
            n_limit = min(MAX_UNITS, min(cols - j, rows - i))
            n = py5.random_int(1, n_limit)
            # print(s)
            if check_grid_space(i, j, n):
                fill_grid(i, j, n)
            elif check_grid_space(i, j, 1):
                fill_grid(i, j, 1)
    py5.save('out.png')
    #py5.no_loop()
                
def fill_grid(i, j, n):
    square_size = n * UNIT_SQR
    py5.fill(n * 32 - 16, 100, 240)
    py5.square(i * UNIT_SQR, j * UNIT_SQR, square_size)
#     py5.fill(0)
#     py5.text_align(py5.CENTER, py5.CENTER)
#     py5.text(str(n),
#              i * UNIT_SQR + square_size / 2,
#              j * UNIT_SQR + square_size / 2)
    for di in range(n):
        for dj in range(n):
            grid[i + di, j + dj] = True
    py5.no_loop()
        
def check_grid_space(i, j, n):
    for di in range(n):
        for dj in range(n):
            if grid.get((i + di, j + dj)):
                return False
    return True

def key_pressed():
    grid.clear()
    py5.loop()
    py5.redraw()

py5.run_sketch()