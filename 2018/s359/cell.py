# -*- coding: utf-8 -*-
from random import choice
from arcs import quarter_circle, half_circle, circle_arc


class Cell():
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

    def __init__(self, index, cell_size, state=False):
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        i, j = index[0], index[1]
        self.pos = PVector(self.size_ / 2 + i * self.size_,
                           self.size_ / 2 + j * self.size_)
        self.type = choice(("f1", "f2", "t", "i", "l"))
        self.ang = choice((0, 1, 2, 3))

    def update(self, mx, my):
        # mouse over & selection treatment
        hs = self.size_ / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < mx < px + hs and
                         py - hs < my < py + hs)
        if self.mouse_on:
            self.mouse_down = True
            if keyPressed:
                self.type = choice(("f1", "f2", "t", "i", "l"))
                self.ang = choice((0, 1, 2, 3))
        elif self.mouse_down:    
            self.state = not self.state
            self.mouse_down = False
            return True
        return False

    def plot(self, mode):
        if self.state:
            strokeWeight(1)
            if mode == -1:
                fill(0)
                noStroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
            noFill()
            if mode == 0:
                stroke(0)
                self.draw_lines(Cell.ONL)
                self.draw_lines(Cell.DNL, -4)
                # self.draw_lines(Cell.DNL)
            elif mode == 1:
                stroke(0, 150, 0)
                self.draw_lines(Cell.ONL)
            elif mode == 2:
                stroke(0, 0, 150)
                self.draw_lines(Cell.DNL)
                
            """ draws node """
            with pushMatrix():
                translate(self.pos.x, self.pos.y)
                rotate(HALF_PI * self.ang)
                noFill()  # stroke(0)
                siz = self.size_
                l = siz / 2.
                a = l / 2. - 1
                c = l / 2. + 1
                stroke(0, 0, 200, 50)
                rect(0, 0, siz, siz)
                for i in range(-4, 5, 4):  # (-28, 29, 7):
                    stroke(32, 64 + i * 8, 64 - i * 8)
                    if self.type == "f1":
                        quarter_circle(l, l, c + i, TOP + LEFT)
                        quarter_circle(-l, -l, c + i, BOTTOM + RIGHT)
                        quarter_circle(-l, l, c + i, TOP + RIGHT)
                        quarter_circle(l, -l, c + i, BOTTOM + LEFT)
                    elif self.type == "f2":
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                        half_circle(0, l, a - i, TOP)
                        half_circle(0, -l, a - i, BOTTOM)
                    elif self.type == "t":
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)                    
                    elif self.type == "i":               
                        half_circle(0, l, a - i, TOP)
                        half_circle(0, -l, a - i, BOTTOM)
                    elif self.type == "l":
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(0, -l, a - i, BOTTOM)
    
    def draw_lines(self, nbs, res=0):
        third = self.size_ / 3.
        i, j = self.index[0], self.index[1]
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                rect(self.pos.x + ni * third * 1.5,
                     self.pos.y + nj * third * 1.5,
                     third + res, third + res)
