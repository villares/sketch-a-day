"""Sketch 190514c - abav.lugaralgum.com/sketch-a-day"""

from random import choice, seed

CELL_SIZE, D, RANDOM_SEED = 50, 4, 1

def setup():
    size(620, 620, P3D)
    seed(RANDOM_SEED)
    init_grid(width // CELL_SIZE)


def init_grid(grid_size):
    """Create a grid of Cells/nodes with random states."""
    W, H = width // CELL_SIZE, height // CELL_SIZE
    f = lambda i, j: choice((True, False))
    for i in range(W):
        for j in range(H):
            for k in range(D):
	       cell =  Cell((i, j, k), CELL_SIZE, f(i, j))
                Cell.grid[(i, j, k)] = cell


def draw():
    background(240)
    # orthogonal bars
    for c in Cell.grid.values():
        c.plot(0)
    # diagonal bars
    for c in Cell.grid.values():
        c.plot(1)


def keyPressed():
    init_grid(width // CELL_SIZE)
def bar(x1, y1, z1, x2, y2, z2, weight=10):
    """Draw a box rotated in 3D like a bar/edge."""
    p1, p2 = PVector(x1, y1, z1), PVector(x2, y2, z2)
    v1 = p2 - p1
    rho = sqrt(v1.x ** 2 + v1.y ** 2 + v1.z ** 2)
    phi, the  = acos(v1.z / rho), atan2(v1.y, v1.x)
    v1.mult(0.5)
    pushMatrix()
    translate(x1 + v1.x, y1 + v1.y, z1 + v1.z)
    rotateZ(the)
    rotateY(phi)
    box(weight, weight, p1.dist(p2))
    popMatrix()


class Cell():
    BORDER, grid = 10, dict()

    # ortho neighbours
    ONL = ((+0, -1, +0), (-1, +0, +0), (+1, +0, +0),
           (+0, +1, +0), (+0, +0, -1), (+0, +0, +1))
    # diagonal neighbours
    DNL = ((+1, +1, +0), (-1, -1, +0), (+1, -1, +0),
           (-1, +1, +0), (+0, -1, +1), (-1, +0, +1),
           (+1, +0, +1), (+0, +1, +1), (+0, -1, -1),
           (-1, +0, -1), (+1, +0, -1), (+0, +1, -1))

    def __init__(self, i, siz, state=False):
        """Init a node-Cell and calculate its position."""
        self.index, self.size_, self.state = i, siz, state
        i, j, k = self.index
        self.pos = PVector(
            Cell.BORDER + self.size_ / 2 + i * self.size_,  
            Cell.BORDER + self.size_ / 2 + j * self.size_,  
            k * self.size_ - height / 5)
    def plot(self, mode):
        """Draw node bar/edges with neighbours."""
        ORTHO_STROKE = color(128, 0, 0)
        DIAGO_STROKE = color(0, 0, 128)
        noFill()

        if self.state:
            pushMatrix()
            translate(self.pos.x, self.pos.y, self.pos.z)
            i, j, k = self.index
            if  mode == 0:
                stroke(ORTHO_STROKE)
                neighbour_list = Cell.ONL
                bar_weight = 5
            else:
                stroke(DIAGO_STROKE)
                neighbour_list = Cell.DNL
                bar_weight = 3
            for (ni, nj, nk) in neighbour_list:
                nb = Cell.grid.get((i + ni,
				j + nj,
				k + nk), None)
                if nb and nb.state:
                        bar(0, 0, 0,
                            ni * self.size_ / 2,
                            nj * self.size_ / 2,
                            nk * self.size_ / 2,
			 bar_weight)
            popMatrix()
