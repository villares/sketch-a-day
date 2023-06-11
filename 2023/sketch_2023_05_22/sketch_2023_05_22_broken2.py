import numpy as np
import py5

color_map = np.array([
    [0, 0, 0],       # void
    [200, 200, 0],   # yellow sand
    [200, 0, 0],     # red concrete
    [0, 0, 200],     # blue water
    ])

VOID, SAND, CONCRETE, WATER = range(4)
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
    # flow sideways
#     w = grid.shape[1]
#     if py5.random(100) > 50:
#         for j in reversed(range(w)):
#           if py5.random(100) > 50:
#                 col = grid.T[j]
#                 water = col == WATER
#                 next_col = grid.T[(j + 1) % w]
#                 next_empty = next_col == VOID
#                 moving_right = water & next_empty
#                 col[moving_right] = VOID
#                 next_col[moving_right] = WATER
#     else:
#         for j in range(w):
#            if py5.random(100) > 50:
#                 col = grid.T[j]
#                 water = col == WATER
#                 previous_col = grid.T[(j - 1) % w]
#                 previous_empty = previous_col == VOID
#                 moving_left = water & previous_empty
#                 col[moving_left] = VOID
#                 previous_col[moving_left] = WATER
    # vertical fall
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]
        next_row_empty = next_row == VOID
        for material in (SAND, WATER):
            positions = row == material
            falling_positions = positions & next_row_empty
            row[falling_positions] = VOID
            next_row[falling_positions] = material
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
        
        
def mouse_dragged():
    x = py5.mouse_x % py5.width
    y = py5.mouse_y % py5.height
    if py5.is_key_pressed:
        grid[y][x] = current_material
    else:
        grid[y-4:y+5,x-4:x+5] = current_material


py5.run_sketch()
