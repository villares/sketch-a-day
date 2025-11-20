def setup():
    size(800, 800)
    no_fill()
    espiral(200, 200, 350, 12)    
    espiral(600, 200, 350, 6, 6)    
    espiral(600, 600, 350, 24)    
    espiral(200, 600, 350, 6, 8)    
    save('out.png')

def espiral(xc, yc, tamanho, voltas=12, segmentos=36):
    incremento = (tamanho / voltas) / 2 
    angulo_segmento = TWO_PI / segmentos
    incremento_segmento = incremento / segmentos
    begin_shape()
    for i in range(1, segmentos * voltas + 1):
        raio = i * incremento_segmento
        xv = xc + raio * cos(angulo_segmento * i)
        yv = yc + raio * sin(angulo_segmento * i)
        vertex(xv, yv)
    end_shape()    