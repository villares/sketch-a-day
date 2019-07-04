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
    nbr = ((-1, 0), (0, -1), (1, 0), (0, 1))

    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.grid[(i, j)] = self
        self.space = 25
        self.ox = self.x = self.i * self.space
        self.oy = self.y = self.j * self.space

    def place(self):
        offx, offy = self.ox - self.x, self.oy - self.y
        mx, my = mouseX - width / 2., mouseY - height / 2.
        dx, dy = self.ox - mx, self.oy - my
        d = dist(mx, my, dx, dy)
        move_factor = 100 / (1 + d)
        if move_factor > 1:
            self.x += move_factor * (-1 if dx < 0 else 1)
            self.y += move_factor * (-1 if dy < 0 else 1)
        self.x += offx * .01
        self.y += offy * .01
        return (self.x, self.y)

    def plot(self):
        stroke(0)
        fill(128, 100)
        beginShape()
        sx, sy = self.place()
        for oi, oj in self.nbr:
            nbr_ij = (self.i + oi, self.j + oj)
            other = self.grid.get(nbr_ij)
            if other:
                ox, oy = other.place()
                mx, my = (ox + sx) / 2., (oy + sy) / 2.
                vertex(mx, my)
        endShape(CLOSE)
        ellipse(sx, sy, 5, 5)
                 
