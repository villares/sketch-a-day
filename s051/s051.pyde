"""
sketch 51 180220 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
import random as rnd

CEL_SIZE = 64
HALF_CEL = CEL_SIZE / 2
MARGIN = 100
GRADE_PONTOS = []  # lista de tuplas (x, y) / list of tuples
NUM_NODES = 30  # número de elementos do desenho / number of nodes
DESENHO = []  # lista de tuplas dos elementos/'nós' do desenho
              # (x, y, diâmetro, espessura, se é seta, pra quem aponta)

def setup():
    size(712, 712)
    noFill()
    # calcula uma região do canvas dentro das margens / canvas - margin
    h, w = height - 2 * MARGIN, width - 2 * MARGIN
    # calcula número de filas e colunas de 'células' de uma grade
    n_rows, n_cols = int(h / CEL_SIZE), int(w / CEL_SIZE)
    # populalista com grade de pontos dos centros das 'células'
    # populates a list of points in a grid according to CEL_SIZE
    for r in range(n_rows):
        for c in range(n_cols):
            x, y = HALF_CEL + c * CEL_SIZE,\
                HALF_CEL + r * CEL_SIZE
            GRADE_PONTOS.append((x + MARGIN, y + MARGIN))  # acrescenta ponto
    # chama o procedimento que gera um desenho
    novo_desenho()
    println("'s' to save, and 'n' for a new drawing")

def novo_desenho():
    # esvazia a lista elementos (setas e linhas) de desenho anterior
    # clears the list of nodes (drawing elements: arrows & lines)
    DESENHO[:] = []
    for _ in range(NUM_NODES):
        # sorteia um ponto da grade (unpack x, y)
        x, y = rnd.choice(GRADE_PONTOS)
        DESENHO.append((  # acrescenta elemento/"nó" uma tupla com:
            x,  # x
            y,  # y
            # circle size (sorteia um tamanho de círculo)
            rnd.choice([10, 20, 30]),
            rnd.choice([2, 4, 6]),  # strokeWeight (espessura da linha)
            rnd.choice([True, False]),  # arrow (se é seta)
            # other nodes (nesta lista pode ser posta ref. a outro elem.))
            list()
        ))
    for node in DESENHO:  # para cada elemento do desenho
        rnd_node = rnd.choice(DESENHO)  # sorteia outro elemento
        x1, y1, x2, y2 = node[0], node[1], rnd_node[0], rnd_node[1]
        # compara coordenadas, se não for no mesmo ponto
        if (x1, y1) != (x2, y2):
            # 'aponta' para este elemento, acrescenta na sub_lista
            node[-1].append(rnd_node)
            # pode acontecer de um elemento não apontar para ninguém
            # caso ele mesmo tenha sido sorteado, ou um outro na mesma posição

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
        for other in points_to:  # se estiver apontando para alguém
            # pega as coordenadas do outro elemento
            x2, y2 = other[0], other[1]
            if arrow:   # se for arrow == True, desenhe seta preta apontando
                stroke(0)
                # x1, y1, x2, y2, circle offset, arrow head size
                seta(x1, y1, x2, y2, d1, sw * 5)
            else:   # senão desenhe linha branca até ele
                stroke(255)
                line(x1, y1, x2, y2)
        ellipse(x1, y1, d1, d1)  # desenha o círculo

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'n':
        novo_desenho()
