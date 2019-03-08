# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s145", ".png"  # 180525

# add_library('gifAnimation')
# from gif_export_wrapper import *

GRID_SIZE = 10

def setup():
    size(500, 500)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 15
    spacing = (width - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE):
            Ponto.PONTOS.append(Ponto(border + spacing / 2 + i * spacing,
                                      border + spacing / 2 + j * spacing)
                                )

def draw():
    fill(200, 10)
    rect(0, 0, width, height)
    for p in Ponto.PONTOS:
        p.update()

class Ponto():
    PONTOS = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = x
        self.py = y

    def update(self):
        rx = random(-0.5, 0.5)
        ry = random(-0.5, 0.5)
        if abs(self.px + rx - self.x) < 10:
            self.px += rx
        if abs(self.py + ry - self.y) < 10:
            self.py += ry
        self.plot()

    def plot(self):
        stroke(0)
        for p in Ponto.PONTOS:
            if dist(p.px, p.py,
                    self.px, self.py) < Ponto.spacing * 1.2:
                if frameCount % 2:  # só desenha a linha um frame sim outro não
                    line(p.px, p.py, self.px, self.py)

def keyPressed():
    saveFrame(SKETCH_NAME+OUTPUT)

def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
