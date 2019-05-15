# -*- coding: utf-8 -*-
from random import choice
from bar import bar

class Cell():
    border = 0
    # RES = 4.
    grid = dict()
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
        self.calculate_pos()

    def calculate_pos(self):
        i, j, k = self.index
        self.pos = PVector(
            Cell.border + self.size_ / 2 + i * self.size_,  # - width / 2,
            Cell.border + self.size_ / 2 + j * self.size_,  # - height / 2,
            k * self.size_ - height / 5)

    def plot(self, mode):
        """ draws node """
        siz = self.size_
        if self.state:
            pushMatrix()
            translate(self.pos.x,
                      self.pos.y,
                      self.pos.z)
            noFill()  # stroke(0)

            i, j, k = self.index
            # stroke(0)
            if mode == 0:
                for (ni, nj, nk) in Cell.ONL:
                    nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
                    if nb and nb.state:
                        bar(0, 0, 0,
                            ni * siz / 2, nj * siz / 2, nk * siz / 2,
                            5)
            if mode == 1:
                for (ni, nj, nk) in Cell.DNL:
                    nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
                    if nb and nb.state:
                        bar(0, 0, 0,
                            ni * siz / 2, nj * siz / 2, nk * siz / 2,
                            3)
            popMatrix()
