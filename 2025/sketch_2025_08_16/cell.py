from math import sqrt
from py5 import *
from functools import cache


SIN_60 = sqrt(3) * 0.5  # sin(radians(60))

class Cell():
    board = dict()
    EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
    ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
    W = 30
    H = SIN_60 * W
    last_clicked = None

    def __init__(self, i, j, poly=None):
        
        self.board[(i, j)] = self
        self.i = i
        self.j = j
        self.x = i * self.W * 1.5 + self.W
        if i % 2 == 0:
            self.y = j * self.H * 2 + self.H
        else:
            self.y = j * self.H * 2 + self.H * 2
        self.state = 0
        if poly and poly.contains(self.x, self.y):
            self.state = 1
        self.nbs = 0


    def display(self):
        if self.state:
            self.calc_live_nbs()
            with push_matrix():
                translate(self.x, self.y)
                #stroke(d * 16, 200, 200) #42 * self.nbs)
                stroke(42 * self.nbs, 200, 200)
                stroke_weight(self.H)
                point(0, 0)


    def check_click(self):
        if self.__class__.last_clicked != self:
            self.state ^= 1
            self.__class__.last_clicked = self


    def calc_live_nbs(self):
        nbs = self.EVN_NBS if self.i % 2 == 0 else self.ODD_NBS
        self.nbs = sum(self.get_neighbour(i_offset, j_offset)
                       for i_offset, j_offset in nbs)

    def get_neighbour(self, i_offset, j_offset):
        if c := self.board.get(
            (self.i + i_offset, self.j + j_offset)
            ):
            return c.state
        else:
            return 0

    @classmethod
    def toggle(cls, mx, my):
        i = (mx - cls.W) // (cls.W * 1.5)
        if i % 2 == 0:
            j = (my - cls.H) // (cls.H * 2)
        else:
            j = (my - cls.H * 2) // (cls.H * 2)
        try:
           cell = cls.board[(i, j)]
           cell.check_click()
        except KeyError:
            pass

    @classmethod
    def init_board(cls, cols, rows, poly=None):
        for i in range(cols):
            for j in range(rows):
                cls(i, j, poly)

