# -*- coding: utf-8 -*-
from random import choice
from poly_arcs import quarter_poly, half_poly, poly_arc, bar

class Cell():
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

    # neighbours list
    NL = ((-1, -1), (+0, -1), (+1, -1),
          (-1, +0), (+0, +0), (+1, +0),
          (-1, +1), (+0, +1), (+1, +1))
    # ortho neighbours
    ONL = ((+0, -1),
           (-1, +0), (+0, +0),
           (+1, +0),
           (+0, +1))
    # diagonal neighbours
    DNL = ((-1, -1), (+1, -1),
           (+0, +0),
           (-1, +1), (+1, +1))

    def __init__(self, index, cell_size, state=False, border=None):
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        self.variation = "a"
        self.ang = choice((0, 1, 2, 3))
        self.border = border
        self.calculate_pos()

    def calculate_pos(self):
        i, j = self.index
        if self.border == None:
            self.border = self.size_
        self.pos = PVector(self.border + self.size_ / 2 + i * self.size_ - width / 2,
                           self.border + self.size_ / 2 + j * self.size_ - height / 2)

    def update(self, mx, my):
        # mouse over & selection treatment
        hs = self.size_ / 2
        px, py = self.pos.x, self.pos.y
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
        quarter = self.size_ / 4.  # - 1
        rnd = choice(Cell.variations)
        mode_variation = {1: "a",
                          2: "b",
                          3: "c",
                          4: "d",
                          5: "e",
                          6: Cell.variation_dict.get(Cell.module_types.get(self.module)),
                          7: rnd
                          }
        self.draw_node()
        if self.state:
            strokeWeight(2)
            if 1 <= mode <= len(mode_variation):
                self.variation = mode_variation[mode]
            # self.draw_node()
            if mode == -1:
                fill(100, 100)
                noStroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
                noFill()

            # diagonal mode
            if mode == 8:
                i, j = self.index
                for (ni, nj) in Cell.DNL:
                    nb = Cell.grid.get((i + ni, j + nj), None)
                    if nb and nb.state:
                        for ii in range(Cell.step_start,
                                        Cell.step_end,
                                        Cell.step):  # (-28, 29, 7):
                            stroke(64 - ii * 8, 255, 255)
                            if ni <> 0 and nj <> 0:
                                bar(self.pos.x, self.pos.y,
                                    nb.pos.x, nb.pos.y,
                                    (quarter + ii) * 2, ends=(0, 1))
                            # else:
                            #     rect(self.pos.x, self.pos.y,
                            #             (a + ii) * 2, (a + ii) * 2)

    def draw_node(self):
        """ draws node """
        siz = self.size_
        l = siz / 2.
        a = l / 2.  # - 1
        c = l / 2.  # + 1
        with pushMatrix():
            translate(self.pos.x, self.pos.y)
            if Cell.debug_mode:
                fill(0)
                text(self.type, 0, 0)
            noFill()  # stroke(0)
            rotation = {"11110": PI,
                        "10110": PI,
                        "00101": PI,
                        "11101": HALF_PI,
                        "01110": HALF_PI,
                        "11100": HALF_PI,
                        "00110": HALF_PI,
                        "11111": HALF_PI * self.ang,
                        "10111": PI + HALF_PI,
                        "00111": PI + HALF_PI,
                        "01100": PI + HALF_PI
                        }
            # rotation appropriate for each type
            rotate(rotation.get(self.module, 0))

            for i in range(Cell.step_start,
                           Cell.step_end,
                           Cell.step):  # (-28, 29, 7):
                translate(0, 0, (a + i))
                stroke(16 + i * 8, 255, 255)

                if self.type == Cell.A:
                    if self.variation in "bd":
                        quarter_poly(l, l, c + i, TOP + LEFT)
                        quarter_poly(-l, -l, c + i, BOTTOM + RIGHT)
                        quarter_poly(-l, l, c + i, TOP + RIGHT)
                        quarter_poly(l, -l, c + i, BOTTOM + LEFT)
                    if self.variation in "ae":
                        half_poly(-l, 0, a - i, RIGHT)
                        half_poly(l, 0, a - i, LEFT)
                        half_poly(0, l, a - i, TOP)
                        half_poly(0, -l, a - i, BOTTOM)
                    if self.variation == "c":
                        line(+a - i, -l, +a - i, l)
                        line(-a + i, -l, -a + i, l)
                        half_poly(-l, 0, a - i, RIGHT)
                        half_poly(l, 0, a - i, LEFT)
                    if self.variation in "de":
                        Cell.square(a, i)
                        
                elif self.type == Cell.T:
                    if self.variation in "bde":
                        line(-l, -a + i, l, -a + i)
                        quarter_poly(l, l, c + i, TOP + LEFT)
                        quarter_poly(-l, l, c + i, TOP + RIGHT)
                    elif self.variation == "c":
                        pass
                        half_poly(-l, 0, a - i, RIGHT)
                        half_poly(l, 0, a - i, LEFT)
                        half_poly(0, l, a - i, TOP)
                    if self.variation in "ce":
                        Cell.square(a, i)
                    if self.variation == "a":
                        line(-l, -a + i, l, -a + i)
                        half_poly(-l, 0, a - i, RIGHT)
                        half_poly(l, 0, a - i, LEFT)
                        half_poly(0, l, a - i, TOP)

                elif self.type == Cell.I:
                    if self.variation in "abde":
                        line(+a - i, -l, +a - i, l)
                        line(-a + i, -l, -a + i, l)
                    if self.variation in "ca":
                        half_poly(0, l, a - i, TOP)
                        half_poly(0, -l, a - i, BOTTOM)
                    if self.variation == "ce":
                        Cell.square(a, i)

                elif self.type == Cell.L:
                    if self.variation in "acde":
                        half_poly(-l, 0, a - i, RIGHT)
                        half_poly(0, l, a - i, TOP)
                    if self.variation in "a":
                        quarter_poly(-l, l, siz - c - i, TOP + RIGHT)
                    elif self.variation == "b":
                        quarter_poly(-l, l, siz - c - i, TOP + RIGHT)
                        i *= -1
                        quarter_poly(-l, l, c - i, TOP + RIGHT)
                    elif self.variation in "ce":
                        Cell.square(a, i)

                elif self.type == Cell.C:
                    if self.variation in "ac":
                        half_poly(0, -l, a - i, BOTTOM)
                    if self.variation in "abe":
                        half_poly(0, 0, a - i, BOTTOM)
                    if self.variation in "abde":
                        line(+a - i, -l, +a - i, 0)
                        line(-a + i, -l, -a + i, 0)
                    if self.variation in "dc":
                        Cell.square(a, i)
                    if self.variation == "e":
                        half_poly(0, -l / 2, a - i, TOP)

                elif self.type == Cell.N:
                    box((a - i) * 2)

    def identify_module(self, nbs):
        i, j = self.index[0], self.index[1]
        self.module = ""
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                self.module += "1"
            else:
                self.module += "0"
                
    @staticmethod
    def square(a, i):
        with pushMatrix():
            #translate(0, 0, (a - i))
            rect(0, 0, (a - i) * 2, (a - i) * 2)

    @staticmethod
    def variation_choices():
        Cell.variation_dict = dict()
        for t in Cell.type_names:
            Cell.variation_dict[t] = choice(Cell.variations)
