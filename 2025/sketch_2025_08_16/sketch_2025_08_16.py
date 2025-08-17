

import py5
from cell import Cell

def setup():
    global cols, rows, board
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
    cols = int(py5.width / Cell.W * 1.5)
    rows = int(py5.height / Cell.H * 2) - 1
    Cell.init_board(cols, rows)


def draw():
    py5.background(0)
    
    for cell in Cell.board.values():
        cell.display()

def key_pressed():
    if py5.key == 'e':
        Cell.init_board(cols, rows)
    elif py5.key == 's':
        py5.save_frame('####.png')


def mouse_dragged():
    Cell.toggle(py5.mouse_x, py5.mouse_y)

def mouse_pressed():
    Cell.toggle(py5.mouse_x, py5.mouse_y)


def mouse_released():
    Cell.last_clicked = None

py5.run_sketch(block=False)

