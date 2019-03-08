# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s152", ".gif"  # 180601

add_library('gifAnimation')
from gif_export_wrapper import *

GRID_SIZE = 10

def setup():
    size(500, 500)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 25
    spacing = (width - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE):
            Ponto.PONTOS.append(Ponto(border + spacing / 2 + i * spacing,
                                      border + spacing / 2 + j * spacing
                                ))

def draw():
    fill(200, 4)
    noStroke()
    rect(0, 0, width, height)
    for p in Ponto.PONTOS:
        p.update()
    for p in Ponto.PONTOS:
        p.plot()
    #noLoop()

    if  frameCount % 2:
        gif_export(GifMaker, frames=200, filename=SKETCH_NAME)

class Ponto():
    PONTOS = []

    def __init__(self, x, y):
        self.tx = int(random(100))
        self.ty = int(random(100))
        self.random_speed = 0.01
        self.space = Ponto.spacing * 5
        self.ox = x - self.space*noise(self.tx)
        self.oy = y - self.space*noise(self.ty)

    def update(self):
        self.tx += self.random_speed
        self.x = self.space*noise(self.tx)
        self.ty += self.random_speed
        self.y = self.space*noise(self.ty)
        self.px = self.ox + self.x
        self.py = self.oy + self.y

    def plot(self):
        fill(0)
        noStroke()
        for p in Ponto.PONTOS:
            if p != self and dist(p.px, p.py,
                                  self.px, self.py) < Ponto.spacing * 1:
                if frameCount % 2:  # só desenha a linha um frame sim outro não
                    stroke(100, 0, 200)
                    line(p.px, p.py, self.px, self.py)
        fill(0)
        noStroke()
        ellipse(self.px, self.py, 3, 3)
        
def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
