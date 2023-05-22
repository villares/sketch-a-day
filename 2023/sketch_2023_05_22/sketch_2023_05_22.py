"""
Minimal "sand" simulator - using py5 (py5coding.org) and numpy
"""

import numpy as np
import py5

color_map = np.array([
    [0, 0, 0],       # void
    [50, 50, 200],     # blue water
    [200, 200, 100],   # yellow sand
    [150, 50, 50],     # red rock
    [128, 128, 128], # gray concrete
    ])

VOID, WATER, SAND, ROCK, CONCRETE = range(5)
material_names = ['Void', 'Water', 'Sand', 'Rock', 'Concrete']
key_shortcuts = 'vwsrc'
current_material = SAND 

def setup():
    global grid
    py5.size(500, 500)
    grid = np.zeros((py5.width, py5.height), dtype='int8')

def draw():
    py5.set_np_pixels(color_map[grid], 'RGB')
    update_grid()
    py5.text(material_names[current_material], py5.width - 50, 20)
    py5.window_title(f'{py5.get_frame_rate():.1f}')

def update_grid():
    shake_water()
    # generalized vertical fall - heavier sinks Rock > Sand > Water > Air-Void
    rows, next_rows = grid[:-1], grid[1:]
    fall = (next_rows < rows) & (rows != CONCRETE)  # Concrete is heavier still
    rows[fall], next_rows[fall] = next_rows[fall], rows[fall] 
    
    shake_water()
    # diagonal fall left
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row_left = grid[i][1:], grid[i+1][:-1]
        next_left_empty = next_row_left == VOID
        material = (row == WATER) | (row == SAND)
        swap = material & next_left_empty
        row[swap], next_row_left[swap] = next_row_left[swap], row[swap]
    shake_water()
    # diagonal fall right
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row_right = grid[i][:-1], grid[i+1][1:]
        next_right_empty = next_row_right == VOID
        material = (row == WATER) | (row == SAND)
        swap = material & next_right_empty
        row[swap], next_row_right[swap] = next_row_right[swap], row[swap]

def shake_water():
    water = grid == WATER
    if py5.random_int(1):
        right_empty = (np.roll(grid, -1, axis=1) == VOID)
        moving_right = water & right_empty 
        grid[moving_right] = VOID
        grid[np.roll(moving_right, 1, axis=1)] = WATER
    else:
        left_empty = (np.roll(grid, 1, axis=1) == VOID)
        moving_left = water & left_empty 
        grid[moving_left] = VOID
        grid[np.roll(moving_left, -1, axis=1)] = WATER
 
def key_pressed():
    global current_material
    if py5.key == ' ':
        grid[:] = np.zeros((py5.width, py5.height), dtype='int8')
    elif str(py5.key) in key_shortcuts:
        current_material = key_shortcuts.find(py5.key)
    elif py5.key == 'p':
        py5.save_pickle(grid, 'sandbox.pickle')
        print('saved pickle')
    elif py5.key == 'l':
        try:
            grid[:] = py5.load_pickle('sandbox.pickle')
        except FileIOError:
            print('saved pickle not found')
    elif py5.key_code == py5.RIGHT:
        grid[:] = np.roll(grid, 10, axis=1)
        
def mouse_dragged():
    x, y = py5.mouse_x % py5.width, py5.mouse_y % py5.height
    if py5.is_key_pressed:
        grid[y][x] = current_material
    else:
        grid[y-4:y+5,x-4:x+5] = current_material

py5.run_sketch()