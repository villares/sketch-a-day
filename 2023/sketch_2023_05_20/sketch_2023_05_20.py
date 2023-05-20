import numpy as np
import py5

def setup():
    global grid
    py5.size(500, 500)
    grid = np.zeros((py5.width, py5.height), dtype=bool)

def draw():
    py5.set_np_pixels(grid * 128, 'L')
    update_grid()

def update_grid():
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]
        sand = row == 1
        next_row_empty = next_row == 0
        falling = sand & next_row_empty
        row[falling] = 0
        next_row[falling] = 1
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]        
        sand_right = row[1:] == 1
        next_left_empty = next_row[:-1] == 0
        falling_left = sand_right & next_left_empty
        row[1:][falling_left] = 0        
        next_row[:-1][falling_left] = 1
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]                
        sand_left = row[:-1] == 1
        next_right_empty = next_row[1:] == 0
        falling_right = sand_left & next_right_empty
        row[:-1][falling_right] = 0        
        next_row[1:][falling_right] = 1

def key_pressed():
    if py5.key == ' ':
        grid[:] = np.zeros((py5.width, py5.height), dtype=bool)

def mouse_dragged():
    x = py5.mouse_x % py5.width
    y = py5.mouse_y % py5.height
    if py5.is_key_pressed:
        grid[y-4:y+5,x-4:x+5] = 1
    else:
        grid[y][x] = 1

py5.run_sketch()
