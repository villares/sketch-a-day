import py5
from cell import Cell

play = former_play_state = False
sample_rate = 1
rs = 1

def setup():
    global cols, rows, board
    py5.size(800, 800)
    py5.color_mode(py5.HSB)
    cols = int(py5.width / Cell.W / 1.5)
    rows = int(py5.height / Cell.H * 2) // 4
    init_board()


def draw():
    py5.background(200)
    for cell in Cell.board.values():
        cell.display()
    if play and py5.frame_count % sample_rate == 0:
        next_board()


def key_pressed():
    global play
    if py5.key == 'e':
        init_board()
    elif py5.key == 'r':
        init_board(rnd=True)
    elif py5.key == ' ':
        play = not play
    elif py5.key == 's':
        from villares.helpers import save_png_with_src
        save_png_with_src()

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


def toggle():
    mx, my = py5.mouse_x, py5.mouse_y
    i = (mx - Cell.W) // (Cell.W * 1.5)
    if i % 2 == 0:
        j = (my - Cell.H) // (Cell.H * 2)
    else:
        j = (my - Cell.H * 2) // (Cell.H * 2)
    try:
       cell = Cell.board[(i, j)]
       cell.check_click()
    except KeyError:
        pass


def init_board(rnd=False):
    py5.random_seed(rs)
    for i in range(cols):
        for j in range(rows):
            Cell(i, j, rnd)


py5.run_sketch()

