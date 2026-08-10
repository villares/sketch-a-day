import py5
from py5 import LEFT, RIGHT, TOP, BOTTOM, PI, HALF_PI, TWO_PI
from poly_arcs import quarter_poly, half_poly, poly_arc, bar
from random import choice

CELL_SIZE = 100
modulus = 3
mode = 0
frame_saving = False 
frame_saved = 0

cores_b = (
    '#fec31c',
    '#f15628',
    '#d1212b',
    )
cores_a = (
    '#21a5a8',
    '#1f79ac',
    '#174a92',
    )
#cores_t = cores_a + cores_b


def setup():
    py5.size(1200, 800, py5.P3D)
    py5.color_mode(py5.HSB)
    global grid_size
    grid_size = py5.width / CELL_SIZE
    py5.rect_mode(py5.CENTER)
    py5.stroke_cap(py5.SQUARE)
    Cell.variation_choices()
    Cell.step_start = -10
    Cell.step_end = 11
    Cell.step = 5
    #cam = PeasyCam(this, 200)


def init_grid(f=None):
    # default grid is with random state for cells
    if f == None:
        f = lambda i, j: choice((True, False))
    # number of collums and rows -2 for default cell sized border
    w = int(py5.width // CELL_SIZE)  # - 2
    h = int(py5.height // CELL_SIZE)  # - 2
    # print(w, h)
    for i in range(w):
        for j in range(h):
            # default Cell constructor has border=CELL_SIZE
            Cell.grid[(i, j)] = Cell((i, j), CELL_SIZE, f(i, j), border=0)

def draw():
    global frame_saving, frame_saved
    py5.translate(py5.width / 2, py5.height / 2)
    py5.background(0)
    for c in Cell.grid.values():
        c.update(py5.mouse_x - py5.width / 2, py5.mouse_y - py5.height / 2)
    for c in Cell.grid.values():
        c.plot(mode)

    if frame_saving:
        frame_saving = False
        frame_saved += 1
        py5.save_frame(f'{frame_saved}.png')
        py5.println(frame_saved)

def key_pressed():
    global mode, modulus, frame_saving
    if py5.key == "g" or py5.key == "G":
        frame_saving = True
    if py5.key == "s" or py5.key == "S":
        py5.save_frame("_#######.png")
    if py5.key != py5.CODED and py5.key in "01245679":
        mode = int(py5.key)
    if py5.key == "-":
        mode = -1
    if py5.key == " ":
        t = lambda i, j: True
        f = lambda i, j: False
        init_grid(choice((t, f)))
    if py5.key == "r":
        init_grid()
    if py5.key == "R":
        Cell.variation_choices()
    if py5.key == "x":
        init_grid(lambda i, j: (i + j) % modulus)
    if py5.key == "<" and modulus > 2:
        modulus -= 1
    if py5.key == ">":
        modulus += 1
    if py5.key == "z":
        move_grid()
    if py5.key_code == RIGHT:
        move_grid(x=1, y=0)
    if py5.key_code == LEFT:
        move_grid(x=-1, y=0)
    if py5.key_code == py5.UP:
        move_grid(x=0, y=-1)
    if py5.key_code == py5.DOWN:
        move_grid(x=0, y=1)

def move_grid(x=1, y=1):
    w, h = py5.width // CELL_SIZE, py5.height // CELL_SIZE
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
    RES = 8
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
        self.pos = py5.Py5Vector(
            self.border + self.size_ / 2 + i * self.size_ - py5.width / 2,
            self.border + self.size_ / 2 + j * self.size_ - py5.height / 2)

    def update(self, mx, my):
        # mouse over & selection treatment
        hs = CELL_SIZE / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < mx < px + hs and
                         py - hs < my < py + hs)
        if self.mouse_on and py5.is_mouse_pressed:
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
            py5.stroke_weight(3)
            if 1 <= mode <= len(mode_variation):
                self.variation = mode_variation[mode]
            # self.draw_node()
            if mode == -1:
                py5.fill(255, 100)
                py5.no_stroke()
                py5.rect(self.pos.x, self.pos.y, self.size_, self.size_)
                py5.no_fill()
            elif mode == 8:         # diagonal mode
                self.draw_diagonals()
            else:
                self.draw_mode()


    def draw_mode(self):
        """ draws node """
        siz = self.size_
        l = siz / 2.
        a = l / 2 # * 2  #- 1
        c = l / 2  # + 1
        with py5.push_matrix():
            py5.translate(self.pos.x, self.pos.y)
            if Cell.debug_mode:
                py5.fill(0)
                py5.text(self.type, 0, 0)
            py5.no_fill()  # stroke(0)
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
            py5.rotate(rotation.get(self.module, 0))

            for i in range(Cell.step_start,
                           Cell.step_end,
                           Cell.step):  # (-28, 29, 7):
                #py5.translate(0, 0, (a / 2 + i))
                #py5.stroke(200 + i * Cell.step) #16 + i * 8, 255, 255)
                py5.random_seed(100)
                if py5.random(100) < 2:
                    py5.stroke(255)
                else:
                    py5.stroke(cores_b[i % len(cores_b)])
                
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
                        py5.line(+a - i, -l, +a - i, l)
                        py5.line(-a + i, -l, -a + i, l)
                        half_poly(-l, 0, a - i, RIGHT)
                        half_poly(l, 0, a - i, LEFT)
                    if self.variation in "de":
                        Cell.csquare(a, i)

                elif self.type == Cell.T:
                    if self.variation in "bde":
                        py5.line(-l, -a + i, l, -a + i)
                        quarter_poly(l, l, c + i, TOP + LEFT)
                        quarter_poly(-l, l, c + i, TOP + RIGHT)
                    elif self.variation == "c":
                        pass
                        half_poly(-l, 0, a - i, RIGHT)
                        half_poly(l, 0, a - i, LEFT)
                        half_poly(0, l, a - i, TOP)
                    if self.variation in "ce":
                        Cell.csquare(a, i)
                    if self.variation == "a":
                        py5.line(-l, -a + i, l, -a + i)
                        half_poly(-l, 0, a - i, RIGHT)
                        half_poly(l, 0, a - i, LEFT)
                        half_poly(0, l, a - i, TOP)

                elif self.type == Cell.I:
                    if self.variation in "abde":
                        py5.line(+a - i, -l, +a - i, l)
                        py5.line(-a + i, -l, -a + i, l)
                    if self.variation in "ca":
                        half_poly(0, l, a - i, TOP)
                        half_poly(0, -l, a - i, BOTTOM)
                    if self.variation == "ce":
                        Cell.csquare(a, i)

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
                        Cell.csquare(a, i)

                elif self.type == Cell.C:
                    if self.variation in "ac":
                        half_poly(0, -l, a - i, BOTTOM)
                    if self.variation in "abe":
                        half_poly(0, 0, a - i, BOTTOM)
                    if self.variation in "abde":
                        py5.line(+a - i, -l, +a - i, 0)
                        py5.line(-a + i, -l, -a + i, 0)
                    if self.variation in "dc":
                        Cell.csquare(a, i)
                    if self.variation == "e":
                        half_poly(0, -l / 2, a - i, TOP)

                elif self.type == Cell.N:
                    poly_arc(
                        0, 0, (a - i), # * 2,
                        0, # QUARTER_PI
                        TWO_PI, num_points=8)

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
    def csquare(a, i):
        poly_arc(0, 0, radius=(a-i), start_ang=0, sweep_ang=TWO_PI,
                 num_points=Cell.RES*2)
        #rect(0, 0, (a - i) * 2, (a - i) * 2)

    @staticmethod
    def variation_choices():
        Cell.variation_dict = dict()
        for t in Cell.type_names:
            Cell.variation_dict[t] = choice(Cell.variations)


py5.run_sketch()
