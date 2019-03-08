
class Cell():
    # neighbours list
    NL = ((-1, -1), (+0, -1), (+1, -1),
          (-1, +0), (+0, +0), (+1, +0),
          (-1, +1), (+0, +1), (+1, +1))
    ONL = (          (+0, -1),
           (-1, +0), (+0, +0), (+1, +0),
                     (+0, +1))
    DNL = ((-1, -1)          , (+1, -1),
                     (+0, +0),  
          (-1, +1),           (+1, +1))

    def __init__(self, index, cell_size, state=False):
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        i, j = index[0], index[1]
        self.pos = PVector(self.size_ / 2 + i * self.size_,
                           self.size_ / 2 + j * self.size_)

    def play(self, mode):
        # mouse selection treatment
        hs = self.size_ / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < mouseX < px + hs and
                         py - hs < mouseY < py + hs)
        if self.mouse_on and mousePressed:
            self.mouse_down = True
        if self.mouse_down and not mousePressed:
            self.state = not self.state
            self.mouse_down = False
        # go draw yourself!
        self.plot(mode)

    def plot(self, mode):
        stroke(0)
        if self.state:
            third = self.size_ / 3
            if mode == 0:
                nbs = Cell.NL
            elif mode == 1:
                nbs = Cell.ONL
                stroke(0, 150, 0)
            elif mode == 2:
                stroke(0, 0, 150)
                nbs = Cell.DNL
    
            i, j = self.index[0], self.index[1]
            strokeWeight(third)
            for (ni, nj) in nbs:
                nb = Cell.grid.get((i + ni, j + nj), None)
                if nb and nb.state:
                    line(self.pos.x + ni * third * 1.5,
                         self.pos.y + nj * third * 1.5,
                         self.pos.x, self.pos.y)
        strokeWeight(1)
        noFill()
        stroke(100)
        rect(self.pos.x, self.pos.y, self.size_, self.size_)

        if self.mouse_on:
            with pushStyle():
                fill(128, 128)
                rect(self.pos.x, self.pos.y,
                     self.size_,
                     self.size_
                     )
