# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s131"  # 180511
GRID_SIDE = 200  # colunas na grade
UPDATE = False


def setup():
    global input, GIF_EXPORT
    size(600, 600, P2D)
    frameRate(10)
    # textAlign(CENTER, CENTER)
    noFill()
    Cell.CELLS = []
    GIF_EXPORT = False
    create_grid()


def draw():
    background(200, 150, 0)
    #fill(64, 64, 127, 128)
    #rect(0, 0, width, height)

    for cell in Cell.CELLS:
        cell.draw_()
    # uncomment next lines to export GIF
    global GIF_EXPORT
    if GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=50,
                                delay=200,
                                filename=SKETCH_NAME)
    if UPDATE:
        Cell.update()


def create_grid(mode=0):
    global SPAC_SIZE
    # espaçamento entre os elementos
    SPAC_SIZE = int(width / GRID_SIDE)
    # empty list
    Cell.CELLS[:] = []
    # append new cells to grid
    for x in range(GRID_SIDE):  # um x p/ cada coluna
        for y in range(GRID_SIDE):  # um y p/ cada linha
            new_cell = Cell(x, y)
            Cell.CELL_GRID[x][y] = new_cell
            Cell.CELLS.append(new_cell)
    for cell in Cell.CELLS:
        if mode == 1:
            cell.status = int(random(10) > 9)
        else:
            cell.status = 0
        cell.update_nc()
        cell.color_ = map(cell.nc, 0, 6, 0, 255)


def keyPressed():
    global GIF_EXPORT, UPDATE
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'g':  # save GIF
        GIF_EXPORT = True
    if key == 'h':
        input.help()
    if key == 'r':
        create_grid()
    if key == '1':
        create_grid(1)
    if key == ' ':
        UPDATE = not UPDATE
        for cell in Cell.CELLS:
            cell.update_nc()
            cell.color_ = map(cell.nc, 0, 6, 0, 255)


class Cell():
    CELLS = []
    CELL_GRID = [[None] * GRID_SIDE for _ in range(GRID_SIDE)]

    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.status = 0
        self.nc = 6
        self.next = 0

    def update_nc(self):
        '''
        update neighbour count (self.nc)
        AND apply the 'game' rule
        '''
        self.nc = self.count_neighbours()
        # cells with 1, 5 or 6 neighbours die
        if self.nc < 2:
            self.next = 0
        elif self.nc > 2:
            self.next = 0
        else:
            self.next = 1

    @classmethod
    def update(cls):
        for cell in cls.CELLS:
            cell.status = cell.next
        for cell in cls.CELLS:
            cell.update_nc()
            cell.color_ = map(cell.nc, 0, 6, 0, 255)

    def draw_(self):
        fill(self.color_)
        noStroke()
        s = SPAC_SIZE * 1.2
        v = SPAC_SIZE * 1.5
        h = SPAC_SIZE * sqrt(3)
        if self.y % 2:
            x = self.x * h + h / 4
        else:
            x = self.x * h - h / 4
        y = self.y * v
        if self.status:
            ellipse(x, y, s, s)
            # pointy_hexagon(x, y, s)
            if not UPDATE:
                fill(255, 0, 0)
                textSize(10)
                text(str((self.x, self.y)), x, y)
                text(str((self.nc)), x, y + 10)
        if dist(mouseX, mouseY, x, y) < s:
            if mousePressed:
                self.status = (1, 0)[self.status]

    def count_neighbours(self):
        count = 0
        for cell in self.neighbours():
            if cell and cell.status:
                count += 1
        return count

    def neighbours(self):
        neighbour_list = []
        if self.y % 2:
            offset_list = [(-1, 0), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]
        else:
            offset_list = [(-1, 0), (0, -1), (0, 1), (1, 0), (-1, -1), (-1, 1)]

        for offset_x, offset_y in offset_list:
            try:
                neighbour = Cell.CELL_GRID[
                    self.x + offset_x][self.y + offset_y]
                neighbour_list.append(neighbour)
            except IndexError:
                pass
        return neighbour_list
