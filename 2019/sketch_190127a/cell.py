# -*- coding: utf-8 -*-
from random import choice
from bar import bar

class Cell():
    border = 0
    RES = 4.
    grid = dict()
    debug_mode = False
    # constants
    variations = "abcde"
    N, A, I, T, L, C, E = type_names = "NAITLCE"
    module_types = {"11111": A,  # All neighbours on
                    "00100": N,  # No neighbours on - isolated
                    "01111": T,  # T-shaped (three neighbours)
                    "11110": T,
                    "11101": T,
                    "10111": T,
                    "10101": I,  # I - Up & down or Left and Right
                    "01110": I,
                    "01100": C,  # Cap - single neighbour
                    "00110": C,
                    "00101": C,
                    "10100": C,
                    "01101": L,  # L-shaped (two neighbours)
                    "10110": L,
                    "00111": L,
                    "11100": L,
                    "00000": E,  # Empty - not used at this point
                    # "10000": E,
                    # "01000": E,
                    # "00010": E
                    }

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

        self.identify_module(Cell.ONL)
        self.type = Cell.module_types.get(self.module, "")

    def plot(self, mode):
        rnd = choice(Cell.variations)
        mode_variation = {1: "a",
                          2: "b",
                          3: "c",
                          4: "d",
                          5: "e",
                          6: Cell.variation_dict.get(Cell.module_types.get(self.module)),
                          7: rnd
                          }
        if self.state:
            strokeWeight(1)
            self.variation = mode_variation.get(mode, self.variation)
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
            # rotation = {"11110": PI,
            #             "10110": PI,
            #             "00101": PI,
            #             "11101": HALF_PI,
            #             "01110": HALF_PI,
            #             "11100": HALF_PI,
            #             "00110": HALF_PI,
            #             "11111": HALF_PI * self.ang,
            #             "10111": PI + HALF_PI,
            #             "00111": PI + HALF_PI,
            #             "01100": PI + HALF_PI
            #             }
            # rotation appropriate for each type
            # rotate(rotation.get(self.module, 0))

            # for i in range(Cell.step_start,
            #                Cell.step_end,
            #                Cell.step):  # (-28, 29, 7):
            #     #translate(0, 0, (a + i))
            #     stroke(16 + i * 8, 255, 255)
            #     #stroke(self.index[2] * 8, 255, 255)
            strokeWeight(2)
            stroke(255)
            box(siz / 3)
            strokeWeight(2)
            i, j, k = self.index
            for (ni, nj, nk) in Cell.ONL:
                nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
                if nb and nb.state:
                    stroke(200)
                    with pushMatrix():
                        translate(ni * siz / 3, nj * siz / 3, nk * siz / 3)
                        box(siz / 3)
            for (ni, nj, nk) in Cell.DNL:
                nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
                if nb and nb.state:
                    stroke(64 + (ni * 2 + nj * 3 + nk * 5) * 16, 255, 200)
                    with pushMatrix():
                        translate(ni * siz / 3, nj * siz / 3, nk * siz / 3)
                        box(siz / 3)
                    # bar(0, 0, 0,
                    #      ni * siz, nj * siz, nk * siz,
                    #      ni * 2 + nj * 3 + nk * 5)

    def identify_module(self, nbs):
        i, j, k = self.index
        self.module = ""
        for (ni, nj, nk) in nbs:
            nb = Cell.grid.get((i + ni, j + nj, k + nk), None)
            if nb and nb.state:
                self.module += "1"
            else:
                self.module += "0"

    @staticmethod
    def variation_choices():
        Cell.variation_dict = dict()
        for t in Cell.type_names:
            Cell.variation_dict[t] = choice(Cell.variations)
