"""
This is a variant of the work submited to PCD Porto!

Recursive grid PCD Porto 2021 / Grade recursiva PCD Porto 2021
Alexandre B A Villares - https://abav.lugaralgum.com/

This work started by exploring a series of recursive grids from my sketch-a-day project, 
and this variation is offered to the PCD Porto exhibition.

The recursive grid theme/structure has been a favourite of mine since I learned it from 
Japanese creative coder Takawo Shunsuke (https://twitter.com/takawo) in 2019.

I'm using Processing Python mode, but a version of this code can run on the browser using 
the pyodide WASM interpreter, adapted for drawing with p5js, this tool can be explored
with  the p5pyjs project (https://github.com/berinhard/pyp5js). 

I'd like to dedicate this work to the memory of my father, Alberto Siciliano Villares
who passed away recently. He loved Portugal and would have enjoyed to engage with the 
PCD Porto community and the exhibition works.
"""

from __future__ import division

add_library('gifAnimation')
from villares.gif_export import gif_export

def setup():
    global grid
    size(512, 512, FX2D)
    pixelDensity(2)
    rectMode(CENTER)
    # colorMode(HSB, 255)
    # noSmooth()
    grid = Cell(0, 0, width  - 128, height - 128, 4, 4, deep=True)

def draw():
    global f
    f = frameCount / 40.0
    background(240)
    translate(width / 2, height / 2)
    grid.plot()

    if f <= TWO_PI:
        if frameCount % 2:
            gif_export(GifMaker, "output")
    else:
        gif_export(GifMaker)
        gif_export(GifMaker)
        gif_export(GifMaker)
        gif_export(GifMaker, finish=True)

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
            t = 1 + cos(PI - f + self.x / 1200.0) #/ 2
            self.lerp_cell_plot(t)
        else:
            for c in self.children:

                c.plot()

    def lerp_cell_plot(self, t):
        xa, ya = self.x, self.y
        xb, yb = self.parent.x, self.parent.y
        cwa, cha = self.cw, self.ch
        cwb, chb = self.parent.cw, self.parent.ch
        rb, ra = self.parent.cw / 4.0, 0 
        xc, yc, cwc, chc, rc = [lerp(a, b, t) for a, b in ((xa, xb),
                                                           (ya, yb),
                                                           (cwa, cwb),
                                                           (cha, chb),
                                                           (ra, rb))]
        transp = constrain(260 - rc * 4, 0, 255)
        stroke(8 + 2 * (cwc + 2) - rc, 255, 255, transp)
        stroke(0, transp)
        strokeWeight(constrain(0.5 + rc / 4, 1, 100))
        rect(xc, yc, cwc, cwc, constrain(rc, 0, 100))

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

# def keyPressed():
#     from villares.helpers import sketch_name
#     saveFrame(sketch_name() + "###.png")
