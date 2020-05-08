"""
Yet another noise fielf
"""

# add_library('GifAnimation')
# from gif_animation_helper import gif_export
sketch_name = 'sketch_2020_05_7a'

escala = 0.002
xo = yo = zo = 0 
s_len = 30
def setup():
    size(500, 500)
    strokeWeight(2)
    
def draw():
    background(240)
    for x in range(-10, width + 10, 10):
        for y in range(-10, height + 10, 10):
            n = noise(x * escala,
                     y * escala,
                     zo * escala)
            pushMatrix()
            translate(x, y)
            rotate(TWO_PI * n)
            s = s_len * n
            stroke(0, 200, 0)
            line(-s, 0, s, 0)
            popMatrix()
            n = noise(x * escala,
                     y * escala,
                     (zo + yo)* escala)
            pushMatrix()
            translate(x, y)
            rotate(TWO_PI * n)
            s = s_len * n
            stroke(0, 0, 200)
            line(-s, 0, s, 0)
            popMatrix()
            n = noise(x * escala,
                     y * escala,
                     (zo + xo)* escala)
            pushMatrix()
            translate(x, y)
            rotate(TWO_PI * n)
            s = s_len * n
            stroke(0)
            line(-s, 0, s, 0)
            popMatrix()
        
                                        
def keyPressed():
    # gif_export(GifMaker, "animation", quality=10, delay=120)

    global xo, yo, zo, s_len, escala
    if key == 'd':
        escala += 0.001
    if key == 'c':
        escala -= 0.001
    if key == 's':
        s_len +=1
    if key == 'x':
        s_len -=1
    if key == 'a':
        zo +=10
    if key == 'z':
        zo -=10
    if keyCode == UP:
        yo -=10
    if keyCode == DOWN:
        yo +=10
    if keyCode == RIGHT:
        xo +=10
    if keyCode == LEFT:
        xo -=10
        
    # if key == 'q':
    #     gif_export(GifMaker, "animation", finish=True)
        
