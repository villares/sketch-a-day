from cell import Cell

def setup():
    global cols, rows, board
    size(800, 800)
    # noSmooth()
    cols = width / int(Cell.W * 1.533)
    rows = height / int(Cell.H * 2)
    init_board()

def draw():
    # scale(0.95)
    # translate(-Cell.W / 2, -Cell.H / 2)
    background(0)
    for cell in Cell.board.values():
        cell.display()

def keyPressed():
    if key == ' ':
        init_board()
    elif key == 'r':
        init_board(rnd=True)
    elif key == 'n':
        next_board()
    
def mouseDragged():
    toggle()

def mousePressed():
    toggle()
    
def mouseReleased():
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
