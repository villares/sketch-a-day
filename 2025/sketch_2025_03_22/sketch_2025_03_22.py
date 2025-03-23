
def setup():
    size(600, 600)
    frame_rate(10)
    color_mode(HSB) # Matiz, Sat, Bri
    no_stroke()
    
def draw():
    #background(0)
    fill(0, random(32))
    rect(0, 0, width, height)
    num = 1 + int(mouse_y / 10)
    largura = altura = width / num
    for fila in range(num):
        y = fila * altura + altura / 2
        for coluna in range(num):  # 0, 1, ... 9
            x = coluna * largura + largura / 2
            fill(random(64, 200), 200, 255, 200)
            d = random(10, largura)
            d = d + d * sin(radians(x + frame_count * 10))
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

    
    
    
    
    

