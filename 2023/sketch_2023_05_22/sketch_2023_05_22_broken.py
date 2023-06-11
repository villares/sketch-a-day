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
    if py5.random(10) < 5:
        left_empty = grid[:,:-1] == VOID
        water_right = grid[:,1:] == WATER
        moving_left = water_right & left_empty
        grid[:,1:][moving_left] = VOID        
        grid[:,:-1][moving_left] = WATER
    else:
        right_empty = grid[:,1:] == VOID
        water_left = grid[:,:-1] == WATER
        moving_right = water_left & right_empty
        grid[:,:-1][moving_right] = VOID        
        grid[:,1:][moving_right] = WATER

        
    # vertical fall
    rows, next_rows = grid[:-1], grid[1:]
    smaller_down = (next_rows < rows) & (rows != CONCRETE)  # Concrete is heavier still
    rows[smaller_down], next_rows[smaller_down] = next_rows[smaller_down], rows[smaller_down] 
    # diagonal fall left
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]
        next_left_empty = next_row[:-1] == VOID
        for material in (WATER, SAND):
            material_right = row[1:] == material
            falling_left = material_right & next_left_empty
            row[1:][falling_left] = VOID        
            next_row[:-1][falling_left] = material
    # diagonal fall right
    for i in reversed(range(grid.shape[0]-1)):
        row, next_row = grid[i], grid[i+1]
        next_right_empty = next_row[1:] == VOID
        for material in (WATER, SAND):
            material_left = row[:-1] == material
            falling_right = material_left & next_right_empty
            row[:-1][falling_right] = VOID        
            next_row[1:][falling_right] = material
    # flow water again



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
    elif py5.key_code == py5.RIGHT:
        grid[:] = np.roll(grid, 10)
        
def mouse_dragged():
    x = py5.mouse_x % py5.width
    y = py5.mouse_y % py5.height
    if py5.is_key_pressed:
        grid[y][x] = current_material
    else:
        grid[y-4:y+5,x-4:x+5] = current_material


py5.run_sketch()
