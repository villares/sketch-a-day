from __future__ import division

# add_library('gifAnimation')
# from villares.gif_export import gif_export

def setup():
    global grid
    size(640, 640)
    rectMode(CENTER)
    colorMode(HSB)
    noSmooth()
    grid = Cell(0, 0, width, 4, deep=True)

def draw():
    global f
    f = frameCount / 40.0
    background(0)
    ortho()
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

    def __init__(self, x, y, cw, n=0, deep=False):
        self.x = x
        self.y = y
        self.cw = cw
        self.parent = self  # for root Cell
        self.children = Cell.rec_grid(x, y, cw, n, deep) if n else None
        if self.children:
            for c in self.children:
                c.parent = self
                 
    def plot(self):
        if not self.children:
            noFill()
            # square(self.x, self.y, self.cw / 2)
            self.lerp_square()
        else:
            for c in self.children:
                # stroke(8 + 2 * (c.cw + 2), 255, 255)
                # line(self.x, self.y,
                #      c.x, c.y)
                # square(self.x, self.y, self.cw)
                # circle(c.x, c.y, c.cw / 4)
                c.plot()

    def lerp_square(self):
        xa, ya = self.x, self.y
        xb, yb = self.parent.x, self.parent.y
        cwa, ra = cwb = self.cw, 0
        cwb, rb = self.parent.cw, self.parent.cw / 4
        # t = map(mouseX, 0, width, 0, 2)
        t = 1 + cos(PI + f)
        xc, yc, cwc, rc = [lerp(a, b, t) for a, b in ((xa, xb),
                                                      (ya, yb),
                                                      (cwa, cwb),
                                                      (ra, rb))]
        stroke(8 + 2 * (cwc + 2) - rc, 255, 255)
        rect(xc, yc, cwc, cwc, rc)

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
