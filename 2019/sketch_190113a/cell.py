# -*- coding: utf-8 -*-
from random import choice
from arcs import quarter_circle, half_circle, circle_arc, bar

class Cell():
    grid = dict()
    debug_mode = False
    # constants
    N, A, I, T, L, C, E = "NAITLCE"
    types = {"11111": A, # All neighbours on
             "00100": N, # No neighbours on - isolated
             "01111": T, # T-shaped (three neighbours)
             "11110": T,
             "11101": T,
             "10111": T,
             "10101": I, # I - Up & down or Left and Right
             "01110": I, 
             "01100": C, # Cap - single neighbour
             "00110": C,
             "00101": C,
             "10100": C,
             "01101": L, # L-shaped (two neighbours)
             "10110": L,
             "00111": L,
             "11100": L,
             # "00000": E, # Empty - not used at this point
             # "10000": E,
             # "01000": E,
             # "00010": E
             }

    # neighbours list
    NL = ((-1, -1), (+0, -1), (+1, -1),
          (-1, +0), (+0, +0), (+1, +0),
          (-1, +1), (+0, +1), (+1, +1))
    ONL = ((+0, -1),
           (-1, +0), (+0, +0), (+1, +0),
           (+0, +1))
    DNL = ((-1, -1), (+1, -1),
           (+0, +0),
           (-1, +1), (+1, +1))

    def __init__(self, index, cell_size, state=False, border=None):
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        self.variation = choice(("a", "b", "c"))
        self.ang = choice((0, 1, 2, 3))
        self.border = border
        self.calculate_pos()

    def calculate_pos(self):
        i, j = self.index
        if self.border == None:
            self.border = self.size_
        self.pos = PVector(self.border + self.size_ / 2 + i * self.size_,
                           self.border + self.size_ / 2 + j * self.size_)

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

        self.find_type(Cell.ONL)

    def plot(self, mode):
        quarter = self.size_ / 4.  # - 1
        rnd = choice(("a", "b", "c", "d"))
        mode_variation = {1: "a",
                          2: "b",
                          3: "c",
                          4: "d",
                          5: rnd}
        if self.state:
            strokeWeight(1)
            if 1 <= mode <= 5:
                self.variation = mode_variation[mode]
            self.draw_node()
            if mode == -1:
                fill(100, 100)
                noStroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
                noFill()
            # diagonal mode
            if mode == 6:
                i, j = self.index
                for (ni, nj) in Cell.DNL:
                    nb = Cell.grid.get((i + ni, j + nj), None)
                    if nb and nb.state:
                        for ii in range(Cell.step_start - 2,
                                        Cell.step_end - 2,
                                        Cell.step):  # (-28, 29, 7):
                            stroke(64 - ii * 8, 128, 64 + ii * 8)
                            if ni <> 0 and nj <> 0:
                                bar(self.pos.x, self.pos.y,
                                    nb.pos.x, nb.pos.y,
                                    (quarter + ii) * 2, ends=(0, 1))
                            # else:
                            #     ellipse(self.pos.x, self.pos.y,
                            #             (a + ii) * 2, (a + ii) * 2)

    def draw_node(self):
        """ draws node """
        if Cell.debug_mode:
            stroke(0, 255, 0)
            text(Cell.types(self.type), 0, 0)
        siz = self.size_
        l = siz / 2.
        a = l / 2.  # - 1
        c = l / 2.  # + 1
        with pushMatrix():
            translate(self.pos.x, self.pos.y)
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
            rotate(rotation.get(self.type, 0))
            
            for i in range(Cell.step_start,
                           Cell.step_end,
                           Cell.step):  # (-28, 29, 7):
                stroke(8, 64 + i * 8, 64 - i * 8)

                if Cell.types[self.type] == Cell.A:
                    if self.variation in "bd":
                        quarter_circle(l, l, c + i, TOP + LEFT)
                        quarter_circle(-l, -l, c + i, BOTTOM + RIGHT)
                        quarter_circle(-l, l, c + i, TOP + RIGHT)
                        quarter_circle(l, -l, c + i, BOTTOM + LEFT)
                    if self.variation == "d":
                        ellipse(0, 0, (a - i) * 2, (a - i) * 2)
                    if self.variation == "a":
                        # ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                        half_circle(0, l, a - i, TOP)
                        half_circle(0, -l, a - i, BOTTOM)
                    if self.variation == "c":
                        line(+a - i, -l, +a - i, l)
                        line(-a + i, -l, -a + i, l)
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                        # if keyPressed: ellipse(0, 0, (a - i) * 2, (a - i) * 2)

                elif Cell.types[self.type] == Cell.T:
                    if self.variation in "bd":
                        line(-l, -a + i, l, -a + i)
                        quarter_circle(l, l, c + i, TOP + LEFT)
                        quarter_circle(-l, l, c + i, TOP + RIGHT)
                    elif self.variation == "c":
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                        half_circle(0, l, a - i, TOP)
                    if self.variation in "cd":
                        ellipse(0, 0, (a - i) * 2, (a - i) * 2)
                    if self.variation == "a":
                        line(-l, -a + i, l, -a + i)
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                        half_circle(0, l, a - i, TOP)

                elif Cell.types[self.type] == Cell.I:
                    if self.variation == "d":
                        ellipse(0, 0, (a - i) * 2, (a - i) * 2)
                    if self.variation in "abd":
                        line(+a - i, -l, +a - i, l)
                        line(-a + i, -l, -a + i, l)
                    if self.variation in "ca":
                        half_circle(0, l, a - i, TOP)
                        half_circle(0, -l, a - i, BOTTOM)

                elif Cell.types[self.type] == Cell.L:
                    if self.variation in "a":
                        quarter_circle(-l, l, siz - c - i, TOP + RIGHT)
                    elif self.variation == "b":
                        quarter_circle(-l, l, siz - c - i, TOP + RIGHT)
                        i *= -1
                        quarter_circle(-l, l, c - i, TOP + RIGHT)
                    elif self.variation == "c":
                        ellipse(0, 0, (a - i) * 2, (a - i) * 2)
                    if self.variation in "acd":
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(0, l, a - i, TOP)

                elif Cell.types[self.type] == Cell.C:
                    if self.variation in "ac":
                        half_circle(0, -l, a - i, BOTTOM)
                    if self.variation in "ab":
                        half_circle(0, 0, a - i, BOTTOM)
                    if self.variation in "abd":
                        line(+a - i, -l, +a - i, 0)
                        line(-a + i, -l, -a + i, 0)
                    if self.variation in "dc":
                        ellipse(0, 0, (a - i) * 2, (a - i) * 2)

                elif Cell.types[self.type] == Cell.N:
                    ellipse(0, 0, (a - i) * 2, (a - i) * 2)

    def find_type(self, nbs):
        i, j = self.index[0], self.index[1]
        self.type = ""
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                self.type += "1"
            else:
                self.type += "0"
