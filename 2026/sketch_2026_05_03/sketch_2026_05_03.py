rs = 1
gs = 30

def setup():
    size(600, 600)
    rect_mode(CENTER)  # retângulos desenhados pelo centro
    text_align(CENTER, CENTER)
    no_fill()  # sem contorno
    stroke_weight(3)
    Cell.CELLS = []
    create_grid()

def draw():
    background(127, 100, 127)  # fundo cinza claro

    for cell in Cell.CELLS:
        cell.draw_()


def key_pressed():
    global rs
    if key == ' ':
        rs += 1
        create_grid()
    elif key == 's':
        save_frame('####.png')


def item_at_x_y(x, y, collenction, width_):
    return collection[x + y * width_]

def pointy_hexagon(x, y, r):
    with push_matrix():
        translate(x, y)
        rotate(radians(30))  # pointy, comment out for "flat_hexagon()"
        with begin_closed_shape():
            for i in range(6):
                sx = cos(i * TWO_PI / 6) * r
                sy = sin(i * TWO_PI / 6) * r
                vertex(sx, sy)

def create_grid():
    global GRID_SIDE, RAND_SIZE, SPAC_SIZE
    # seize inputs
    GRID_SIDE =  gs # 0 a 63 linhas e colunas na grade
    #RAND_SIZE = int(input.analog(2) / 16)  # escala a randomização do tamanho
    random_seed(rs)
    # espaçamento entre os elementos
    SPAC_SIZE = int(width / (GRID_SIDE + 0.01))

    # empty list
    Cell.CELLS[:] = []
    v = SPAC_SIZE * 1.5
    h = SPAC_SIZE * sqrt(3)
    for _ in range(1):
        for ix in range(GRID_SIDE):  # um x p/ cada coluna
            # um y p/ cada linha
            for iy in range(GRID_SIDE):
                if iy % 2:
                    x = ix * h + h / 4
                else:
                    x = ix * h - h / 4
                y = iy * v
                Cell.CELLS.append(Cell(x, y))

class Cell():
    CELLS = []

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.status = int(random(2))

    def update_nc(self):
        self.nc = self.neighbours()

    def get_color(self):
        return remap(mouse_x, 0, width,
                     0, remap(self.nc, 0, 6, 0, 255))

    def get_size(self):
        return remap(mouse_x, 0, width,
                     SPAC_SIZE, (SPAC_SIZE / 6) * (1 + self.nc))

    def draw_(self):
        self.update_nc()
        if dist(self.x, self.y, mouse_x, mouse_y) < SPAC_SIZE * 2:
            fill(255)
            text(str(self.nc), self.x, self.y)
            fill(0, 16)
        else:
            no_fill()
        if self.status:
            stroke(self.get_color())
            pointy_hexagon(self.x, self.y, self.get_size())


    def neighbours(self):
        count = 0
        for cell in Cell.CELLS:
            if cell is not self and cell.status:
                if dist(self.x, self.y, cell.x, cell.y) < SPAC_SIZE * 2:
                    count += 1
        return count