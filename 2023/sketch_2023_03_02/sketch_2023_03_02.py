from random import shuffle

tam = 75
posicoes = []  # lista vazia


def setup():
    size(750, 375)
    text_align(CENTER, CENTER)
    color_mode(HSB)  # matiz, saturacao, brilho
    for y in range(0, height, tam):
        for x in range(0, width, tam): 
            posicoes.append((x, y))  # tupla (x, y)


def draw():
            
    for i, pos in enumerate(posicoes):
        x, y = pos 
        fill(i * 5, 200, 200)
        rect(x, y, tam, tam)
        fill(0)
        text(i,
            x + tam / 2,
            y + tam / 2)
        
def key_pressed():
    shuffle(posicoes)
