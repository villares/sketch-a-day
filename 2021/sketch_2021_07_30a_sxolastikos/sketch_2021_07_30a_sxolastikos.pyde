# Port of tweet by zadgy5534 @sxolastikos #つぶやきProcessing
# https://twitter.com/sxolastikos/status/1421277279456350208
t = 0
w = 400 # tamanho da area de desenho largura e altura

def setup():
    size(w, w)

def draw():
    background(220)
    global t
    t += 0.01  # faz o papel do temp0 passando
    i = 0
    while i < TAU:   # TAU = 2 * PI = 360 graus em radianos 
        beginShape(QUADS)  # teoricamente para desenhar quadriláteros
        n = cos(i * t) * 9
        stroke(n, 99, 99)   # cor do traço
        for j in range(8):
            x = 200 + j % w * n
            y = 200 + j % w * sin(i - t) * 19
            vertex(x, y)
        endShape()
        i += PI / 32
