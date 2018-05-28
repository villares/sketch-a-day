# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s147", ".gif"  # 180527

add_library('gifAnimation')
from gif_export_wrapper import *

GRID_SIZE = 32

def setup():
    size(500, 500)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 20
    spacing = (width - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE):
            Ponto.PONTOS.append(Ponto(border + spacing / 2 + i * spacing,
                                      border + spacing / 2 + j * spacing)
                                )
    for p in Ponto.PONTOS:
        p.set_neighbours()


def draw():
    fill(0, 0, 100, 100)
    rect(0, 0, width, height)
    for p in Ponto.PONTOS:
        p.update()

    if frameCount > 100 and not frameCount % 2:
        gif_export(GifMaker, frames=200, filename=SKETCH_NAME)

class Ponto():
    PONTOS = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = x
        self.py = y
        self.link_count = 4

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

    def update(self):
        rx = random(-0.5, 0.5)
        ry = random(-0.5, 0.5)
        if abs(self.px + rx - self.x) < Ponto.spacing * .5:
            self.px += rx
        if abs(self.py + ry - self.y) < Ponto.spacing * .5:
            self.py += ry
        if self.link_count > 8:
            self.link_count = 8
        if self.link_count < 0:
            self.link_count = 0
            
        self.plot()

    def plot(self):
        for p in self.ngb:
            d = dist(p.px, p.py, self.px, self.py)
            if Ponto.spacing * .9 < d <= Ponto.spacing * 1.2:
                self.link_count += 1
            elif d < Ponto.spacing * 0.9:
                self.link_count += 1
            else:
                self.link_count -= 1
        for p in self.ngb:
            if p.link_count + self.link_count > 3:
                if p in self.dia_ngb:
                    stroke(0, 0, 255)
                else:
                    stroke(0, 150, 0)
                line(p.px, p.py, self.px, self.py)
        if dist(mouseX, mouseY, self.x, self.y) < Ponto.spacing * 2:
            fill(255)
            textSize(6)
            text(str(self.link_count), self.x, self.y)


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
