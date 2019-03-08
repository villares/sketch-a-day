# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s147", ".gif"  # 180527

add_library('gifAnimation')
from gif_export_wrapper import *

GRID_SIZE = 50

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
    background(0)
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
        
    def set_neighbours(self):
        self.ort_ngb = [] # orthogonal neighbours
        self.dia_ngb = [] # diagonal neighbours
        for p in Ponto.PONTOS:
            d = dist(p.px, p.py, self.px, self.py)
            if  Ponto.spacing * 1.41 < d < Ponto.spacing * 1.42:
                self.dia_ngb.append(p)
            elif  d < Ponto.spacing * 1.41:
                self.ort_ngb.append(p)

    def update(self):
        rx = random(-0.5, 0.5)
        ry = random(-0.5, 0.5)
        if abs(self.px + rx - self.x) < Ponto.spacing * 0.25:
            self.px += rx
        if abs(self.py + ry - self.y) < Ponto.spacing * 0.25:
            self.py += ry
        self.plot()

    def plot(self):
        for p in self.ort_ngb + self.dia_ngb:
            d = dist(p.px, p.py, self.px, self.py)
            if  Ponto.spacing * .9 < d <= Ponto.spacing * 1.2:
                stroke(128, 0, 0)
                line(p.px, p.py, self.px, self.py)
            elif  d < Ponto.spacing * 0.9:
                stroke(255)    
                line(p.px, p.py, self.px, self.py)


def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
