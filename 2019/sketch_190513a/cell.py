# -*- coding: utf-8 -*-
from random import choice
from bar import bar

class Cell():
    border = 0
    RES = 4.
    grid = dict()
    debug_mode = False
    # ortho neighbours
    ONL = ((+0, -1, +0),
           (-1, +0, +0),  # (+0, +0, +0),
           (+1, +0, +0),
           (+0, +1, +0),
           (+0, +0, -1), (+0, +0, +1),
           )
    # diagonal neighbours
    DNL = ((+1, +1, +0),
           (-1, -1, +0),  # (+0, +0, +0),
           (+1, -1, +0),
           (-1, +1, +0),
           (+0, -1, +1),
           (-1, +0, +1),
           (+1, +0, +1),
           (+0, +1, +1),
           (+0, -1, -1),
           (-1, +0, -1),
           (+1, +0, -1),
           (+0, +1, -1),
           )

    def __init__(self, index, cell_size, state=False):
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        self.variation = "a"
        self.ang = choice((0, 1, 2, 3))
        self.calculate_pos()

    def calculate_pos(self):
        i, j, k = self.index
        self.pos = PVector(Cell.border + self.size_ / 2 + i * self.size_ - width / 2,
                           Cell.border + self.size_ / 2 +
                           j * self.size_ - height / 2,
                           k * self.size_)

    def update(self, mx, my):
        # mouse over & selection treatment
        hs = self.size_ / 2
        px, py = self.pos.x + width / 2, self.pos.y + height / 2
        self.mouse_on = (px - hs < mx < px + hs and
                         py - hs < my < py + hs)
        if self.mouse_on and mousePressed:
            self.mouse_down = True

        elif self.mouse_down:
            self.state = not self.state
            self.mouse_down = False

    def plot(self, mode):
        """ draws node """
        siz = self.size_
        if self.state:

            pushMatrix()
            translate(self.pos.x, self.pos.y, self.pos.z)
            if Cell.debug_mode:
                fill(255, 0, 100)
                text(self.module, 0, 0)
            noFill()  # stroke(0)

            i, j, k = self.index
            for (ni, nj, nk) in Cell.ONL:
                nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
                if nb and nb.state:
                    stroke(128, 0, 0)
                    bar(0, 0, 0,
                         ni * siz / 2, nj * siz / 2, nk * siz / 2)
            stroke(0, 0, 128)
            for (ni, nj, nk) in Cell.DNL:
                nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
                if nb and nb.state:
                    bar(0, 0, 0,
                         ni * siz / 2, nj * siz / 2, nk * siz / 2, 5)
            popMatrix()
