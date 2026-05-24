# This is a py5 "imported mode" sketch
# learn about py5 modes at https://py5coding.org

"""
Based on ideas from 2018 (s337 2018-12-01 and other experiments) 
"""
from random import choice

CELL_SIZE = 40

def setup():
    size(600, 600)
    rect_mode(CENTER)
    init_grid(width // CELL_SIZE, height // CELL_SIZE)

def init_grid(w, h):
    for i in range(w):
        for j in range(h):
            Cell((i,j), CELL_SIZE, choice((True, False)))
            
def draw():
    background(150)
    for c in Cell.grid.values():
        c.play()

def key_pressed():
    if key == 's':
        save_frame('###.png')                                    
    elif key == ' ':
        Cell.mode = (Cell.mode + 1) % 3
       
class Cell():
    # neighbours list
    DN = ((-1, -1),       (+1, -1),
           
          (-1, +1),       (+1, +1))
    ON = (          (+0, -1),
          (-1, +0),         (+1, +0),
                    (+0, +1))
    ALLN = ON + DN
    grid = dict()
    mode = 0  # 0, 1, 2

    def __init__(self, index, CELL_SIZE, state=False):
        self.grid[index] = self 
        self.index = index
        self.state = state
        self.cell_size = CELL_SIZE
        self.mouse_down = False
        i, j = index
        self.pos = Py5Vector(
            self.cell_size / 2 + i * self.cell_size,
            self.cell_size / 2 + j * self.cell_size)

    def play(self):
        hs = self.cell_size / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < mouse_x < px + hs and
                         py - hs < mouse_y < py + hs)
        if self.mouse_on and is_mouse_pressed:
            self.mouse_down = True
        if self.mouse_down and not is_mouse_pressed:
            self.state = not self.state
            self.mouse_down = False
        self.plot()

    def plot(self):
        no_stroke()
        if self.state:
            fill(255, 32)
        else:
            fill(0, 32)
        square(*self.pos, self.cell_size)
        stroke_weight(self.cell_size / 6)
        i, j = self.index
        third = self.cell_size / 3
        nbs = (self.ALLN, self.ON, self.DN)[self.mode]
        for (ni, nj) in nbs:
            nb = self.grid.get((i + ni, j + nj), None)

            if self.state and nb and nb.state:
                if (ni, nj) in self.DN:
                    stroke(255)
                else:
                    stroke(0)
                line(
                    self.pos.x + ni * third,
                    self.pos.y + nj * third,
                    self.pos.x, self.pos.y)
            elif not self.state and nb and not nb.state:
                if (ni, nj) in self.DN:
                    stroke(200)
                else:
                    stroke(100)
                line(
                    self.pos.x + ni * third,
                    self.pos.y + nj * third,
                    self.pos.x, self.pos.y)                             
        stroke(200, 0, 0)
        point(*self.pos)

        if self.mouse_on:
            with push_style():
                fill(128, 128)
                stroke_weight(2)
                stroke(255)
                square(self.pos.x, self.pos.y,
                     self.cell_size)