import numpy as np
import py5

color_map = np.array([
    [0, 0, 0],       # void
    [0, 0, 200],     # blue water
    [200, 200, 0],   # yellow sand
    [200, 0, 0],     # red rock
    [128, 128, 128], # gray concrete
    ])

VOID, WATER, SAND, ROCK, CONCRETE = range(5)
current_material = SAND 

def setup():
    global grid
    py5.size(500, 500)
    grid = np.zeros((py5.width, py5.height), dtype='int8')

def draw():
    py5.set_np_pixels(color_map[grid], 'RGB')
    update_grid()
    py5.window_title(f'{py5.get_frame_rate():.1f}')

def update_grid():
    # flow water 0
    shake_water()
    # vertical fall
#     rows, next_rows = grid[:-1], grid[1:]
#     next_rows_empty = next_rows == VOID
#     for material in (SAND, WATER):
#         positions = rows == material
#         falling_positions = positions & next_rows_empty
#         rows[falling_positions] = VOID
#         next_rows[falling_positions] = material
    # generalized vertical fall - heavier sinks Rock > Sand > Water > Air-Void
    rows, next_rows = grid[:-1], grid[1:]
    smaller_down = (next_rows < rows) & (rows != CONCRETE)  # Concrete is heavier still
    rows[smaller_down], next_rows[smaller_down] = next_rows[smaller_down], rows[smaller_down] 
    # diagonal fall left
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]
        next_left_empty = next_row[:-1] == VOID
        for material in (SAND, WATER):
            material_right = row[1:] == material
            falling_left = material_right & next_left_empty
            row[1:][falling_left] = VOID        
            next_row[:-1][falling_left] = material
    # diagonal fall right
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]
        next_right_empty = next_row[1:] == VOID
        for material in (SAND, WATER):
            material_left = row[:-1] == material
            falling_right = material_left & next_right_empty
            row[:-1][falling_right] = VOID        
            next_row[1:][falling_right] = material
    # flow water again
    shake_water()

def shake_water():
    cols, next_cols = grid.T[:-1], grid.T[1:]  # grid.T => Transposed grid
    if py5.random(100) < 50: 
        next_cols_empty = next_cols == VOID
        water_positions = cols == WATER
        moving_positions = water_positions & next_cols_empty
        cols[moving_positions] = VOID
        next_cols[moving_positions] = WATER
    else:    
        next_cols_water = next_cols == WATER
        empty_positions = cols == VOID
        moving_positions = empty_positions & next_cols_water
        cols[moving_positions] = WATER
        next_cols[moving_positions] = VOID

def key_pressed():
    global current_material
    if py5.key == ' ':
        grid[:] = np.zeros((py5.width, py5.height), dtype='int8')
    elif py5.key == 'v':
        current_material = VOID
    elif py5.key == 'c':
        current_material = CONCRETE
    elif py5.key == 's':
        current_material = SAND
    elif py5.key == 'w':
        current_material = WATER
    elif py5.key == 'r':
        current_material = ROCK        
        
def mouse_dragged():
    x = py5.mouse_x % py5.width
    y = py5.mouse_y % py5.height
    if py5.is_key_pressed:
        grid[y][x] = current_material
    else:
        grid[y-4:y+5,x-4:x+5] = current_material

py5.run_sketch()
