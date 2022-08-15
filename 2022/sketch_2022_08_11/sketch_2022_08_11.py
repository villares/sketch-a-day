# based on 2021_06_27
from random import choice
from peasy import PeasyCam

def setup():
    size(800, 800, P3D)
    
    Cell.grid_size = 20
    Cell.spacing = 30

    this = get_current_sketch()
    cam = PeasyCam(this, 700)
    rect_mode(CENTER)
    new_cells()


def new_cells():
    Cell.cells = []
    for i in range(Cell.grid_size):
        for j in range(Cell.grid_size):
            Cell.cells.append(Cell(i, j))
    for cell in Cell.cells:
        cell.find_nbs()
    Cell.cells[0].current = True


def draw():
    background(0)
    for cell in Cell.cells:
        cell.display()
        cell.update()
    frame_rate(5)


class Cell():
    cells = []
    grid_size = 10
    spacing = 40
    grid_running = False

    def __init__(self, i, j):
        self.i, self.j = i, j
        cell_size, half_cell = self.spacing, self.spacing / 2.0
        half_grid_width = self.grid_size * cell_size / 2.0
        self.x = i * cell_size + half_cell - half_grid_width
        self.y = j * cell_size + half_cell - half_grid_width
        self.z = 0
        self.visited = False
        self.current = False
        self.links = []
        self.kind = 0  # 0: flat  1: up -1 : down

    def display(self):
        no_fill()
        stroke(255, 100)
        stroke_weight(1)
        push()
        translate(0, 0, self.z)
        if not is_mouse_pressed:
            if self.kind == 0:
                fill(255, 64)
                square(self.x, self.y, self.spacing)
            else:
                square(self.x, self.y, self.spacing)
        #text(self.kind, self.x, self.y)
        pop()
        stroke(55 * self.kind + 200 * abs(self.kind),
               128 * self.kind + 128 * abs(self.kind), 250)
        stroke_weight(3)
        for cell in self.links:
            mid_point_x = (cell.x + self.x) / 2.0
            mid_point_y = (cell.y + self.y) / 2.0
            mid_point_z = (cell.z + self.z) / 2.0
            if self.kind == 0:
                line(self.x, self.y, self.z, mid_point_x, mid_point_y, self.z)
            else:
                line(self.x, self.y, self.z, mid_point_x, mid_point_y, cell.z)

    def find_nbs(self):
        self.nbs = []
        for cell in Cell.cells:
            if cell != self and dist(cell.x, cell.y,
                                     self.x, self.y) <= Cell.spacing * 1:
                self.nbs.append(cell)
        self.unvisited_nbs = self.nbs[:]

    def recalc_unvisited_nbs(self):
        self.unvisited_nbs = [cell for cell in self.unvisited_nbs
                              if not cell.visited]

    def update(self):
        if self.current and self.grid_running:
            self.recalc_unvisited_nbs()
            self.visited = True
            if self.unvisited_nbs:
                rnd_choice = choice(self.unvisited_nbs)
                rnd_choice.current = True
                rnd_choice.links.append(self)
                if self.kind == 0:
                    rnd_choice.kind = choice((-1, 0, 1))
                    rnd_choice.z = self.z + self.spacing / 4.0 * rnd_choice.kind
                else:
                    rnd_choice.kind = 0
                    rnd_choice.z = self.z + self.spacing / 4.0 * self.kind
                self.links.append(rnd_choice)
                self.current = False
            else:
                branch_cells = [cell for cell in Cell.cells
                                if cell.visited and cell.unvisited_nbs
                                # and cell.kind == 0 # precisa ser plana!
                                ]
                if branch_cells:
                    print(len(branch_cells))
                    rnd_choice = branch_cells[0]  # choice(branch_cells)
                    rnd_choice.current = True
                    self.current = False
                else:
                    print("finished")
                    self.grid_running = False


def key_pressed():
    if key == ' ':
        new_cells()
        Cell.grid_running = True
