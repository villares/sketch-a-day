"""
Yet another noise field
"""

add_library('GifAnimation')
from gif_animation_helper import gif_export
sketch_name = 'sketch_2020_05_7a'

escala = 0.002
x = y = z = 0 
s_len = 10
def setup():
    size(500, 500)
    colorMode(HSB)
    # strokeWeight(3)
    
def draw():
    background(240)
    for xo in range(0, width, 10):
        for yo in range(0, height, 10):
            n = noise((x + xo) * escala,
                     (y + yo) * escala,
                     z * escala)
            pushMatrix()
            translate(xo, yo)
            rotate(TWO_PI * n)
            s = s_len * n
            line(-s, 0, s, 0)
            popMatrix()
        
def keyPressed():
    gif_export(GifMaker, "animation", quality=10, delay=120)

    global x, y, z, s_len, escala
    if key == 'd':
        escala += 0.001
    if key == 'c':
        escala -= 0.001
    if key == 's':
        s_len +=1
    if key == 'x':
        s_len -=1
    if key == 'a':
        z +=10
    if key == 'z':
        z -=10
    if keyCode == UP:
        y -=10
    if keyCode == DOWN:
        y +=10
    if keyCode == RIGHT:
        x +=10
    if keyCode == LEFT:
        x -=10
        
    if key == 'q':
        gif_export(GifMaker, "animation", finish=True)
        
