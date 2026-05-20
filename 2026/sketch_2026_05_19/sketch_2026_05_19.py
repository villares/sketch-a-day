# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

"""
Based on s337 2018-12-01
"""
import py5
from random import choice

CELL_SIZE = 40

def setup():
    py5.size(800, 800)
    py5.rect_mode(py5.CENTER)
    init_grid(py5.width // CELL_SIZE, py5.height // CELL_SIZE)

def init_grid(w, h):
    for i in range(w):
        for j in range(h):
            Cell((i,j), CELL_SIZE, choice((True, False)))
            
def draw():
    py5.background(250)
    for c in Cell.grid.values():
        c.play()

def key_pressed():
    if py5.key == 's':
        py5.save_frame('###.png')                                    
    elif py5.key == ' ':
        Cell.mode = (Cell.mode + 1) % 3
       
class Cell():
    # neighbours list
    DN = ((-1, -1),        (+1, -1),
           
          (-1, +1),       (+1, +1))
    ON = (          (+0, -1),
          (-1, +0),         (+1, +0),
                    (+0, +1))
    ALLN = DN + ON
    grid = dict()
    mode = 0  # 0, 1, 2

    def __init__(self, index, CELL_SIZE, state=False):
        self.grid[index] = self 
        self.index = index
        self.state = state
        self.cell_size = CELL_SIZE
        self.mouse_down = False
        i, j = index
        self.pos = py5.Py5Vector(
            self.cell_size / 2 + i * self.cell_size,
            self.cell_size / 2 + j * self.cell_size)

    def play(self):
        hs = self.cell_size / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < py5.mouse_x < px + hs and
                         py - hs < py5.mouse_y < py + hs)
        if self.mouse_on and py5.is_mouse_pressed:
            self.mouse_down = True
        if self.mouse_down and not py5.is_mouse_pressed:
            self.state = not self.state
            self.mouse_down = False
        self.plot()

    def plot(self):
        py5.fill(255)
        py5.stroke_weight(self.cell_size / 4)
        i, j = self.index
        third = self.cell_size / 3
        nbs = (self.ALLN, self.ON, self.DN)[self.mode]
        for (ni, nj) in nbs:
            nb = self.grid.get((i + ni, j + nj), None)
            if self.state and nb and nb.state:
                if (ni, nj) in self.DN:
                    py5.stroke(0, 0, 200)
                else:
                    py5.stroke(0, 200, 0)
                py5.line(
                    self.pos.x + ni * third,
                    self.pos.y + nj * third,
                    self.pos.x, self.pos.y)
            elif not self.state and nb and not nb.state:
                if (ni, nj) in self.DN:
                    py5.stroke(200, 200, 0)
                else:
                    py5.stroke(200, 0, 200)
                py5.line(
                    self.pos.x + ni * third,
                    self.pos.y + nj * third,
                    self.pos.x, self.pos.y)                             
#                 py5.stroke(0)
#                 py5.point(*self.pos)
             
        if self.mouse_on:
            with py5.push_style():
                py5.fill(128, 128)
                py5.stroke_weight(2)
                py5.stroke(255)
                py5.square(self.pos.x, self.pos.y,
                     self.cell_size
                )
       
py5.run_sketch(block=False)

    



