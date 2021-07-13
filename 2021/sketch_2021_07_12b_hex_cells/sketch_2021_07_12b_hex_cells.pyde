from cell import Cell

play = former_play_state = False
sample_rate = 2

def setup():
    global cols, rows, board
    size(600, 600)
    # noSmooth()
    cols = width / int(Cell.W * 1.5)
    rows = height / int(Cell.H * 2) - 1
    init_board()
    stroke(255)


def draw():
    # scale(0.95)
    # translate(-Cell.W / 2, -Cell.H / 2)
    background(0)
    for cell in Cell.board.values():
        cell.display()
    if play and frameCount % sample_rate == 0:
        next_board()

def keyPressed():
    global play
    if key == 'e':
        init_board()
    elif key == 'r':
        init_board(rnd=True)
    elif key == ' ':
        play = not play
    
def mouseDragged():
    toggle()

def mousePressed():
    global play, former_play_state
    former_play_state = play
    play = False
    toggle()
    
def mouseReleased():
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
        cell.check_click()
    
def init_board(rnd=False):
    for i in range(cols):
        for j in range(rows):
            Cell(i, j, rnd)
