from functools import cache

from shapely import Polygon, Point

celulas = {}  # {key (col, fil): value objeto Celula}
pontos = {} # {(i, j): (x, y)

def setup():
    global n, w
    size(600, 600, P3D)
    text_font(create_font('Inconsolata Bold', 60))
    text_size(18)
    text_align(CENTER, CENTER)
    #text_mode(MODEL)
    color_mode(HSB)
    
    n = 5 # numero de linhas e colunas da grade de pontos
    w = width / n
    # construir pontos
    calcular_pontos()
    # construir celulas
    calcular_celulas()
            
def draw():
    background(0)
    translate(0, height / 2, -200)
    rotate_x(PI / 6)
    translate(0, -height / 2, 0)
    n = 50
    w = width / n
    for i in range(n): # i 0, 1, 2 .. 4
        for j in range(n):
            x = w / 2 + i * w
            y = w / 2 + j * w
#             x = x + random(-w/8, w/8)
#             y = y + random(-w/8, w/8)
            region = 0    
            for p, k in celulas.values():
                if p_contains(p, x, y):
                    region = k + 1
                    break
                region = 0    
            c = 255 if region == 0 else color((region * 32) % 255, 240, 240)
            fill(c)
            with push_matrix():
                translate(0, 0, region * 25)
                text(str(region % 10), x, y)

    
def key_pressed():
    save(__file__[:-2] + 'png')
    calcular_pontos()
    calcular_celulas()

@cache
def p_contains(p, x, y):
    return p.contains(Point(x, y))
 
def calcular_pontos():
    for i in range(n): # i 0, 1, 2 .. 4
        for j in range(n):
            x = w / 2 + i * w
            y = w / 2 + j * w
            x = x + random(-w/4, w/4)
            y = y + random(-w/4, w/4)
            pontos[(i, j)] = x, y

def calcular_celulas():
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
        
