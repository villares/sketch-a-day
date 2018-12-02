
class Cell():
    # neighbours list
    NL = ((-1, -1), (+0, -1), (+1, -1),
          (-1, +0), (+0, +0), (+1, +0),
          (-1, +1), (+0, +1), (+1, +1))
    ONL = ((+0, -1),
           (-1, +0), (+0, +0), (+1, +0),
           (+0, +1))

    def __init__(self, index, cell_size, state=False):
        # Cell.NL = ((-1, -1), (+0, -1), (+1, -1),
        #            (-1, +0), (+0, +0), (+1, +0),
        #            (-1, +1), (+0, +1), (+1, +1))
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        i, j = index[0], index[1]
        self.pos = PVector(self.size_ / 2 + i * self.size_,
                           self.size_ / 2 + j * self.size_)
        # self.ngbs = []
        # for ni, nj in Cell.NL:
        #     self.ngbs.append(
        #         Cell.grid.get((i-ni, j-nj), None))

    def play(self):
        hs = self.size_ / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < mouseX < px + hs and
                         py - hs < mouseY < py + hs)
        if self.mouse_on and mousePressed:
            self.mouse_down = True
        if self.mouse_down and not mousePressed:
            self.state = not self.state
            self.mouse_down = False
        self.plot()

    def plot(self):
        fill(255)
        strokeWeight(1)
        rect(self.pos.x, self.pos.y, self.size_, self.size_)
        if self.state:
            third = self.size_ / 3
            if key == CODED:
                nbs = Cell.NL
            else:
                nbs = Cell.ONL
            i, j = self.index[0], self.index[1]
            strokeWeight(third)
            for (ni, nj) in nbs:
                nb = Cell.grid.get((i + ni, j + nj), None)
                if nb and nb.state:
                    line(self.pos.x + ni * third,
                         self.pos.y + nj * third,
                         self.pos.x, self.pos.y)

        if self.mouse_on:
            with pushStyle():
                fill(128, 128)
                rect(self.pos.x, self.pos.y,
                     self.size_,
                     self.size_
                     )
