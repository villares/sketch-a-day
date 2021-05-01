def setup():
    size(800, 400)
    background(240)
    r(0, 0, 400, 10)
    saveFrame("sketch_2021_04_30a_exemplo_recursividade.png")

def r(x, y, s, level):
    fill(level * 24, 100)
    rect(x, y, s, s)
    if level > 1:
        r(x, y + height / 8, s / 2 + random(-20, 20), level - 1)
        r(x + s, y, s / 2, level - 1)
    # o caso base aqui é quando nível (`level') chega a 1 (level > 1 se torna falso)
    # e então apenas um retângulo é desenhado
