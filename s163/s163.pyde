# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s163", ".gif"  # 180601

add_library('peasycam')
add_library('gifAnimation')
from gif_export_wrapper import *

GRID_SIZE = 10

def setup():
    size(500, 500, P3D)
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    border = 25
    spacing = (width - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            Ponto.PONTOS.append(Ponto(border + spacing / 2 + x * spacing,
                                      border + spacing / 2 + y * spacing))
    for i in range(200):
        for p in Ponto.PONTOS:
            p.update()
        for p in Ponto.PONTOS:
            p.record(i)

    cam = PeasyCam(this, 500)
    
def draw():
    background(200)
    translate(-width/2, -height/2, 0)

    for px1, py1, pz1, px2, py2, pz2 in Ponto.RECORD:
            if px1:
                stroke(100, 0, 200)
                line(px1, py1, pz1 * 2, px2, py2, pz2 *2)
            with pushMatrix():
                    translate(0, 0, pz2 *2)
                    noStroke()
                    fill(0)
                    ellipse( px2, py2, 3, 3)
                

    if frameCount % 2:
        pass
        gif_export(GifMaker, frames=100, filename=SKETCH_NAME)

class Ponto():
    PONTOS, RECORD = [], []

    def __init__(self, x, y):
        self.tx = int(random(100))
        self.ty = int(random(100))
        self.random_speed = 0.01
        self.space = Ponto.spacing * 5
        self.ox = x - self.space * noise(self.tx)
        self.oy = y - self.space * noise(self.ty)

    def update(self):
        self.tx += self.random_speed
        self.x = self.space * noise(self.tx)
        self.ty += self.random_speed
        self.y = self.space * noise(self.ty)
        self.px = self.ox + self.x
        self.py = self.oy + self.y

    def record(self, i):
        for other in Ponto.PONTOS:
            if other != self and dist(other.px, other.py,
                                      self.px, self.py) < Ponto.spacing * 1:
                if i % 2:  # só desenha a linha um frame sim outro não
                    Ponto.RECORD.append((other.px, other.py, i, self.px, self.py, i))
                else:
                    Ponto.RECORD.append((None, None, None, self.px, self.py, i))

def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
