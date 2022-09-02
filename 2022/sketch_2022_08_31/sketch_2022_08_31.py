import py5
from cell import Cell

play = former_play_state = False
sample_rate = 1
Cell.seed = rs = 2
txt ='Python &\nProcessing\nwith py5'

def setup():
    global cols, rows, board, f
    py5.size(1600, 800)
    py5.color_mode(py5.HSB)
    cols = int(py5.width / Cell.W / 1.5)
    rows = int(py5.height / Cell.H * 2) // 4
    init_board()
    f = py5.create_font('Tomorrow', 240)
    py5.text_font(f)


def draw():
    py5.background(200)
    for cell in Cell.board.values():
        cell.display()
#     for cell in Cell.board.values():
#         cell.display_root()
        
    if play and py5.frame_count % sample_rate == 0:
        for ij in sorted(Cell.board.keys()):
            Cell.board[ij].calc_next_state()
#     py5.text_align(py5.CENTER, py5.CENTER)
#     py5.text_size(240)
#     py5.text_leading(200)
#     py5.text(txt, py5.width / 2, py5.height * 0.4)    


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
        save_png_with_src(files='cell.py')
    elif py5.key == 't':
        init_board(text=txt)


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

def xy_to_ij(x, y):
    i = (x - Cell.W) // (Cell.W * 1.5)
    if i % 2 == 0:
        j = (y - Cell.H) // (Cell.H * 2)
    else:
        j = (y - Cell.H * 2) // (Cell.H * 2)
    return i, j

def toggle():
    mx, my = py5.mouse_x, py5.mouse_y
    i, j = xy_to_ij(mx, my)
    try:
       cell = Cell.board[(i, j)]
       cell.check_click()
    except KeyError:
        pass


def init_board(rnd=False, text=''):
    py5.random_seed(rs)
    for i in range(cols):
        for j in range(rows):
            Cell(i, j, rnd)
    if text:
        print(text)
        buffer = py5.create_graphics(py5.width, py5.height)
        buffer.begin_draw()
        buffer.text_font(f)
        buffer.text_align(py5.CENTER, py5.CENTER)
        buffer.text_size(240)
        buffer.text_leading(210)
        buffer.text(text, py5.width / 2 - 5, py5.height * 0.45)
        for x in range(py5.width):
            for y in range(py5.height):
                i, j = xy_to_ij(x, y)
                if buffer.get(x, y) == py5.color(255):
                    try:
                       cell = Cell.board[(i, j)]
                       cell.check_click()
                    except KeyError:
                        pass  
        buffer.end_draw()

py5.run_sketch()
