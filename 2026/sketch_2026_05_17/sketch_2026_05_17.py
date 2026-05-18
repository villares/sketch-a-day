# This is a py5 "module mode" sketch
# learn about py5 modes at https://py5coding.org

"""
Based on s337 2018-12-01
"""
import py5
from random import choice

CELL_SIZE = 25

def setup():
    py5.size(500, 500)
    py5.rect_mode(py5.CENTER)
    init_grid(py5.width // CELL_SIZE, py5.height // CELL_SIZE)

def init_grid(w, h):
    for i in range(w):
        for j in range(h):
            Cell((i,j), CELL_SIZE, choice((True, False)))
            
def draw():
    py5.background(200)
    for c in Cell.grid.values():
        c.play()

def key_pressed():
    if py5.key == "s":
        py5.save_frame("###.png")                                    
                                                                                                            
       

class Cell():
    # neighbours list
    NL = ((-1, -1), (+0, -1), (+1, -1),
          (-1, +0), (+0, +0), (+1, +0),
          (-1, +1), (+0, +1), (+1, +1))
    ONL = ((+0, -1),
           (-1, +0), (+0, +0), (+1, +0),
           (+0, +1))
    grid = dict()

    def __init__(self, index, CELL_SIZE, state=False):
        self.grid[index] = self 
        self.index = index
        self.state = state
        self.size_ = CELL_SIZE
        self.mouse_down = False
        i, j = index
        self.pos = py5.Py5Vector(
            self.size_ / 2 + i * self.size_,
            self.size_ / 2 + j * self.size_)

    def play(self):
        hs = self.size_ / 2
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
        py5.stroke_weight(1)
        #py5.rect(self.pos.x, self.pos.y, self.size_, self.size_)
        if self.state:
            third = self.size_ / 3
            if py5.key != py5.CODED:
                nbs = self.NL
            else:
                nbs = self.ONL
            i, j = self.index[0], self.index[1]
            py5.stroke_weight(third)
            for (ni, nj) in nbs:
                nb = self.grid.get((i + ni, j + nj), None)
                if nb and nb.state:
                    if (ni, nj) in self.ONL:
                        py5.stroke(0, 0, 100)
                    else:
                        py5.stroke(0, 100, 0)
                    py5.line(
                        self.pos.x + ni * third,
                        self.pos.y + nj * third,
                        self.pos.x, self.pos.y)

        if self.mouse_on:
            with py5.push_style():
                py5.fill(128, 128)
                py5.rect(self.pos.x, self.pos.y,
                     self.size_,
                     self.size_
                )
       
py5.run_sketch(block=False)

    



