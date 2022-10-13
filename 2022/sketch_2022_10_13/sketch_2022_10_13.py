def setup():
    size(800, 800)
    background(200)
    no_fill()
    poligono_recursivo(400, 400, 200)

def poligono_recursivo(xo, yo, tamanho, n=6):
    pontos = pontos_poligono(xo, yo, tamanho, n)
    stroke_weight(tamanho / 12)
    desenha_poligono_fechado(pontos)
    if tamanho > 10:
        for x, y in pontos:
            poligono_recursivo(x, y, tamanho * 0.48, n)

def pontos_poligono(xo, yo, raio, n):
    a = TWO_PI / n
    return [(xo + cos(i * a) * raio, yo + sin(i * a) * raio)
             for i in range(n)]

def desenha_poligono_fechado(pontos):
    with begin_closed_shape():
        vertices(pontos)

