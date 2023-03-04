from random import shuffle

tam = 150
posicoes = list(range(1, 26))

def setup():
    size(750, 750)
    text_align(CENTER, CENTER)
    text_size(40)
    color_mode(HSB)  # matiz, saturacao, brilho
    

def draw():
    x = y = 0            
    for i in posicoes: 
        fill(i * 10, 200, 200)
        rect(x, y, tam, tam)
        fill(0)
        text(i, x + tam / 2, y + tam / 2)
        x += tam
        if x >= width:
            x = 0
            y += tam
 
def boas_posicoes(posicoes):
    if sum(posicoes[:5]) != 65: return False
    print('1', end='')
    if sum(posicoes[::5]) != 65: return False
    return True
 
def key_pressed():
    shuffle(posicoes)
    while not boas_posicoes(posicoes):
        print('.', end='')
        shuffle(posicoes)
    print('done')
