def setup():
    size(800, 400)
    background(255)
    desenha_retangulos(0, 0, 399, 10)
    saveFrame("sketch_2021_04_30a_exemplo_recursividade.png")

def desenha_retangulos(x, y, tamamho, nivel):
    fill(nivel * 24)
    rect(x, y, tamamho, tamamho)
    if nivel > 1:
        desenha_retangulos(x, y, tamamho / 2, nivel - 1)
        desenha_retangulos(x + tamamho, y, tamamho / 2, nivel - 1)
    # o caso base aqui é quando nível (`nivel') chega a 1 (nivel > 1 se torna falso)
    # e então apenas um retângulo é desenhado
