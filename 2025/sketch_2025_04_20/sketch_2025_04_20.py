import py5

grid = {}
quads = []
margin = 50
N = 16

def setup():
    py5.size(700, 700)
    calc_grid()

def draw():
    global mouse_vector
    mouse_vector = py5.Py5Vector(py5.mouse_x, py5.mouse_y)
    py5.random_seed(1)
    py5.background(230, 240, 250)
    py5.stroke_weight(1)
    for q in quads:
        py5.fill(0, 128, py5.random(255))
        with py5.begin_closed_shape(py5.QUADS): 
            py5.vertices(grid[i, j]for i, j in q) 
    py5.stroke_weight(5)
    py5.points(tuple(grid.values()))

#     py5.no_fill()
#     with py5.begin_closed_shape(py5.QUADS): 
#         py5.vertices(grid[i, j]
#                  for q in quads
#                  for i, j in q) 

def calc_grid():
    cell_size = (py5.width - margin * 2) / N
    quads.clear()
    for i in range(N):
        x = margin + i * cell_size + cell_size / 2 
        for j in range(N):
            y = margin + j * cell_size + cell_size / 2
            grid[i, j] = py5.Py5Vector(x, y)
            if i > 0 and j > 0:
                quads.append((
                    (i-1, j-1), (i, j-1),
                    (i, j), (i-1, j)
                    ))

def mouse_dragged():
    for (i, j), v in grid.items():
        d = v - mouse_vector
        d.mag = 1 / (d.mag + 1)
        grid[i, j] += d
    
def key_pressed():
    calc_grid()
     
py5.run_sketch(block=False)