# -*- coding: utf-8 -*-
from random import choice
from poly_arcs import quarter_poly, half_poly, poly_arc, bar

class Cell():
    grid = dict()
    border = None
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
    ONL = ((+0, -1),
           (-1, +0), (+0, +0),
           (+1, +0),
           (+0, +1))
    

    def __init__(self, index, cell_size, state=False):
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        self.variation = "a"
        self.ang = choice((0, 1, 2, 3))
        self.res = 2
        self.off = 0
        self.calculate_pos()

    def calculate_pos(self):
        i, j = self.index
        if Cell.border == None:
            border = self.size_
        else:
            border = Cell.border
        self.pos = PVector(border + self.size_ / 2 + i * self.size_ - width / 2,
                           border + self.size_ / 2 + j * self.size_ - height / 2)

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
        self.res = int (5 +  2 * cos( frameCount/10. + self.pos.x/2.))
        mode = self.res
        rnd = choice(Cell.variations)
        mode_variation = {1: "a",
                          2: "b",
                          3: "c",
                          4: "d",
                          5: "e",
                          6: Cell.variation_dict.get(
                               Cell.module_types.get(self.module)
                               ),
                          7: rnd
                          }
        if self.state:
            strokeWeight(2)
            self.variation = mode_variation.get(mode, self.variation)
            if mode == -1:
                fill(100, 100)
                noStroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
                noFill()
            self.draw_mode()

    def draw_mode(self):
        """ draws node """
        siz = self.size_
        l = siz / 2.
        half = self.size_ / 2
        q_minus= siz / 4. - self.off
        q_plus = siz / 4. + self.off
        with pushMatrix():
            translate(self.pos.x, self.pos.y)
            if Cell.debug_mode:
                fill(255)
                text(self.res, 0, 0)
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
            def corner(h, v, i):
                    corner_y = {TOP : siz / 2, BOTTOM: -siz / 2}
                    corner_x = {LEFT : siz / 2, RIGHT: -siz / 2}
                    quarter_poly(corner_x[h], corner_y[v], q_plus + i, h + v, self.res)
                    
            def side(pos, i):
                    x, y = {TOP : (0, half), BOTTOM: (0, -half),
                            LEFT: (half, 0), RIGHT : (-half, 0)}[pos]
                    half_poly(x, y, q_minus - i, pos, self.res)

            def middle(i):
                poly_arc(0, 0, (q_minus-i), 0, TWO_PI, self.res *2)

            for i in range(Cell.step_start,
                           Cell.step_end,
                           Cell.step):  # (-28, 29, 7):
                translate(0, 0, (q_minus + i))
                stroke(16 + i * 8, 255, 255)

                if self.type == Cell.A:
                    if self.variation in "bd":
                        corner(LEFT, TOP, i)
                        corner(LEFT, BOTTOM, i)
                        corner(RIGHT, TOP, i)
                        corner(RIGHT, BOTTOM, i)
                    if self.variation in "ae":
                        for pos in (RIGHT, LEFT, TOP, BOTTOM):
                            side(pos, i)
                    if self.variation == "c":
                        line(+q_minus - i, -l, +q_minus - i, l)
                        line(-q_minus + i, -l, -q_minus + i, l)
                        side(RIGHT, i)
                        side(LEFT, i)
                    if self.variation in "de":
                        middle(i)

                elif self.type == Cell.T:
                    if self.variation in "bde":
                        line(-l, -q_minus + i, l, -q_minus + i)
                        corner(LEFT, TOP, i)
                        corner(RIGHT, TOP, i)
                    elif self.variation in "ac":
                        for pos in (RIGHT, LEFT, TOP):
                            side(pos, i)
                    if self.variation in "ce":
                        middle(i)
                    if self.variation == "a":
                        line(-l, -q_minus + i, l, -q_minus + i)
 
                elif self.type == Cell.I:
                    if self.variation in "abde":
                        line(+q_minus - i, -l, +q_minus - i, l)
                        line(-q_minus + i, -l, -q_minus + i, l)
                    if self.variation in "ca":
                        side(TOP, i)
                        side(BOTTOM, i)
                    if self.variation == "ce":
                        middle(i)

                elif self.type == Cell.L:
                    if self.variation in "acde":
                        half_poly(-l, 0, q_minus - i, RIGHT, self.res)
                        half_poly(0, l, q_minus - i, TOP, self.res)
                    if self.variation in "ab":
                        quarter_poly(-l, l, siz - q_plus - i, TOP + RIGHT, self.res)
                    if self.variation == "b":
                        #quarter_poly(-l, l, siz - q_plus - i, TOP + RIGHT, self.res)
                        i *= -1
                        quarter_poly(-l, l, q_plus - i, TOP + RIGHT, self.res)
                    elif self.variation in "ce":
                        middle(i)

                elif self.type == Cell.C:
                    if self.variation in "ac":
                        half_poly(0, -l, q_minus - i, BOTTOM, self.res)
                    if self.variation in "abe":
                        half_poly(0, 0, q_minus - i, BOTTOM, self.res)
                    if self.variation in "abde":
                        line(+q_minus - i, -l, +q_minus - i, 0)
                        line(-q_minus + i, -l, -q_minus + i, 0)
                    if self.variation in "dc":
                        middle(i)
                    if self.variation == "e":
                        half_poly(0, -l / 2, q_minus - i, TOP, self.res)

                elif self.type == Cell.N:
                    poly_arc(
                        0, 0, (q_minus - i), QUARTER_PI, TWO_PI, self.res *2)

    def identify_module(self, nbs):
        i, j = self.index[0], self.index[1]
        self.module = ""
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                self.module += "1"
            else:
                self.module += "0"

        # num_points=self.res*2):
        #rect(0, 0, (q - i) * 2, (q - i) * 2)

    @staticmethod
    def variation_choices():
        Cell.variation_dict = dict()
        for t in Cell.type_names:
            Cell.variation_dict[t] = choice(Cell.variations)
