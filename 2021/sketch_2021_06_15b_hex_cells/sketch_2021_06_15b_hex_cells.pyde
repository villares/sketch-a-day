# Inspired by an example of hex grid from The Nature of Code example repository
# by Daniel Shiffman http://natureofcode.com

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

def mousePressed():
    init_board()
    
def init_board():
    for i in range(cols):
        for j in range(rows):
            Cell(i, j)
