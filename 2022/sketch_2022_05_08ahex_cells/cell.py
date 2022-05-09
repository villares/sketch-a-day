from math import sqrt
from py5 import *
from functools import cache


SIN_60 = sqrt(3) * 0.5  # sin(radians(60))

class mock_cell:
    state = 1
    gen = 0

class Cell():

    board = dict()
    EVN_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1))
    ODD_NBS = ((0, 1), (0, -1), (-1, 0), (1, 0), (-1,  1), (1,  1))
    W = 6
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
        if rnd:
            self.state = 1 if random(5000 / (1 + j)) < 1 else 0
        else:
            self.state = 0
        self.next_state = self.state
        self.gen = 0
        self.nbs = 0

    def display(self):
        if self.state:
            with push_matrix():
                translate(self.x, self.y)
                # strokeWeight(self.H * 2 * self.j / 100)
                # strokeWeight(4.5 - (abs(self.gen / 5.0) % 4))
                d = (4 + 4 * sin(self.gen / 5.0))
                fill(d * 16, 200, 200) #42 * self.nbs)
                no_stroke()
                self.hexagon(Cell.W)

    def calc_live_nbs(self):
        nbs = self.EVN_NBS if self.i % 2 == 0 else self.ODD_NBS
        return sum(self.get_neighbour(i_offset, j_offset).state
                   for i_offset, j_offset in nbs)


    def get_neighbour(self, i_offset, j_offset):
        return self.board.get((self.i + i_offset,
                               self.j + j_offset),
                               mock_cell())

    def get_live_nbs(self):
        nbs = self.EVN_NBS if self.i % 2 == 0 else self.ODD_NBS
        return [self.get_neighbour(i_offset, j_offset)
                for i_offset, j_offset in nbs
                if self.get_neighbour(i_offset, j_offset).state]

    def calc_next_state(self):
        self.nbs = nbs = self.calc_live_nbs()

        # if nbs == 1 or nbs == 2 and self.state == 0:
        #     self.next_state = 1
        #     lnbs = self.get_live_nbs()
        #     if lnbs:
        #         self.gen = lnbs[-1].gen + 1
        # elif nbs > 4:
        #     self.next_state = 0
        # else:
        #    self.next_state = self.state

        # muito bom
        if nbs == 2 and self.state == 0:
            self.next_state = 1
            lnbs = self.get_live_nbs()
            if lnbs:
                self.gen = lnbs[-1].gen + 1
        elif nbs > 4:
            self.next_state = 0
        else:
            self.next_state = self.state

        # if nbs == 1 and self.state == 0:
        #     self.next_state = 1
        #     lnbs = self.get_live_nbs()
        #     if lnbs:
        #         self.gen = lnbs[0].gen + 1
        # elif nbs > 3:
        #     self.next_state = 0
        # else:
        #    self.next_state = self.state

    def check_click(self, mx, my):
        if (self.mouse_over(mx, my) and
                self.__class__.last_clicked != self):
            self.state ^= 1
            self.__class__.last_clicked = self

    def mouse_over(self, mx, my):
        return dist(self.x, self.y, mx, my) < self.H

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
