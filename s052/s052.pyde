"""
sketch 52 180221 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
from collections import namedtuple
import random as rnd

CEL_SIZE = 128
HALF_CEL = CEL_SIZE / 2
MARGIN = 100
GRADE_PONTOS = []  # lista de tuplas (x, y) / list of tuples
NUM_NODES = 20  # número de elementos do desenho / number of nodes
Node = namedtuple(
    'Node', ['x', 'y', 't_size', 's_weight', 'is_arrow', 'points_to'])
DESENHO = []  # lista de tuplas dos elementos, 'nodes', do desenho

def setup():
    size(712, 712)
    noFill()
    # calcula uma região do canvas dentro das margens / canvas - margin
    h, w = height - 2 * MARGIN, width - 2 * MARGIN
    # calcula número de filas e colunas de 'células' de uma grade
    n_rows, n_cols = int(h / CEL_SIZE), int(w / CEL_SIZE)
    # popula lista com grade de pontos dos centros das 'células'
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
    # esvazia a lista elementos (setas e linhas) do desenho anterior
    # clears the list of nodes (drawing elements: arrows & lines)
    DESENHO[:] = []
    # create a a new drawing (DESENHO, a list of drawing elements)
    for _ in range(NUM_NODES):
        # sorteia um ponto da grade (unpacks x, y from a random point from the grid-list)
        x, y = rnd.choice(GRADE_PONTOS)
        DESENHO.append((Node(  # acrescenta elemento/"nó" uma namedtuple com:
            x,  # x
            y,  # y
            rnd.choice([10, 20, 30]),  # t_size (tail/circle size)
            rnd.choice([2, 4, 6]),     # s_weight (espessura da linha)
            rnd.choice([True, False]),  # is_arrow? (se é seta ou 'linha')
            list()  # points_to... (lista com ref. a outro elem.))
        )))
    for node in DESENHO:  # para cada elemento do desenho
        random_node = rnd.choice(DESENHO)  # sorteia outro elemento
        # compara coordenadas, se não for no mesmo ponto
        if (node.x, node.y) != (random_node.x, random_node.y):
            # 'aponta' para este elemento, acrescenta na sub_lista
            node.points_to.append(random_node)
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
    # draws white 'lines', non-arrows, first.
    for node in (n for n in DESENHO if n.is_arrow == False):
        strokeWeight(node.s_weight)
        stroke(255)
        ellipse(node.x, node.y, node.t_size, node.t_size)  # desenha o círculo
        for other in node.points_to:  # se estiver apontando para alguém
            line(node.x, node.y, other.x, other.y)

    # then draws black arrows
    for node in filter(lambda n: n.is_arrow == True, DESENHO):
        strokeWeight(node.s_weight)
        stroke(0)
        ellipse(node.x, node.y, node.t_size, node.t_size)  # desenha o círculo
        for other in node.points_to:  # se estiver apontando para alguém
            seta(node.x, node.y, other.x, other.y,
                 node.t_size, node.s_weight * 5)


def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'n':
        novo_desenho()
