# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "s158b", ".gif"  # 180607

add_library('gifAnimation')
from gif_export_wrapper import *

perlinScale = 0.02
yo = 0

def setup():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    size(500, 500, P3D)
    stroke(200)
    noFill()
    strokeWeight(2)
    #ortho()

def draw():
    #translate(0, 0, 0)
    rotateX(radians(225))
    global yo
    background(0)
    lines = []
    for l in range(-32, 32):
        line_ = []
        beginShape()
        y = l * 10
        for x in range(40, width - 40, 10):
            n = noise((x + yo / 4) * perlinScale,
                      (l * -4 + yo) * 2 * perlinScale)
            a = width/2 - abs(width / 2 - x)
            z = height / 2 + map(n, 0, 1, -a*.75, 0)
            vertex(x, y, z)
            line_.append((x, y, z))
        endShape()
        lines.append(line_)
    yo += 0.5
    for line1, line2 in zip(lines, lines[1:]):
        for i, (x1, y1, z1) in enumerate(line1):
            x2, y2, z2 = line2[i]
            line(x1, y1, z1, x2, y2, z2)

    gif_export(GifMaker, frames=200, filename=SKETCH_NAME)
    # if frameCount <= 50:
    #     saveFrame(OUTPUT)

def print_text_for_readme(name, output):
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
