from math import sqrt
from py5 import *
from random import sample, seed, shuffle
from villares.arcs import var_bar

SIN_60 = sqrt(3) * 0.5  # sin(radians(60))

class mock_cell:
    state = 0
    gen = 0

class Cell():

    board = dict()
    EVN_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2, -2), (2, -2))
    ODD_NBS = ((0, 2), (0, -2), (-2, 0), (2, 0), (-2,  2), (2,  2))
    W = 6
    H = SIN_60 * W
    last_clicked = None
    seed = 3
    root_color = 128

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
            if random(1000) < 2: self.state = self            
        self.gen = 0
        self.nbs = 0


    def display_root(self):
        if self.state == self:
            fill(100)
            circle(self.x, self.y, self.W * 1.5)
            
    def display(self):
        no_stroke()
        fill((128 + self.gen * 4) % 256, 200 - self.gen * 4, 128)
        if self.state:
            if self.state is not self:
                var_bar(self.x, self.y,
                        self.state.x, self.state.y,
                       self.W / (self.gen / 10 + 2),
                       self.W / (self.state.gen / 10 + 2))
            else:
                fill(Cell.root_color)
                circle(self.x, self.y, self.W * 1.5)
            #line(self.x, self.y, self.state.x, self.state.y)
#             with push_matrix():
#                 translate(self.x, self.y)
#                 #no_fill()
#                 self.hexagon(self.W / (self.gen / 10 + 1))
            
    def get_neighbour(self, i_offset, j_offset):
        return self.board.get((self.i + i_offset,
                               self.j + j_offset),
                               mock_cell())

    def get_empty_nbs(self):
        nbs = self.EVN_NBS if self.i % 2 == 0 else self.ODD_NBS
        return [self.get_neighbour(i_offset, j_offset)
                for i_offset, j_offset in nbs
                if self.get_neighbour(i_offset, j_offset).state == 0]

    def calc_next_state(self):
        if self.state:
            en = self.get_empty_nbs()[::-1]
            if len(en) > 3: shuffle(en)
            if en: # and random(10) < 5:
                en[0].state = self
                en[0].gen = self.gen + 1
                
#             for n in en:
#                 n.state = self
#                 n.gen = self.gen + len(en) / 6

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
