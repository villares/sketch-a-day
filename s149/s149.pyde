# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s149", ".gif"  # 180528

add_library('gifAnimation')
from gif_export_wrapper import *

GRID_SIZE = 25

def setup():
    size(1000, 500)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 12.5
    spacing = (height - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE):
            new_ponto = Ponto(border + spacing / 2 + i * spacing,
                              border + spacing / 2 + j * spacing)
            Ponto.PONTOS.append(new_ponto)

    for p in Ponto.PONTOS:
        p.set_neighbours()


def draw():
    noStroke()
    fill(200, 100)
    rect(0, 0, width, height)
    for p in Ponto.PONTOS:
        p.update("A")
    translate(mouseX, 0)
    for p in Ponto.PONTOS:
        p.update("B")

    if frameCount > 100 and not frameCount % 2:
        gif_export(GifMaker, frames=200, filename=SKETCH_NAME)

class Ponto():
    PONTOS = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = x
        self.py = y
        self.link_count = 0

    def set_neighbours(self):
        self.ort_ngb = []  # orthogonal neighbours
        self.dia_ngb = []  # diagonal neighbours
        for p in Ponto.PONTOS:
            d = dist(p.px, p.py, self.px, self.py)
            if Ponto.spacing * 1.41 < d < Ponto.spacing * 1.42:
                self.dia_ngb.append(p)
            elif d < Ponto.spacing * 1.41:
                self.ort_ngb.append(p)
        self.ngb = set(self.ort_ngb + self.dia_ngb)

    def update(self, mode):
        rx = random(-0.5, 0.5)
        ry = random(-0.5, 0.5)
        if abs(self.px + rx - self.x) < Ponto.spacing * .25:
            self.px += rx
        if abs(self.py + ry - self.y) < Ponto.spacing * .25:
            self.py += ry
        if mode == "A":
            self.plot_a()
        else:
            self.plot_b()

    def plot_a(self):
        self.link_count = 0
        for p in self.ngb:
            d = dist(p.px, p.py, self.px, self.py)
            if p in self.ort_ngb and d > Ponto.spacing * 1:
                stroke(0)
                line(p.px, p.py, self.px, self.py)
                self.link_count += 1
            elif p in self.dia_ngb and d > Ponto.spacing * 1.45:
                stroke(0, 0, 128)
                line(p.px, p.py, self.px, self.py)
                self.link_count += 1

    def plot_b(self):
        self.link_count = 0
        for p in self.ngb:
            d = dist(p.px, p.py, self.px, self.py)
            if p in self.ort_ngb and d < Ponto.spacing * 1:
                stroke(0)
                line(p.px, p.py, self.px, self.py)
                self.link_count += 1
            elif p in self.dia_ngb and d < Ponto.spacing * 1.45:
                stroke(0, 0, 128)
                line(p.px, p.py, self.px, self.py)
                self.link_count += 1


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
