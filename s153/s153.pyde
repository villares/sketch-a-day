# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s153", ".gif"  # 180602

add_library('gifAnimation')
from gif_export_wrapper import *

GRID_SIZE = 30

def setup():
    size(500, 500)
    background(0)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 25
    spacing = (width - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    a = 0
    while a < TWO_PI:
                x = cos(a) * spacing * 10
                y = sin(a) * spacing * 10
                Ponto.PONTOS.append(Ponto(width/2 + x, height/2 + y))
                a += TWO_PI/60.
    
def draw():
    #fill(200, 4)
    #noStroke()
    #rect(0, 0, width, height)
    for p in Ponto.PONTOS:
        p.update()
    for p in Ponto.PONTOS:
        p.plot()
    #noLoop()

    if  frameCount > 200 and frameCount % 2:
        gif_export(GifMaker, frames=200, filename=SKETCH_NAME)

class Ponto():
    PONTOS = []

    def __init__(self, x, y):
        self.tx = int(random(100))
        self.ty = int(random(100))
        self.speed = 0.02
        self.space = Ponto.spacing * 5
        self.ox = x - self.space*noise(self.tx)
        self.oy = y - self.space*noise(self.ty)

    def update(self):
        if frameCount > 300: rs = self.speed
        else: rs = -self.speed
        self.tx += rs
        self.x = self.space*noise(self.tx)
        self.ty += rs
        self.y = self.space*noise(self.ty)
        self.px = self.ox + self.x
        self.py = self.oy + self.y

    def plot(self):
        for p in Ponto.PONTOS:
            if p != self and dist(p.px, p.py,
                                  self.px, self.py) < Ponto.spacing * 3:
                if frameCount % 2:  # só desenha a linha um frame sim outro não
                    colorMode(HSB)
                    stroke(4 * (frameCount % 64), 255, 255)
                    line(p.px, p.py, self.px, self.py)
        
def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
