from __future__ import division

# add_library('gifAnimation')
# from villares.gif_export import gif_export

def setup():
    global grid
    size(1024, 512)
    rectMode(CENTER)
    colorMode(HSB)
    noSmooth()
    grid = Cell(0, 0, width, height, 8, 4, deep=True)

def draw():
    global f
    f = frameCount / 40.0
    background(0)
    translate(width / 2, height / 2)
    grid.plot()

    # if f <= TWO_PI:
    #     if frameCount % 2:
    #         gif_export(GifMaker, "output")
    # else:
    #     gif_export(GifMaker)
    #     gif_export(GifMaker)
    #     gif_export(GifMaker)
    #     gif_export(GifMaker, finish=True)

class Cell():

    def __init__(self, x, y, cw, ch, cols=0, rows=0, deep=False):
        self.x = x
        self.y = y
        self.cw = cw
        self.ch = ch
        self.parent = self  # for root Cell
        self.children = Cell.rec_grid(x, y, cw, ch, cols, rows, deep) if cols else None
        if self.children:
            for c in self.children:
                c.parent = self

    def plot(self):
        if not self.children:
            noFill()
            t = 0.5 + cos(PI - f + self.x / 320.0) / 2.0
            self.lerp_cell(t)
        else:
            for c in self.children:
                c.plot()

    def lerp_cell(self, t):
        xa, ya = self.x, self.y
        xb, yb = self.parent.x, self.parent.y
        cwa, cha = self.cw, self.ch
        cwb, chb = self.parent.cw, self.parent.ch
        rb, ra = 0, self.parent.cw / 4
        # t = map(mouseX, 0, width, 0, 2)
        xc, yc, cwc, chc, rc = [lerp(a, b, t) for a, b in ((xa, xb),
                                                           (ya, yb),
                                                           (cwa, cwb),
                                                           (cha, chb),
                                                           (ra, rb))]
        stroke(8 + 2 * (cwc + 2) - rc, 255, 255)
        rect(xc, yc, cwc, cwc, rc)

    @classmethod
    def rec_grid(cls, x, y, tw, th, cols, rows, deep=False):
        cw = tw / cols
        ch = th / rows
        xoffset = (cw - tw) / 2.0
        yoffset = (ch - th) / 2.0
        cells = []
        for i in range(cols):
            nx = x + cw * i + xoffset
            for j in range(rows):
                ny = y + ch * j + yoffset
                if (cw > 8 and random(10) < 5) or deep:
                    cs = Cell(nx, ny, cw, ch, 2, 2)
                    cells.append(cs)
                else:
                    cells.append(Cell(nx, ny,
                                      cw - 2, ch - 2,
                                      0))
        return cells

def keyPressed():
    from villares.helpers import sketch_name
    saveFrame(sketch_name() + ".png")
