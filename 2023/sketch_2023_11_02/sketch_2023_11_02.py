from shapely import Polygon, Point
celulas = {}  # {key (col, fil): value objeto Celula}
pontos = {} # {(i, j): (x, y)

def setup():
    global n, w
    size(600, 600)
    text_font(create_font('Inconsolata Bold', 18))
    text_align(CENTER, CENTER)
    color_mode(HSB)
    n = 5 # numero de linhas e colunas da grade de pontos
    w = width / n
    # construit pontos
    calcular_pontos()
    # construir celulas
    k = 0
    for i in range(n - 1):
        for j in range(n - 1):
            cps = (# cell points
                (i, j),
                (i + 1, j),
                (i + 1, j + 1),
                (i, j + 1),    
                )
            celulas[i, j] = (Polygon(pontos[pi, pj] for pi, pj in cps), k)
            k += 1
    no_loop()
            
def draw():
    background(0)
    n = 50
    w = width / n
    for i in range(n): # i 0, 1, 2 .. 4
        for j in range(n):
            x = w / 2 + i * w
            y = w / 2 + j * w
#             x = x + random(-w/8, w/8)
#             y = y + random(-w/8, w/8)
            c = -1
            for p, k in celulas.values():
                if p.contains(Point(x, y)):
                    c = k + 1
                    #print(c)
                    break
            c = 255 if c == -1 else color((c * 16) % 255, 240, 240)
            fill(c)
            text(str(random_choice((0, 1))), x, y)

#     for i, j in celulas:
#         cps, dados = celulas[(i, j)]
#         begin_shape()
#         for pi, pj in cps:
#             #print(pontos[pi, pj])
#             fill(dados[0], 50)
#             x, y = pontos[pi, pj]
#             vertex(x, y)
#         end_shape(CLOSE)
    
def key_pressed():
    save(__file__[:-2] + 'png')
    redraw()
    #calcular_pontos()
    
def calcular_pontos():
    for i in range(n): # i 0, 1, 2 .. 4
        for j in range(n):
            x = w / 2 + i * w
            y = w / 2 + j * w
            x = x + random(-w/4, w/4)
            y = y + random(-w/4, w/4)
            pontos[(i, j)] = x, y
    
        
