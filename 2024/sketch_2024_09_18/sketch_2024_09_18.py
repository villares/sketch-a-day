from collections import defaultdict

import py5

UNIT_SQR = 10
MAX_UNITS = 10

counts = defaultdict(lambda:0)
grid = {}

def setup():
    global w
    py5.size(640, 640, py5.P3D)
    py5.color_mode(py5.HSB)
    py5.stroke(0)
     
def draw():
    py5.background(0)
    py5.translate(py5.width / 2, py5.height / 2, -py5.height * 0.60)
    py5.rotate_x(py5.PI / 4)
    py5.rotate_z(py5.PI / 4)
    py5.translate(-py5.width / 2, -py5.height / 2, py5.height / 6)

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
    counts[n] += 1
    for di in range(n):
        for dj in range(n):
            grid[i + di, j + dj] = 0, 0
    grid[i, j] = n, counts[n] 


def draw_square(i, j, n, square_number):
    square_size = n * UNIT_SQR
    py5.fill(n * 32 - 16, 100, 240)
    
    xyz_box(i * UNIT_SQR, j * UNIT_SQR, 0, square_size)

def xyz_box(x, y, z, s):
    with py5.push_matrix():
        py5.translate(x + s / 2, y + s / 2, z + s / 2)
        py5.box(s)
    
def check_grid_space(i, j, n):
    for di in range(n):
        for dj in range(n):
            if grid.get((i + di, j + dj)):
                return False
    return True

def key_pressed():
    grid.clear()
    counts.clear()
    py5.redraw()

py5.run_sketch()