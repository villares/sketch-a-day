# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s151", ".gif"  # 180530

add_library('gifAnimation')
from gif_export_wrapper import *

GRID_SIZE = 4

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
    fill(200, 5)
    noStroke()
    rect(0, 0, width, height)
    for p in Ponto.PONTOS:
        p.update()
    # noLoop() # for debug

    if frameCount > 100 and not frameCount % 2:
        gif_export(GifMaker, frames=200, filename=SKETCH_NAME)

class Ponto():
    PONTOS = []

    def __init__(self, x, y):
        self.ox = x
        self.oy = y
        self.tx = int(random(100))
        self.ty = random(100)
        self.random_speed = 0.01
        while int(width/10*noise(self.tx)) > 10:
            self.tx += 1
        while int(height/10*noise(self.ty)) > 10:
            self.ty += 1
        print(
              int(width/10h*noise(self.tx)),
              int(width/10*noise(self.ty))
              )

    def update(self):
        self.tx += self.random_speed
        self.x = width/10*noise(self.tx)
        self.ty += self.random_speed
        self.y = height/10*noise(self.ty)
        self.plot()

    def plot(self):
        fill(0)
        noStroke()
        with pushMatrix():
            translate(self.ox, self.oy)
            ellipse(self.x, self.y, 5, 5)
        
# def keyPressed():
#     redraw() # for debug

def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
