"""
Yet another noise thing
"""

add_library('GifAnimation')
from gif_animation_helper import gif_export
sketch_name = '2020_05_10a'

escala = 0.002
xo = yo = zo = 0
s_len = 18
def setup():
    size(500, 500)
    rectMode(CENTER)

def draw():
    a = TWO_PI / 360 * frameCount
    xo = width + width * sin(a)
    yo = height + height * cos(a)

    background(0)
    for x in range(-30, width + 30, 10):
        for y in range(-30, height + 30, 10):
            ny = noise((y + yo) * escala,
                       (x) * escala,
                       # yo* escala,
                       )
            nx = noise((x + xo) * escala,
                       (y) * escala,
                       # xo * escala,
                       )
            
            
            pushMatrix()
            translate(nx * width, ny * height)
            rotate(TWO_PI * nx)
            noFill()
            stroke(255, 128)
            square(0, 0, s_len)
            popMatrix()
            pushMatrix()
            translate(nx * width, ny * height)
            rotate(TWO_PI * ny)
            stroke(0, 0, 200, 64)
            square(0, 0, s_len)
            popMatrix()

    # if frameCount % 2:
    #     gif_export(GifMaker, sketch_name, quality=32, delay=220)
    # if frameCount > 360:
    #     gif_export(GifMaker, finish=True)

def keyPressed():
    global xo, yo, zo, s_len, escala

    if key == 'd':
        escala += 0.001
    if key == 'c':
        escala -= 0.001
    if key == 's':
        s_len += 1
    if key == 'x':
        s_len -= 1
    # if key == 'a':
    #     zo +=10
    # if key == 'z':
    #     zo -=10
    # if keyCode == UP:
    #     yo -=10
    # if keyCode == DOWN:
    #     yo +=10
    # if keyCode == RIGHT:
    #     xo +=10
    # if keyCode == LEFT:
    #     xo -=10

    # if key == 'q':
    #     gif_export(GifMaker, "animation", finish=True)
