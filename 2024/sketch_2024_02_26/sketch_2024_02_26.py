from random import choice

import py5

def setup():
    global linhas
    py5.size(500, 500)
    linhas = py5.load_strings('horoscopos.txt')
    py5.no_loop()
    py5.fill(0)
    py5.text_size(40)

def draw():
    py5.background(200)
    sorteio = choice(linhas)
    texto = quebra_frase(sorteio, 480)
    py5.text(texto, 20, 20)

def quebra_frase(frase, largura):
    resultado = ""
    parcial = ""
    for letra in frase:
        parcial += letra
        if py5.text_width(parcial) > largura:
            ultimo_espaco = parcial.rfind(' ')
            resultado += '\n' + parcial[:ultimo_espaco]
            parcial = parcial[ultimo_espaco + 1:]
    resultado += '\n' + parcial
    return resultado  

def key_pressed():
    py5.redraw()

py5.run_sketch()