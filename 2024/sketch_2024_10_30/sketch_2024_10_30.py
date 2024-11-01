
from itertools import product

import py5
import numpy as np

step_scale = 0.003

def setup():
    global screen_grid, noise_space_grid, len_grid
    py5.size(500, 500, py5.P3D)
    py5.color_mode(py5.HSB)
    py5.stroke_weight(5)
    grid = list(product(range(0, py5.height, 5), range(0, py5.width, 5)))
    len_grid = len(grid)
    screen_grid = np.array((grid))

def draw():
    global screen_grid, remapped_values, positions_and_values
    py5.window_title(f'{py5.get_frame_rate():.1f}')
    py5.translate(py5.width/2, py5.height/2, -py5.height/2)
    py5.rotate_x(py5.radians(45))
    py5.translate(-py5.width/2, -py5.height/2)
    py5.background(0)
    offset = np.array((-py5.mouse_x * 10, -py5.mouse_y * 10))
    t = py5.frame_count * 10 
    noise_space_grid = (screen_grid + offset) * step_scale
    noise_values = py5.os_noise(
        noise_space_grid[:,0],
        noise_space_grid[:,1],
        np.full(len_grid, t * step_scale)
    )
    remapped_values = (noise_values + 1) / 2 * 255  # could have been remap()
#    positions_and_values = np.hstack((screen_grid, remapped_values.reshape(-1, 1)))
#     for x, y, n in positions_and_values:
#         py5.stroke(n, 255, 255)
#         py5.point(x, y, n)
    colored_points(screen_grid[:,0], screen_grid[:,1], remapped_values)

@np.vectorize
def colored_points(x, y, n):
    py5.stroke(n, 255, 255)
    py5.point(x, y, n)
# at some point I should try a Py5Shape with py5.begin_shape(py5.POINTS)
# & vertices() & set_strokes() but I'm tired
      
py5.run_sketch(block=False)     
