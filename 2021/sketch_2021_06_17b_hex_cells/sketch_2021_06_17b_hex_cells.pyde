from cell import Cell

def setup():
    global cols, rows, board
    size(825, 805)
    noSmooth()
    cols = width / int(Cell.W * 1.5)
    rows = height / int(Cell.H * 2)
    init_board()

def draw():
    # scale(0.95)
    background(0)
    for cell in Cell.board.values():
        cell.display()

def keyPressed():
    if key == ' ':
        init_board()
    elif key == 'r':
        init_board(rnd=True)
    
def mouseDragged():
    toggle()

def mousePressed():
    toggle()
    
def mouseReleased():
    Cell.last_clicked = None
    
def toggle():
    for cell in Cell.board.values():
        cell.check_click()
    
def init_board(rnd=False):
    for i in range(cols):
        for j in range(rows):
            Cell(i, j, rnd)
