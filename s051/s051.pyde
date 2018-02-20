"""
sketch 51 180220 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
import random as rnd


CEL_SIZE = 64
HALF_CEL = CEL_SIZE / 2
MARGIN = 100
GRADE_PONTOS = [] # lista de tuplas (x, y)
DESENHO = []  # lista de elementos 


def setup():
    size(712, 712)
    h, w = height - 2 * MARGIN, width - 2 * MARGIN
    noFill()
    n_rows, n_cols = int(h / CEL_SIZE), int(w / CEL_SIZE)
    for r in range(n_rows):
        for c in range(n_cols):
            x, y = HALF_CEL + c * CEL_SIZE,\
                HALF_CEL + r * CEL_SIZE
            GRADE_PONTOS.append((x + MARGIN, y + MARGIN))  # acrescenta ponto

    novo_desenho()
    println("'s' to save, and 'n' for a new drawing")


def novo_desenho():
    DESENHO[:] = []  # esvazia a lista de setas e linhas
    for _ in range(30):
        x, y = rnd.choice(GRADE_PONTOS)
        DESENHO.append((
            x,  # x
            y,  # y
            rnd.choice([10, 20, 30]),  # size
            rnd.choice([2, 4, 6]),  # strokeWeight
            rnd.choice([True, False]),  # arrow (se é seta)
            list()  # other nodes (para onde aponta)
        ))
    for node in DESENHO: # para cada elemento do desenho
        rnd_node = rnd.choice(DESENHO) # sorteia outro elemento
        x1, y1, x2, y2 = node[0], node[1], rnd_node[0], rnd_node[1]
        if (x1, y1) != (x2, y2):  # se não for no mesmo ponto
            node[-1].append(rnd_node) # "aponta" para este elemento
            # pode acontecer de um elemento não apontar para ninguém

def seta(x1, y1, x2, y2, shorter=12, head=12):
    """
    O código para fazer as setas, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    """
    L = dist(x1, y1, x2, y2)
    with pushMatrix():
        translate(x2, y2)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = -shorter * .6
        line(0, offset, 0, -L - offset)
        line(0, offset, -head / 3, -head + offset)
        line(0, offset, head / 3, -head + offset)

def draw():
    background(200)
    # para cada elemento do desenho, pegue as coordenandas e atributos
    for x1, y1, d1, sw, arrow, points_to in DESENHO:
        strokeWeight(sw)
        for other in points_to:
            x2, y2 = other[0], other[1]
            if arrow:   # se for arrow == True, desenhe seta preta
                stroke(0)
                # x1, y1, x2, y2, circle offset, arrow head size
                seta(x1, y1, x2, y2, d1, sw * 5)
            else:   # senhão desenhe linha branca e círculo branco
                stroke(255)
                line(x1, y1, x2, y2)
        ellipse(x1, y1, d1, d1)

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'n':
        novo_desenho()
