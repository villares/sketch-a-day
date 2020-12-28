from __future__ import division
# from villares import ubuntu_jogl_fix  # you probably won't need this

# from copy import deepcopy

def setup():
    global grid
    size(640, 640)
    rectMode(CENTER)
    colorMode(HSB)
    noSmooth()
    grid = Cell(0, 0, width, 4, deep=True)

def draw():
    global f
    f = frameCount / 80.0
    background(0)
    ortho()
    translate(width / 2, height / 2)
    # for cell in grid.children:
    #     cell.plot()
    grid.plot()

class Cell():

    def __init__(self, x, y, cw, n=0, deep=False):
        self.x = x
        self.y = y
        self.cw = cw
        self.children = Cell.rec_grid(x, y, cw, n, deep) if n else None

    def plot(self):
        if not self.children:
            noFill()
            stroke(8 + 2 * (self.cw + 2), 255, 255)
            square(self.x, self.y, self.cw/2)
        else:
            for c in self.children:
                stroke(8 + 2 * (c.cw + 2), 255, 255)
                line(self.x, self.y,
                     c.x, c.y)
                # square(self.x, self.y, self.cw)
                circle(c.x, c.y, c.cw/4)
                c.plot()

    @classmethod
    def rec_grid(cls, x, y, tw, n, deep=False):
        cw = tw / n
        margin = (cw - tw) / 2.0
        cells = []
        for i in range(n):
            nx = x + cw * i + margin
            for j in range(n):
                ny = y + cw * j + margin
                if (cw > 8 and random(10) < 5) or deep:
                    cs = Cell(nx, ny, cw, 2)
                    cells.append(cs)
                else:
                    cells.append(Cell(nx, ny, cw - 2, 0))
        return cells
    
def keyPressed():
    from villares.helpers import sketch_name
    saveFrame(sketch_name() + ".png")
