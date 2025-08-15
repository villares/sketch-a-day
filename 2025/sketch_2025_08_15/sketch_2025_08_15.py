# based on sketch_2022_05_12hex_cells

import py5
from cell import Cell, mock_cell

mock_cell.state = 1 # makes the left border grow
play = former_play_state = False
sample_rate = 1

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
    if play and py5.frame_count % sample_rate == 0:
        Cell.next_board()


def key_pressed():
    global play
    if py5.key == 'e':
        Cell.init_board(cols, rows)
    elif py5.key == 'r':
        Cell.init_board(cols, rows, rnd=True)
    elif py5.key == ' ':
        play = not play
    elif py5.key == 's':
        py5.save_frame('####.png')


def mouse_dragged():
    Cell.toggle(py5.mouse_x, py5.mouse_y)


def mouse_pressed():
    global play, former_play_state
    former_play_state = play
    play = False
    Cell.toggle(py5.mouse_x, py5.mouse_y)


def mouse_released():
    global play
    play = former_play_state
    Cell.last_clicked = None

py5.run_sketch(block=False)

