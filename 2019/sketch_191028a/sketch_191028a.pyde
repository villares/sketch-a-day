s = -1000
rnd_mult = 0

def setup():
    size(600, 600)
    
def draw():
    randomSeed(s)
    background(200, 240, 240)
    translate(300, 400)
    galho(60)
    
def galho(tamanho):
    line(0, 0, 0, -tamanho)
    angulo = radians(mouseX % 360)
    encurtamento = 0.8 + 0.10 * rnd_mult * random(1) 
    if tamanho > 10:
        pushMatrix()
        translate(0, -tamanho)
        rotate(angulo)
        galho(tamanho * encurtamento)
        rotate(-angulo * 2)
        galho(tamanho * encurtamento)
        popMatrix()
        
def keyPressed():
    global s, rnd_mult
    if keyCode == LEFT:
        s -= 1
    if keyCode == RIGHT:
        s += 1
    if keyCode == DOWN and rnd_mult > 0:
        rnd_mult -= .01
    if keyCode == UP and rnd_mult < 1:
        rnd_mult += .01
    if key == 's':
        saveFrame("arvore{}-{}.png".format(s, mouseX % 360))
