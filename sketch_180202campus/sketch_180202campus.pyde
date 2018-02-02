"""
s180202c - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Exemplo mínimo de animação com variáveis globais
"""

TAMANHO = 20  # variáveis criadas fora do setup e draw são globais
POS = 0 # posição inicial do círculo

def setup():
    size(500, 500)
    noFill()          # para desenhar sem preenchimento
    strokeWeight(3)   # epessura da linha
    stroke(255, 0, 0) # traço vermelho
    background(0)

def draw():
    global TAMANHO
    global POS    # se você pretende atualizar o valor de uma global precis avisar
    #background(0) # limpa a tela (experimente desativar)
    ellipse(POS, 250, TAMANHO, TAMANHO) # círculo de diâmetro TAMANHO, x=POS e y=250
    POS = POS + 10  # Atualiza a posição
    TAMANHO = TAMANHO + 11 # Para usar isto precisa declarar 'global TAMANHO'