"""
Um tabuleiro que permite acrescentar e remover peças com o clique do mouse
O botão da direita põe uma peça "D" e o da esquerda põe uma peça "E"
- Clicando sobre uma peça ela é removida
"""

tam_tabuleiro = 15
tam_casa = 35
meia_casa = tam_casa / 2
borda = 36
tabuleiro = {}  # cria um dicionário vazio
cores = {'E': color(200, 0, 0), 'D': color(0, 200, 0)}  # cores para as peças

def setup():
    size(600, 600)
    text_align(CENTER, CENTER)

def draw():
    background(200)
    for i in range(tam_tabuleiro):
        for j in range(tam_tabuleiro):
            c = tabuleiro.get((i, j))
            if c:
                fill(cores[c])
            else:
                fill(255)
            square(i * tam_casa + borda,
                   j * tam_casa + borda,
                   tam_casa) 
            if c:
                fill(255)
                text(c,
                     i * tam_casa + borda + meia_casa,
                     j * tam_casa + borda + meia_casa)

def mouse_to_tabuleiro(x, y):
    i = (x - borda) // tam_casa
    j = (y - borda) // tam_casa
    return i, j
    
def mouse_pressed():
    if (borda < mouse_x < width - borda and
        borda < mouse_y < height - borda):
        i, j = mouse_to_tabuleiro(mouse_x, mouse_y)

        if (i, j) in tabuleiro:
            del tabuleiro[i, j]
        else:
            tabuleiro[i, j] = 'E' if mouse_button == LEFT else 'D'
#       # Outra versão para remover e acrescentar peças
#       # remove peça se houver
#       if not tabuleiro.pop((i, j), None):  
#       # se não houver inclui peça
#           tabuleiro[i, j] = 'E' if mouse_button == LEFT else 'D'
