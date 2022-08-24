from math import sqrt
from py5 import *
from random import sample, seed


SIN_60 = sqrt(3) * 0.5  # sin(radians(60))

class mock_cell:
    state = 0
    gen = 0

class Cell():

    board = dict()
    EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
    ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
    W = 16
    H = SIN_60 * W
    last_clicked = None

    def __init__(self, i, j, rnd=False):
        self.board[(i, j)] = self
        self.i = i
        self.j = j
        self.x = i * self.W * 1.5 + self.W
        if i % 2 == 0:
            self.y = j * self.H * 2 + self.H
        else:
            self.y = j * self.H * 2 + self.H * 2
        self.state = 0
        if rnd:
            if random(1000) < 10: self.state = self            
        self.gen = 0
        self.nbs = 0

    def display(self):
        if self.state:
            stroke(100 + (self.gen * 16) % 100, 200 - self.gen, 200) #42 * self.nbs)
            stroke_weight(2)
            line(self.x, self.y, self.state.x, self.state.y)

    def get_neighbour(self, i_offset, j_offset):
        return self.board.get((self.i + i_offset,
                               self.j + j_offset),
                               mock_cell())

    def get_empty_nbs(self):
        #seed(len(self.board) // 100)
        nbs = self.EVN_NBS if self.i % 2 == 0 else self.ODD_NBS
        #nbs = sample(nbs, 4)
        return [self.get_neighbour(i_offset, j_offset)
                for i_offset, j_offset in nbs
                if self.get_neighbour(i_offset, j_offset).state == 0]

    def calc_next_state(self):
        if self.state:
            en = self.get_empty_nbs()
            for n in en:
                if random(10) < len(en):
                    n.state = self
                    n.gen = self.gen + len(en) / 6

    def check_click(self):
        if self.__class__.last_clicked != self:
            if not self.state: self.state = self 
            self.__class__.last_clicked = self


    @staticmethod
    def hexagon(w):
        h = SIN_60 * w
        with begin_shape():
            vertex(-w, 0)
            vertex(-w / 2, -h)
            vertex(w / 2, -h)
            vertex(w, 0)
            vertex(w - w / 2, h)
            vertex(-w / 2, h)
            vertex(-w, 0)
