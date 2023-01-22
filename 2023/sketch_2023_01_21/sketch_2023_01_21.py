import py5
from py5 import TOP, BOTTOM, RIGHT, LEFT

from collections import namedtuple
from random import choice
import pickle

from villares.arcs import quarter_circle, half_circle, circle_arc

mode = 0
CELL_SIZE = 50
modulus = 3

Position = namedtuple('Position', 'x y')

def setup():
    py5.size(1050, 500)
    global grid_size
    grid_size = py5.width / CELL_SIZE
    py5.rect_mode(py5.CENTER)
    # stroke_cap(SQUARE)
    Cell.step_start = -11
    Cell.step_end = 10
    Cell.step = 5
    Cell.rotated_start = False


def init_grid(f=None):
    # default grid is with random state for cells
    if f is None:
        def f(i, j): return choice((True, False))
    # number of collums and rows -2 for default cell sized border
    w = int(py5.width // CELL_SIZE) - 2
    h = int(py5.height // CELL_SIZE) - 2
    for i in range(w):
        for j in range(h):
            # default Cell constructor has border=CELL_SIZE
            Cell.grid[(i, j)] = Cell((i, j), CELL_SIZE, f(i, j))


def draw():
    py5.background(100, 0, 0)
    for c in Cell.grid.values():
        c.update(py5.mouse_x, py5.mouse_y)
    for c in Cell.grid.values():
        c.plot(mode)


def key_pressed():
    global mode, modulus
    if py5.key == 's' or py5.key == 'S':
        py5.save_frame('###.png')
    if py5.key != py5.CODED and py5.key in '01234567789':
        mode = int(py5.key)
    if py5.key == '-':
        mode = -1
    if py5.key == ' ':
        def t(i, j): return True
        def f(i, j): return False
        init_grid(choice((t, f)))
    if py5.key == 'r':
        init_grid()
    if py5.key == 'x':
        init_grid(lambda i, j: (i + j) % modulus)
    if py5.key == 'z':
        move_grid()
    if py5.key == 'd':
        with open('sketch.data', 'wb') as out:
            pickle.dump(Cell.grid, out)
    if py5.key == 'l':
        with open('sketch.data', 'rb') as inp:
            Cell.grid = pickle.load(inp)


def move_grid(x=1, y=1):
    w, h =py5.width // CELL_SIZE,py5.height // CELL_SIZE
    new_grid = dict()
    for i in range(w):
        for j in range(h):
            c = Cell.grid.get((i, j), None)
            if c:
                c.index = ((i + x) % w, (j + y) % h)
                c.calculate_pos()
                new_grid[c.index] = c
    Cell.grid = new_grid


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
        self.variation = choice(('a', 'b', 'c'))
        self.border = border
        self.calculate_pos()

    def calculate_pos(self):
        i, j = self.index
        if self.border is None:
            self.border = self.size_
        self.pos = Position(self.border + self.size_ / 2 + i * self.size_,
                            self.border + self.size_ / 2 + j * self.size_)

    def update(self, mx, my):
        # mouse over & selection treatment
        hs = self.size_ / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < mx < px + hs and
                         py - hs < my < py + hs)
        if self.mouse_on and py5.is_mouse_pressed:
            self.mouse_down = True

        elif self.mouse_down:
            self.state = not self.state
            self.mouse_down = False

        self.find_type(Cell.ONL)

    def plot(self, mode):
        if self.state:
            py5.stroke_weight(2)
            if mode == 1:
                self.variation = 'a'
            if mode == 2:
                self.variation = 'b'
            if mode == 3:
                self.variation = 'c'
            if mode == 4:
                self.variation = ('a', 'b', 'c')[sum(self.index) % 3]
            if mode == -1:
                py5.fill(0)
                py5.no_stroke()
                py5.rect(self.pos.x, self.pos.y, self.size_, self.size_)
            py5.no_fill()

            """ draws node """
            with py5.push_matrix():
                py5.translate(self.pos.x, self.pos.y)
                #rotate(py5.HALF_PI * self.ang)
                py5.no_fill()  # stroke(0)
                siz = self.size_
                l = siz / 2.
                a = l / 2. - 1
                c = l / 2. + 1
                # base rect
                #stroke(0, 0, 200, 50)
                #rect(0, 0, siz, siz)
                #text(self.type, 0, 0)
                # inv t & inv l
                if (self.type == '11110' or
                        self.type == '10110' or
                        self.type == '00101'):
                    py5.rotate(py5.PI)
                if (self.type == '11101' or
                    self.type == '01110' or
                    self.type == '11100' or
                        self.type == '00110'):  # t r & i
                    py5.rotate(py5.HALF_PI)
                if (self.type == '10111' or
                        self.type == '00111' or
                        self.type == '01100'):  # t l
                    py5.rotate(py5.PI + py5.HALF_PI)

                for i in range(Cell.step_start,
                               Cell.step_end,
                               Cell.step):  # (-28, 29, 7):
                    py5.stroke(64 + i * 8, 255, 64 - i * 8)
                    if self.type == '11111' and self.variation == 'a':
                        quarter_circle(l, l, c + i, TOP + LEFT)
                        quarter_circle(-l, -l, c + i, BOTTOM + RIGHT)
                        quarter_circle(-l, l, c + i, TOP + RIGHT)
                        quarter_circle(l, -l, c + i, BOTTOM + LEFT)
                    if self.type == '11111' and self.variation == 'b':
                        #ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                        half_circle(0, l, a - i, TOP)
                        half_circle(0, -l, a - i, BOTTOM)
                    if self.type == '11111' and self.variation == 'c':
                        py5.line(+a - i, -l, +a - i, l)
                        py5.line(-a + i, -l, -a + i, l)
                        half_circle(-l, 0, a - i, RIGHT)
                        half_circle(l, 0, a - i, LEFT)
                    #     ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                    elif (self.type == '01111' or  # t
                          self.type == '11110' or
                          self.type == '11101' or
                          self.type == '10111'):  # t
                        #line(-l, a + i, l, a + i)
                        py5.line(-l, -a + i, l, -a + i)
                        #half_circle(-l, 0, a - i, RIGHT)
                        #half_circle(l, 0, a - i, LEFT)
                        #half_circle(0, l, a - i, TOP)
                        quarter_circle(l, l, c + i, TOP + LEFT)
                        #quarter_circle(-l, -l, c + i, BOTTOM + RIGHT)
                        quarter_circle(-l, l, c + i, TOP + RIGHT)
                        #quarter_circle(l, -l, c + i, BOTTOM + LEFT)
                        #ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                    elif self.type == '10101' or self.type == '01110':
                        if self.variation in 'ab':
                            py5.line(+a - i, -l, +a - i, l)
                            py5.line(-a + i, -l, -a + i, l)
                        elif self.variation == 'c':
                            half_circle(0, l, a - i, TOP)
                            half_circle(0, -l, a - i, BOTTOM)
                            #ellipse(0, 0, (a + i) * 2, (a + i) * 2)
                    elif (self.type == '01101' or
                          self.type == '10110' or
                          self.type == '00111' or
                          self.type == '11100'):  # l
                        if self.variation == 'a':
                            # stroke(255, 0, 0)
                            # text(self.type, 0, 0)
                            half_circle(-l, 0, a - i, RIGHT)
                            half_circle(0, l, a - i, TOP)
                        else:
                            # stroke(0, 255, 0)
                            # text(self.type, 0, 0)
                            quarter_circle(-l, l, siz - c - i, TOP + RIGHT)
                            i *= -1
                            quarter_circle(-l, l, c - i, TOP + RIGHT)
                            #half_circle(-l, 0, a - i, RIGHT)
                            #half_circle(0, l, a - i, TOP)
                    elif (self.type == '01100' or
                          self.type == '00110' or
                          self.type == '00101' or
                          self.type == '10100'):
                        py5.line(+a - i, -l, +a - i, 0)
                        py5.line(-a + i, -l, -a + i, 0)
                        half_circle(0, 0, a - i, BOTTOM)
                    elif self.type == '00100':
                        py5.rect(0, 0, (a - i) * 2, (a - i) * 2, (a - i - 1))
                        # ellipse(0, 0, (a + i) * 2.0, (a + i) * 2.0)
                        # ellipse(0, 0, (a - i) * 2.5, (a - i) * 2.5)

    def find_type(self, nbs):
        i, j = self.index[0], self.index[1]
        self.type = ''
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                self.type += '1'
            else:
                self.type += '0'


py5.run_sketch()
