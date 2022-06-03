save_pdf = False
largura_carta = 240
altura_carta = 160
colunas = 3
filas = 3
e = 30  # espaçamento

def setup():
    size(420 * 2, 297 * 2)
    begin_record(PDF, "arquivo.pdf")
    background(200)
    for i in range(colunas): 
        x = e + (largura_carta + e) * i
        for j in range(filas): 
            y = e + (altura_carta + e) * j
            no_stroke()
            fill(240)
            bleed = 3
            rect(x - bleed, y - bleed, largura_carta + bleed * 2,
                 altura_carta + bleed * 2)  # outer bleed
#             stroke(200)
#             no_fill()
#             rect(x, y, largura_carta, altura_carta) # mostra onde corta
            circulos(x, y, i, j)
            stroke(0)
            marcas_de_corte(x, y, largura_carta, altura_carta)
    end_record()  # encerra a gravação do arquivo

def circulos(x, y, i, j):
    for k in range(1, 4):
        xc = k * largura_carta / 4
        if k == 1:
            fill(i * 128, 128, 128)
        elif k == 2:
            fill(128, j * 128, 128)                    
        else:
           fill(i * 128, j * 128, 128) 
        circle(x + xc, y + altura_carta / 2, altura_carta / 3)

def marcas_de_corte(x, y, w, h, d=6):
    line(x - d, y, x - d * 2, y)
    line(x - d, y + h, x - d * 2, y + h)
    line(x + w + d, y, x + w + d * 2, y)
    line(x + w + d, y + h, x + w + d * 2, y + h)
    line(x, y - d, x, y - d * 2)
    line(x + w, y - d, x + w, y - d * 2)
    line(x, y + h + d, x, y + h + d * 2)
    line(x + w, y + h + d, x + w, y + h + d * 2)
