

def setup():
    size(1000, 1000)

    # # center
    # rectMode(CENTER)
    # cols = rows = 4
    # w = 150
    # for i in range(cols):
    #     x = w / 2 + i * w
    #     for j in range(rows):
    #         y = w / 2 + j * w
    #         square(x, y, w)
    
    
    # # corner
    # largura_total = 600
    # colunas = filas = 4
    # largura_celula = largura_total / colunas
    # for i in range(colunas):
    #     x = i * largura_celula
    #     for j in range(filas):
    #         y = j * largura_celula
    #         square(x, y, largura_celula)
    
        
# def draw():
#     grade(600, 6)

# def grade(largura_total, celulas):
#     largura_total = 600
#     colunas = filas = celulas
#     largura_celula = largura_total / colunas
#     for i in range(colunas):
#         x = i * largura_celula
#         for j in range(filas):
#             y = j * largura_celula
#             square(x, y, largura_celula)
    
def draw():
    strokeWeight(0.1)
    grade(0, 0, width, 5)
    noLoop()
    saveFrame("a.png")
    
def grade(xo, yo, largura_total, celulas):
    colunas = filas = celulas
    largura_celula = float(largura_total) / colunas
    for i in range(colunas):
        x = xo + i * largura_celula
        for j in range(filas):
            y = yo + j * largura_celula
            if largura_total > 25 and i % 2:
                grade(x, y, largura_celula, 5)
            else:
                fill(0, i * 64, j * 64)
                square(x, y, largura_celula)
    
