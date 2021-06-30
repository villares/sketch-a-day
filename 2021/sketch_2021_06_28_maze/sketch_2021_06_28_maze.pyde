from random import choice

add_library('peasycam')

def setup():
    size(800, 800, P3D)
    cam = PeasyCam(this, 700)
    rectMode(CENTER)
    colorMode(HSB)
    make_grid()
    
def make_grid():
    Cell.cells = []
    for i in range(Cell.grid_size):
        for j in range(Cell.grid_size):
            Cell.cells.append(Cell(i, j))
    for cell in Cell.cells:
        cell.find_nbs()
    Cell.cells[0].current = True
    # Cell.grid_running = True

def draw():
    background(0)
    for cell in Cell.cells:
        cell.display()
        cell.update()

class Cell():
    cells = []
    grid_size = 40
    spacing = 15
    grid_running = False

    def __init__(self, i, j):
        self.i, self.j = i, j
        cell_size, half_cell = self.spacing, self.spacing / 2.0
        half_grid_width = self.grid_size * cell_size / 2.0         
        self.x = i * cell_size + half_cell - half_grid_width
        self.y = j * cell_size + half_cell - half_grid_width
        self.visited = False
        self.current = False
        self.links = []
        self.cor = 0 # 0: flat  1: up

    def display(self):
        noFill()
        stroke(255, 100)
        strokeWeight(1)
        square(self.x, self.y, self.spacing)
        strokeWeight(3)
        for cell in self.links:
            mid_point_x = (cell.x + self.x) / 2.0
            mid_point_y = (cell.y + self.y) / 2.0
            stroke(self.cor % 256, 255, 255)
            line(self.x, self.y, self.cor, mid_point_x, mid_point_y, cell.cor)
            fill(self.cor % 256, 255, 255)
            push()
            translate(0, 0, self.cor)
            circle(self.x, self.y, 5)
            pop()

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
                rnd_choice.cor = self.cor + 1
                self.links.append(rnd_choice)
                self.current = False
            else:
                branch_cells = [cell for cell in Cell.cells
                                if cell.visited and cell.unvisited_nbs]
                if branch_cells:
                    print(len(branch_cells))
                    branch_cell = branch_cells[0] #choice(branch_cells)
                    branch_cell.current = True
                    self.current = False
                else:
                    print("finished")
                    self.grid_running = False

def keyPressed():
        make_grid()
        Cell.grid_running = True
    
