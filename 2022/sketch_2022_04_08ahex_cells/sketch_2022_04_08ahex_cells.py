# based on sketch_2021_07_14ahex_cells

from cell import Cell

play = former_play_state = False
sample_rate = 2

def setup():
    global cols, rows, board
    size(600, 600)
    color_mode(HSB)
    cols = int(width / Cell.W * 1.5)
    rows = int(height / Cell.H * 2) - 1
    init_board()
    stroke(0)


def draw():
    background(0)
    for cell in Cell.board.values():
        cell.display()
    if play and frame_count % sample_rate == 0:
        next_board()


def key_pressed():
    global play
    if key == 'e':
        init_board()
    elif key == 'r':
        init_board(rnd=True)
    elif key == ' ':
        play = not play


def mouse_dragged():
    toggle()


def mouse_pressed():
    global play, former_play_state
    former_play_state = play
    play = False
    toggle()


def mouse_released():
    global play
    play = former_play_state
    Cell.last_clicked = None


def next_board():
    for cell in Cell.board.values():
        cell.calc_next_state()
    for cell in Cell.board.values():
        cell.state = cell.next_state


def toggle():
    for cell in Cell.board.values():
        cell.check_click(mouse_x, mouse_y)


def init_board(rnd=False):
    for i in range(cols):
        for j in range(rows):
            Cell(i, j, rnd)
