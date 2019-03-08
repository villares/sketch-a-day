# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s150", ".png"  # 180530

# add_library('gifAnimation')
# from gif_export_wrapper import *

GRID_SIZE = 15

def setup():
    size(500, 500)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 25
    spacing = (width - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE):
            Ponto.PONTOS.append(Ponto(border + spacing / 2 + i * spacing,
                                      border + spacing / 2 + j * spacing,
                                      random_range= map(j, 0, GRID_SIZE, 0.1, 1))
                                )

def draw():
    fill(200, 5)
    noStroke()
    rect(0, 0, width, height)
    for p in Ponto.PONTOS:
        p.update()

class Ponto():
    PONTOS = []

    def __init__(self, x, y, random_range):
        self.x = x
        self.y = y
        self.px = x
        self.py = y
        self.random_range = random_range
        self.random_speed = 1

    def update(self):
        rx = random(-self.random_speed, self.random_speed)
        ry = random(-self.random_speed, self.random_speed)
        if abs(self.px + rx - self.x) < Ponto.spacing * self.random_range:
            self.px += rx
        if abs(self.py + ry - self.y) < Ponto.spacing * self.random_range:
            self.py += ry
        self.plot()

    def plot(self):
        for p in Ponto.PONTOS:
            if p != self and dist(p.px, p.py,
                                  self.px, self.py) < Ponto.spacing * 1.5:
                if frameCount % 2:  # só desenha a linha um frame sim outro não
                    stroke(255, 0, 0)
                    line(p.px, p.py, self.px, self.py)
        fill(0)
        noStroke()
        ellipse(self.px, self.py, 5, 5)

def keyPressed():
    saveFrame(SKETCH_NAME + OUTPUT)

def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
