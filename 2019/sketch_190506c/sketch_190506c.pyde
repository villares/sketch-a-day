# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# Based on s097 - 180407

add_library('GifAnimation')

from gif_exporter import *
from inputs import *

def setup():
    global input, GIF_EXPORT
    fullScreen()
    #size(600, 600)
    rectMode(CENTER)  # retângulos desenhados pelo centro
    colorMode(HSB)  # linha em preto
    strokeWeight(2)  # espessura de linha 2px
    noFill()  # sem preenchimento
    frameRate(30)  # deixa um pouco mais lento
    GIF_EXPORT = False
    input = Input() 
    
def draw():
    background(200)  # fundo cinza claro

    # 0 a 63, número de linhas e colunas na grade
    grid_elem = int(input.analog(1) / 16)
    # 0 a 63, tamanho base de cada quadrado
    elem_size = int(input.analog(2) / 16)
    # 0 a 63, ativa faixa entre -64 e 63 para randomizar tamanho
    rand_size = int(input.analog(3) / 16)
    # 0 a 63, ativa faixa equivalente para randomizar a posição
    rand_posi = int(input.analog(4) / 16)

    # trava a randomização entre os ciclos de draw
    # mas varia com o número de colunas na grade
    randomSeed(int(input.analog(1)) / 4)
    # calcula o espaçamento entre os quadrandos
    spac_size = int(width / (grid_elem + 1))
    # para cada coluna um x
    for x in range(spac_size / 2, width, spac_size):
        # para cada linha um y
        for y in range(spac_size / 2, width, spac_size):
            # sorteia um tamanho (se o rand_size > 0)
            square_size = elem_size + rand_size * random(-1, 1)
            stroke(square_size * 3, 255, 128)
            rect(x + rand_posi * random(-1, 1),  # desenha um quadrado
                 y + rand_posi * random(-1, 1),
                 square_size,
                 square_size)

    # uncomment next lines to export GIF
    global GIF_EXPORT
    if not frameCount % 20 and GIF_EXPORT:
        GIF_EXPORT = gif_export(GifMaker,
                                frames=1000,
                                delay=300,
                                filename=SKETCH_NAME)

    # Updates reading or draws sliders and checks mouse dragging / keystrokes
    input.update()


def keyPressed():
    global GIF_EXPORT
    if key == 'p':  # save PNG
        saveFrame("####.png")
    if key == 'g':  # save GIF
        GIF_EXPORT = True
    if key == 'h':
        input.help()

    input.keyPressed()

def keyReleased():
    input.keyReleased()

def settings():
    from os import path
    global SKETCH_NAME
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
