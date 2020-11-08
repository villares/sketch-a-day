from random import choice

def setup():
    size(500, 500)
    background(0)   # 0 preto, 255 branco, 128 cinza (n, n, n) -> (n)
    # colorMode(HSB)
    noStroke()
    frameRate(1)
    
def draw():
    background(128)   # 0 preto, 255 branco, 128 cinza (n, n, n) -> (n)
    # laços aninhados ou encaixados (nested loops)
    for y in range(0, 500, 50):
        for x in range(0, 500, 50):
            elemento(x, y)
                        
def elemento(x, y):
    moeda = random(1)
    fill(0, 0, 200)
    funcs = [triangulo_1, triangulo_2, triangulo_3, triangulo_4, estrela]
    func = choice(funcs)
    func(x, y)
    
        
def triangulo_1(x, y):
    # x1, y1, x2, y2, x3, y3
    triangle(x, y, x + 50, y, x, y + 50)
    
def triangulo_2(x, y):
    triangle(x + 50, y + 50, x + 50, y, x, y + 50)
    
def triangulo_3(x, y):
    triangle(x, y, x + 50, y, x + 50, y + 50)

def triangulo_4(x, y):
    triangle(x, y, x, y + 50, x + 50, y + 50)

    
def estrela(cx, cy, raio_a=None, raio_b=None, num_pontas=None):
    raio_a = raio_a or random(5, 15)
    raio_b = raio_b or random(5, 25)
    num_pontas = num_pontas or int(random(5, 13))
    x, y = cx + 25, cy + 25
    passo = TWO_PI / num_pontas
    fill(255, 0, 0)
    beginShape()
    ang = 0
    while ang < TWO_PI:  # enquanto o ângulo for menor que 2 * PI:
        sx = cos(ang) * raio_a
        sy = sin(ang) * raio_a
        vertex(x + sx, y + sy)
        sx = cos(ang + passo / 2.) * raio_b
        sy = sin(ang + passo / 2.) * raio_b
        vertex(x + sx, y + sy)
        ang += passo  # aumente o ângulo um passo
    endShape(CLOSE)
