1
class Cell():
    # neighbours list
    NL = ((-1, -1), (0, -1), (1, -1),
          (-1, 0), (0, 0), (1, 0),
          (-1, 1), (0, 1), (1, 1))
    ONL = (          (0, -1),
           (-1, 0), (0, 0), (1, 0),
                     (0, 1))
    DNL = ((-1, -1), (1, -1),
                (0, 0),
           (-1, 1), (1, 1))

    def __init__(self, index, cell_size, state=False):
        self.index = index
        self.state = state
        self.size_ = cell_size
        self.mouse_down = False
        i, j = index[0], index[1]
        self.pos = PVector(self.size_ / 2 + i * self.size_,
                           self.size_ / 2 + j * self.size_)

    def update(self):
        # mouse over & selection treatment
        hs = self.size_ / 2
        px, py = self.pos.x, self.pos.y
        self.mouse_on = (px - hs < mouseX < px + hs and
                         py - hs < mouseY < py + hs)
        if self.mouse_on and mousePressed:
            self.mouse_down = True
        if self.mouse_down and not mousePressed:
            self.state = not self.state
            self.mouse_down = False
        if self.mouse_on:
            fill(128, 128)
        else:
            noFill()
        strokeWeight(1)
        stroke(200)
        #rect(self.pos.x, self.pos.y, self.size_, self.size_)

    def plot(self, mode):
        if self.state:
            strokeWeight(self.size_ / 5.)
            if mode == -1:
                fill(0)
                noStroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
            if mode == 0:
                stroke(0)
                self.draw_lines(Cell.NL)
            elif mode == 1:
                stroke(0, 150, 0)
                self.draw_lines(Cell.ONL)
            elif mode == 2:
                stroke(0, 0, 150)
                self.draw_lines(Cell.DNL)
            elif mode == 3:
                stroke(0, 150, 0)
                self.draw_lines(Cell.ONL)
                stroke(0, 0, 150)
                self.draw_lines(Cell.DNL)
            elif mode == 4:
                stroke(0, 150, 0)
                self.draw_lines(Cell.DNL)
                stroke(0, 0, 150)
                self.draw_lines(Cell.ONL)

    def draw_lines(self, nbs):
        third = self.size_ / 3.
        i, j = self.index[0], self.index[1]
        strokeWeight(1)
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                for si in range(3):
                    s = (third + si * third)
                    ellipse(self.pos.x + ni * third * 1.5,
                            self.pos.y + nj * third * 1.5,
                      s, s)
                    #point(self.pos.x, self.pos.y) #, third, third)
                    ellipse(self.pos.x, self.pos.y, s, s)
3
