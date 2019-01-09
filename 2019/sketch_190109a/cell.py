# -*- coding: utf-8 -*-
from random import choice
from arcs import quarter_circle, half_circle, circle_arc, bar


class Cell():
    grid = dict()
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
        if self.state:
            strokeWeight(1)
            if mode == 0:
                self.variation = ""
            if mode == 1:
                self.variation = "a"
            if mode == 2:
                self.variation = "b"
            if mode == 3:
                self.variation = "c"
            if mode == 4:
                self.variation = choice(("a", "b", "c"))
            if mode == -1:
                fill(100, 100)
                noStroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
                noFill()
            siz = self.size_
            l = siz / 2.
            a = l / 2. - 1
            c = l / 2. + 1

            if mode == 6:
                i, j = self.index
                for (ni, nj) in Cell.DNL:
                    nb = Cell.grid.get((i + ni, j + nj), None)
                    if nb and nb.state and ni <> 0 and nj <> 0:
                        for ii in range(Cell.step_start,
                                       Cell.step_end,
                                       Cell.step):  # (-28, 29, 7):                           
                            stroke(64 + ii * 8, 128, 64 - ii * 8)
                            bar(self.pos.x,
                                self.pos.y,
                                nb.pos.x,
                                nb.pos.y,
                                Cell.step + (a + ii) * 2)
                       

            """ draws node """
            with pushMatrix():
                translate(self.pos.x, self.pos.y)
                noFill()  # stroke(0)
                # base rect
                #stroke(0, 0, 200, 50)
                #rect(0, 0, siz, siz)
                #text(self.type, 0, 0)
                # inv t & inv l
                if (self.type == "11110" or
                        self.type == "10110" or
                        self.type == "00101"
                    ):
                    rotate(PI)
                if (self.type == "11101" or
                        self.type == "01110" or
                        self.type == "11100" or
                        self.type == "00110" or
                        (self.type == "11111" and self.ang % 2)
                    ):  # t r & i
                    rotate(HALF_PI)
                if (self.type == "10111" or
                        self.type == "00111" or
                        self.type == "01100"
                    ):  # t l
                    rotate(PI + HALF_PI)

                for i in range(Cell.step_start,
                               Cell.step_end,
                               Cell.step):  # (-28, 29, 7):
                    stroke(64 + i * 8, 128, 64 - i * 8)
                    if self.type == "11111" and self.variation == "b":
                        quarter_circle(l, l, c + i, TOP + LEFT)
                        quarter_circle(-l, -l, c + i, BOTTOM + RIGHT)
                        quarter_circle(-l, l, c + i, TOP + RIGHT)
                        quarter_circle(l, -l, c + i, BOTTOM + LEFT)
                    if self.type == "11111" and self.variation == "a":
                        #ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                        half_circle(0, l, a - i, TOP)
                        half_circle(0, -l, a - i, BOTTOM)
                    if self.type == "11111" and self.variation == "c":
                        line(+a - i, -l, +a - i, l)
                        line(-a + i, -l, -a + i, l)
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                    #     ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                    elif (self.type == "01111" or  # t
                          self.type == "11110" or
                          self.type == "11101" or
                          self.type == "10111"):  # t
                        if self.variation == "b":
                            #line(-l, a + i, l, a + i)
                            line(-l, -a + i, l, -a + i)
                            #half_circle(-l, 0, a - i, RIGHT)
                            #half_circle(l, 0, a - i, LEFT)
                            #half_circle(0, l, a - i, TOP)
                            quarter_circle(l, l, c + i, TOP + LEFT)
                            #quarter_circle(-l, -l, c + i, BOTTOM + RIGHT)
                            quarter_circle(-l, l, c + i, TOP + RIGHT)
                            #quarter_circle(l, -l, c + i, BOTTOM + LEFT)
                            #ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                        elif self.variation == "c":
                            half_circle(-l, 0, a - i, RIGHT)
                            half_circle(l, 0, a - i, LEFT)
                            half_circle(0, l, a - i, TOP)
                            #ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                        else:
                            line(-l, -a + i, l, -a + i)
                            half_circle(-l, 0, a - i, RIGHT)
                            half_circle(l, 0, a - i, LEFT)
                            half_circle(0, l, a - i, TOP)

                    elif self.type == "10101" or self.type == "01110":
                        if self.variation in "a":
                            line(+a - i, -l, +a - i, l)
                            line(-a + i, -l, -a + i, l)
                            half_circle(0, l, a - i, TOP)
                            half_circle(0, -l, a - i, BOTTOM)
                        if self.variation in "b":
                            line(+a - i, -l, +a - i, l)
                            line(-a + i, -l, -a + i, l)
                        elif self.variation == "c":
                            half_circle(0, l, a - i, TOP)
                            half_circle(0, -l, a - i, BOTTOM)
                            #ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                    elif (self.type == "01101" or
                          self.type == "10110" or
                          self.type == "00111" or
                          self.type == "11100"):  # l
                        if self.variation == "c":
                        # stroke(255, 0, 0)
                        # text(self.type, 0, 0)
                            half_circle(-l, 0, a - i, RIGHT)
                            half_circle(0, l, a - i, TOP)
                        elif self.variation == "b":
                            # stroke(0, 255, 0)
                            # text(self.type, 0, 0)
                            quarter_circle(-l, l, siz - c - i, TOP + RIGHT)
                            i *= -1
                            quarter_circle(-l, l, c - i, TOP + RIGHT)
                            #half_circle(-l, 0, a - i, RIGHT)
                            #half_circle(0, l, a - i, TOP)
                        else:
                            quarter_circle(-l, l, siz - c - i, TOP + RIGHT)
                            #i *= -1
                            #quarter_circle(-l, l, c - i, TOP + RIGHT)
                            half_circle(-l, 0, a - i, RIGHT)
                            half_circle(0, l, a - i, TOP)

                    elif (self.type == "01100" or
                          self.type == "00110" or
                          self.type == "00101" or
                          self.type == "10100"):
                        if self.variation in "ab":
                            line(+a - i, -l, +a - i, 0)
                            line(-a + i, -l, -a + i, 0)
                            half_circle(0, 0, a - i, BOTTOM)
                        if self.variation in "ac":
                            half_circle(0, 0, a - i, TOP)
                            half_circle(0, 0, a - i, BOTTOM)
                            half_circle(0, -l, a - i, BOTTOM)

                    elif self.type == "00100":
                        if self.variation == "b":
                            rect(0, 0, (a - i) * 2, (a - i) * 2, (a - i - 1))
                        elif self.variation == "a":
                            ellipse(0, 0, (a + i) * 2.0, (a + i) * 2.0)
                            ellipse(0, 0, (a - i) * 2.5, (a - i) * 2.5)
                        elif self.variation == "c":
                            half_circle(0, 0, a - i, TOP)
                            half_circle(0, 0, a - i, BOTTOM)

    def find_type(self, nbs):
        i, j = self.index[0], self.index[1]
        self.type = ""
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                self.type += "1"
            else:
                self.type += "0"
