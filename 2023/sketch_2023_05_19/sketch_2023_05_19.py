import numpy as np
import py5

def setup():
    global grid
    py5.size(500, 500)
    grid = np.zeros((py5.width, py5.height), dtype=bool)

def draw():
    py5.set_np_pixels(grid * 255, 'L')
    update_grid()

def update_grid():
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]
        sand = row == 1
        next_row_empty = next_row == 0
        falling = sand & next_row_empty
        row[falling] = 0   
        next_row[falling] = 1

def mouse_dragged():
    x = py5.mouse_x % py5.width
    y = py5.mouse_y % py5.height
    if py5.is_key_pressed:
        grid[y-2:y+3,
             x-2:x+3] = 1
    else:
        #grid[y, x] = 1
        grid[y][x] = 1

py5.run_sketch()
