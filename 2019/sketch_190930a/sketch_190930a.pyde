from elementos import olho, casinha, grade, estrela

def setup():
    size(500, 500)
    desenho()
    saveFrame("capa_desenho_sem_argumentos.png")
    
def desenho():
    # width é a largura da área de desenho
    metade, quarto = width / 2, width / 4
    noStroke() # desliga o traço
    fill(100) # preenchimento cinza escuro
    rect(0, metade, metade, metade) # fundo para grade
    fill(0) # preenchimento preto
    rect(metade, 0, metade, metade) # fundo preto para o olho
    olho(metade + quarto, quarto, 200)
    fill(255) # preenchimento branco
    stroke(0) # traço preto
    strokeWeight(10) # espessura do traço
    casinha(quarto, quarto, 200)
    grade(quarto, metade + quarto, 4, 220)
    estrela(metade + quarto, metade + quarto, 7, 100, 50)
    
