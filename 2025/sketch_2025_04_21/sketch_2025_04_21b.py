import py5
import numpy as np

grid = {}
quads = []
margin = 50
N = 16

def setup():
    py5.size(700, 700)
    calc_grid()

def draw():
    py5.random_seed(1)
    py5.background(230, 240, 250)
    py5.stroke_weight(1)
    for q in quads:
        py5.fill(0, 128, py5.random(255))
        with py5.begin_closed_shape(py5.QUADS): 
            py5.vertices(grid[vi] for vi in q) 
    py5.stroke_weight(5)
    py5.points(tuple(grid.values()))

def calc_grid():
    cell_size = (py5.width - margin * 2) / N
    quads.clear()
    for i in range(N):
        x = margin + i * cell_size + cell_size / 2 
        for j in range(N):
            y = margin + j * cell_size + cell_size / 2
            grid[(i, j)] = np.array([x, y])
            if i > 0 and j > 0:
                quads.append((
                    (i-1, j-1), (i, j-1),
                    (i, j), (i-1, j)
                ))

def mouse_dragged():
    mouse_vector = np.array([py5.mouse_x, py5.mouse_y])
    grid_positions = np.array(list(grid.values()))
    d = grid_positions - mouse_vector
    d_mag = np.linalg.norm(d, axis=1, keepdims=True)
    d_mag[d_mag == 0] = 1  # avoid division by zero
    d_scaled = d * (1 / d_mag)
    for i, vi in enumerate(grid.keys()):
        grid[vi] += d_scaled[i]

def key_pressed():
    calc_grid()
     
py5.run_sketch(block=False)
