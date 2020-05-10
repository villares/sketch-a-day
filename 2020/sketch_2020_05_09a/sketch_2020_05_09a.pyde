"""
Yet another noise field
"""

# add_library('GifAnimation')
# from gif_animation_helper import gif_export
# sketch_name = '2020_05_09a'

escala = 0.002
xo = yo = zo = 0 
s_len = 18
def setup():
    size(500, 500)
    
def draw():
    a = TWO_PI / 360 * frameCount
    xo = width + width * sin(a)     
    yo = height + height * cos(a) 
    zo = xo + yo
    
    background(240)
    for x in range(-30, width + 30, 10):
        for y in range(-30, height + 30, 10):
            n = noise(x * escala,
                     y * escala,
                     zo * escala)
            pushMatrix()
            translate(x, y)
            rotate(TWO_PI * n)
            s = s_len
            noStroke()
            fill(0, 0, 200)
            triangle(-s, 0, s, 0, s, n * s / 2.)
            popMatrix()
            n = noise(x * escala,
                     y * escala,
                     (zo + yo)* escala)
            pushMatrix()
            translate(x, y)
            rotate(TWO_PI * n)
            s = s_len
            fill(0)
            triangle(-s, 0, s, 0, s, n * s / 2.)
            popMatrix()
            n = noise(x * escala,
                     y * escala,
                     (zo + xo)* escala)
            # pushMatrix()
            # translate(x, y)
            # rotate(TWO_PI * n)
            # s = s_len * n
            # stroke(0)
            # line(-s, 0, s, 0)
            # popMatrix()

    # if frameCount % 2:
    #      gif_export(GifMaker, sketch_name, quality=32, delay=220)
    # if frameCount > 360:
    #     gif_export(GifMaker, finish=True)            

def keyPressed():
    global xo, yo, zo, s_len, escala

    if key == 'd':
        escala += 0.001
    if key == 'c':
        escala -= 0.001
    if key == 's':
        s_len +=1
    if key == 'x':
        s_len -=1
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
        
