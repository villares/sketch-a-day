from pyp5js import *

def setup():
    createCanvas(500, 500)
    for i in range(-9, 10):
        for j in range(-9, 10):
            Point(i, j)

def draw():
    background(240, 240, 200)
    translate(width / 2, height / 2)
    for p in Point.grid.values():
        p.plot()


class Point():

    grid = dict()
    nbr = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.grid[(i, j)] = self
        self.space = random(45, 55)

    def place(self):
        x, y = self.i * self.space, self.j * self.space
        mx, my = mouseX - width / 2, mouseY - height / 2
        a = self.space / sqrt(1 + dist(x, y, mx, my) / 100)
        return (self.i * a, self.j * a)

    def plot(self):
        stroke(0)
        for oi, oj in self.nbr:
            nbr_ij = (self.i + oi, self.j + oj)
            other = self.grid.get(nbr_ij)
            if other:
                ox, oy = other.place()
                sx, sy = self.place()
                mx, my = (ox + sx) / 2., (oy + sy) / 2.
                line(mx, my, sx, sy)
