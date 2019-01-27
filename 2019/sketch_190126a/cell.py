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

        if self.state:
            strokeWeight(1)
            self.draw_mode()
            if mode == -1:
                fill(100, 100, 100, 10)
                noStroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
                noFill()

    def draw_mode(self):
        """ draws node """
        siz = self.size_
        with pushMatrix():
            translate(self.pos.x, self.pos.y, self.pos.z)
            if Cell.debug_mode:
                fill(255, 0, 100)
                text(self.module, 0, 0)
            noFill()  # stroke(0)
            i, j, k = self.index
            for (ni, nj, nk) in Cell.ONL:
                nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
                if nb and nb.state:
                    stroke(200)
                    bar(0, 0, 0,
                         ni * siz, nj * siz, nk * siz)
                    # stroke(64, 200, 200)
                    # with pushMatrix():
                    #     translate(ni * siz / 3, nj * siz / 3, nk * siz / 3)
                    #     box(siz / 3)
            for (ni, nj, nk) in Cell.DNL:
                nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
                if nb and nb.state:
                    stroke(64 + (ni * 2 + nj * 3 + nk * 5) * 16, 255, 200)
                    bar(0, 0, 0,
                         ni * siz, nj * siz, nk * siz,
                         ni * 2 + nj * 3 + nk * 5)
