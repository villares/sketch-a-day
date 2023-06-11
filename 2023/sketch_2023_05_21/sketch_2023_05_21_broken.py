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

def update_grid():
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
    # flow sideways
    empty_positions = grid == VOID
    water_positions = grid == WATER
    shifted_empty_positions_left = np.roll(empty_positions, -1, axis=1)
    shifted_empty_positions_right = np.roll(empty_positions, 1, axis=1)
    water_matched_left = water_positions & shifted_empty_positions_left
    empty_matched_left = np.roll(water_matched_left, -1, axis=1)
    grid[water_matched_left] = VOID
    grid[empty_matched_left] = WATER
    water_matched_right = water_positions & shifted_empty_positions_right
    empty_matched_right = np.roll(water_matched_right, 1, axis=1)
    grid[water_matched_right] = VOID
    grid[empty_matched_right] = WATER

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
