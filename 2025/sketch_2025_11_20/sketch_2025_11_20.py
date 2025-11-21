def setup():
    size(800, 800)
    background(0)
    no_fill()
    stroke_weight(2)
    N = 8
    W = width / N
    for i in range(N):
        x = W / 2 + W * i
        for j in range(N):
            y = W / 2 + W * j
            stroke(i * 20, j * 20, 128)
            espiral(x, y, W, 3 + i, 3 + j)
        

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