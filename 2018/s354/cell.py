
class Cell():
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
            strokeWeight(1)
            if mode == -1:
                fill(0)
                noStroke()
                rect(self.pos.x, self.pos.y, self.size_, self.size_)
            if mode == 0:
                stroke(0)
                self.draw_lines(Cell.ONL)
                self.draw_lines(Cell.DNL, -4)
                # self.draw_lines(Cell.DNL)
            elif mode == 1:
                stroke(0, 150, 0)
                self.draw_lines(Cell.ONL)
            elif mode == 2:
                stroke(0, 0, 150)
                self.draw_lines(Cell.DNL)
            elif mode == 3:
                stroke(0, 150, 0)
                self.draw_lines(Cell.ONL, -4)
                stroke(0, 0, 150)
                self.draw_lines(Cell.DNL)
            elif mode == 4:
                stroke(0, 150, 0)
                self.draw_lines(Cell.DNL)
                stroke(0, 0, 150)
                self.draw_lines(Cell.ONL, -4)

    def draw_lines(self, nbs, res=0):
        third = self.size_ / 3.
        i, j = self.index[0], self.index[1]
        for (ni, nj) in nbs:
            nb = Cell.grid.get((i + ni, j + nj), None)
            if nb and nb.state:
                rect(self.pos.x + ni * third * 1.5,
                     self.pos.y + nj * third * 1.5,
                     third + res, third + res)
                # point(self.pos.x, self.pos.y) #, third, third)
                #rect(self.pos.x, self.pos.y, third, third)
                arrow(self.pos.x, self.pos.y,
                      self.pos.x + ni * third * 1.5,
                      self.pos.y + nj * third * 1.5,
                      third / 2, third / 2,
                      tail_func=ellipse)
def arrow(x1, y1, x2, y2, shorter=0, head=None,
          tail_func=None, tail_size=None):
    """

    """
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 20, 2)
    if L > head:
      with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        strokeCap(ROUND)
        line(0, L - offset, -head / 3, L - offset - head)
        line(0, L - offset, head / 3, L - offset - head)
        strokeCap(SQUARE)
        line(0, offset, 0, L - offset)

        if tail_func:
            if not tail_size:
                tail_size = head
            tail_func(0, 0, tail_size, tail_size)
