"""
Tecle 'e' para salvar um único frame e encerrar o sketch
"""

add_library('pdf')

save_frame = False
fator_escala = 2.835 # 297px -> ~297mm

def setup():
    global pdf_output
    size(297, 420)
    pdf_output = createGraphics(int(width * fator_escala),
                                int(height * fator_escala),
                                PDF, "arquivo.pdf")
def draw():
    
    if save_frame:
        beginRecord(pdf_output)
        pdf_output.scale(fator_escala)
        pdf_output.strokeWeight(0.1)

    background(200)        
    largura_carta = 80
    altura_carta = 120
    e = 15
    d = 3  # espaço das marcas de corte
    for x in range(e, width, e + largura_carta):
        for y in range(e, height, e + altura_carta):
            push() 
            noStroke()   
            rect(x - d, y - d, largura_carta + d * 2, altura_carta + d * 2) # outer bleed
            stroke(200)
            noFill()
            # rect(x, y, largura_carta, altura_carta) # will cut here
            rect(x + d, y + d, largura_carta - d * 2, altura_carta - d * 2) # inner margin
            pop()
            marcas(x, y, largura_carta, altura_carta, d)
    # rect(15, 2 * 15 + 120, 80, 120)
    # rect(15, 3 * 15 + 120 * 2, 80, 120)

    if save_frame:
        endRecord()  # encerra a gravação do arquivo
        exit()  # encerra o sketch

def marcas(x, y, w, h, d=3):
    line(x - d, y, x - d * 2, y)
    line(x - d, y + h, x - d * 2, y + h)
    line(x  + w + d, y, x + w + d * 2, y)
    line(x  + w + d, y + h, x + w + d * 2, y + h)
    line(x, y - d, x, y - d * 2)
    line(x + w, y - d, x + w, y - d * 2)
    line(x, y + h + d, x, y + h + d * 2)
    line(x + w, y + h + d, x + w, y + h + d * 2)


def keyPressed():
    global save_frame
    if key == 'e':
        save_frame = True
