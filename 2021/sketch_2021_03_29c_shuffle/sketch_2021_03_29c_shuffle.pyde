# Biblioteca padrão do Python: random.shuffle()
# Importa do módulo random função shuffle
from random import shuffle 

tam = 75

def setup():
    size(750, 375)
    textAlign(CENTER, CENTER)
    colorMode(HSB)  # matiz, saturacao, brilho
    frameRate(1)

def draw():
    # Monta uma lista ordenada das posições da grade
    posicoes = []  # lista vazia
    for y in range(0, height, tam):
        for x in range(0, width, tam): 
            posicoes.append((x, y))  # tupla (x, y)
    # Embaralha a lista gerada com shuffle()    
    shuffle(posicoes)
    # Desenha na tela os quadrados com o índice da lista
    for i, pos in enumerate(posicoes):
        print(i, pos)
        x, y = pos 
        fill(i * 5, 200, 200) # i muda o matiz
        rect(x, y, tam, tam)
        fill(0)
        text(i,   # escrevendo o númeroa
            x + tam / 2,
            y + tam / 2)
    
