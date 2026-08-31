from itertools import product

import py5

N = 10
oi = oj = 0

def setup():
    global grid_pos, cell_size
    py5.size(600, 600)
    py5.text_align(py5.CENTER, py5.CENTER)
    py5.text_size(20)
    cell_size = py5.width / N
    py5.rect_mode(py5.CENTER)
    grid_pos = list(product(range(N), repeat=2))
    
def draw():
    py5.background(200)
    py5.no_fill()
    for i, j in grid_pos:
        x = i * cell_size + cell_size / 2
        y = j * cell_size + cell_size / 2
        py5.square(x, y, cell_size)
        py5.text(f'{i + oi},{j + oj}', x, y)



def key_pressed():
    global oi, oj
    if py5.key == 's':
        py5.save_frame('###.png')
    elif py5.key == py5.CODED:
        if py5.key_code == py5.LEFT:
            oi -= 1
        if py5.key_code == py5.RIGHT:
            oi += 1
        if py5.key_code == py5.UP:
            oj -= 1
        if py5.key_code == py5.DOWN:
            oj += 1

py5.run_sketch(block=False)
