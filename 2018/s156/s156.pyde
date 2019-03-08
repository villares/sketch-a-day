# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s156", ".gif"  # 180605

add_library('gifAnimation')
from gif_export_wrapper import *

perlinScale = 0.02
yo = 0

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(500, 500)
    stroke(255)
    noFill()
    strokeWeight(3)

def draw():
    global yo
    background(100)

    for l in range(-10, 10):
        beginShape()
        for x in range(width):
            n = noise((x + yo / 4) * perlinScale,
                      (l * 5 + yo) * perlinScale)
            y = map(n, 0, 1, -60, 60)
            vertex(x, height / 2 + y + l * 15)
        endShape()
    yo += 0.5

    #gif_export(GifMaker, frames=100, filename=SKETCH_NAME)
    # if frameCount <= 50:
    #     saveFrame(OUTPUT)
    
def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
