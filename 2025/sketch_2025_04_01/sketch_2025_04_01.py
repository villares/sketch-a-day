# py5 imported mode sketch, check out py5coding.org 

import py5_tools

def setup():
    size(512, 512)
    no_stroke()
    # I didn't like the compression
    #     py5_tools.animated_gif('out.gif', duration=0.1, frame_numbers=range(1, 73, 2),
    #                            optimize=False)

def draw():
    background(0)    
    R = 10
    largura = R * 1.5
    altura = R * sqrt(3)
    num = int(width / largura)
    
    for fila in range(num):
        for coluna in range(num):  # 0, 1, ... 9
            x = int(coluna * largura)
            if coluna % 2 == 1:  # colunas impares
                y = fila * altura
            else:                # colunas pares
                y = fila * altura + altura / 2
            #circle(x, y, altura)
             
            r = R / 2 + R / 3 * cos(radians(frame_count * 5 + x) )
            fill(128 + 128 * sin(radians(frame_count * 5 + y) ),
                 x / 2, y  / 2, 200)
            poligono(x, y, r * 2)
            
    if frame_count in range(1, 73, 2):
        save_frame('##.png')
            
def poligono(xc, yc, ra, pontos=6):
    ang = TWO_PI / pontos
    begin_shape()
    for i in range(pontos):
        x = xc + cos(ang * i) * ra
        y = yc + sin(ang * i) * ra
        vertex(x, y)
    end_shape(CLOSE)

    
