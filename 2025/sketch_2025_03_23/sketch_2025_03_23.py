
def setup():
    size(600, 600)
    color_mode(HSB) # Matiz, Sat, Bri
    no_stroke()
    
def draw():
    background(0)
    num = 1 + int(mouse_y / 10)
    R = width / num
    largura = R * 1.5
    altura = R * sqrt(3)
    random_seed(int(R))
    
    for fila in range(num):
        for coluna in range(num):  # 0, 1, ... 9
            x = coluna * largura
            y = fila * altura + altura / 2 + (altura / 2 if coluna % 2 else 0)
            D = R + R / 2 * sin(radians(x + frame_count * 10))
            for i in range(1, 5):
                fill(random(64, 200), 200, 255, 200)
                d = random(D / i)
                poligono(x, y, d)

def poligono(xc, yc, ra, pontos=6):
    ang = TWO_PI / pontos
    begin_shape()
    for i in range(pontos):
        x = xc + cos(ang * i) * ra
        y = yc + sin(ang * i) * ra
        vertex(x, y)
    end_shape(CLOSE)

def estrela(xc, yc, ra, rb, pontas=6, rot=0):
    ang = TWO_PI / pontas
    begin_shape()
    for i in range(pontas):
        x = xc + cos(rot + ang * i) * ra
        y = yc + sin(rot + ang * i) * ra
        vertex(x, y)
        x = xc + cos(rot + ang * i + ang / 3) * rb
        y = yc + sin(rot + ang * i + ang / 3) * rb
        vertex(x, y)
    end_shape(CLOSE)

    
    
    
    
    

