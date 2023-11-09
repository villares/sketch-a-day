from pathlib import Path
from random import sample

from itertools import product

pastas = {} # dicionário de pastas {1: [imagen0, imagem2]}

offset = 0

def setup():
    size(1000, 1000)
    for numero in range(1, 4): # 1, 2, 3        
        pasta = Path(str(numero))
        pastas[numero] = []  # lista vazia para receber imagens
        for arquivo in pasta.iterdir():
            pastas[numero].append(load_image(arquivo))
    no_loop()  # pausei o draw()

def draw():
    background(200)
    p = list(product(pastas[1], pastas[2], pastas[3]))
    y = x = 0
    #amostra = sample(p, 100)
    amostra = p[offset:offset+100]  # fatia de 100
    for ia, ib, ic in amostra:
        no_fill()
        rect(x, y, 100, 100)
        image(ia, x, y, 100, 100)
        image(ib, x, y, 100, 100)
        image(ic, x, y, 100, 100)
        x = x + 100
        if x >= width:
            x = 0
            y = y + 100
        if y > height:
            break # interrompe o for

    
def key_pressed():
    global offset
    save_frame(f'{offset}.png')
    offset = offset + 100
    redraw() # desenha mais um draw
    
    