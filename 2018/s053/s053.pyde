"""
sketch 53 180222 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
from collections import namedtuple
import random as rnd

SPACING, MARGIN = 206, 150
X_LIST, Y_LIST = [], []  # listas de posições para elementos
NUM_NODES = 10  # número de elementos do desenho / number of nodes
Node = namedtuple(
    'Node', ['x', 'y', 't_size', 's_weight', 'is_arrow', 'points_to'])
DESENHO = []  # lista dos elementos, 'nodes', do desenho

def setup():
    size(712, 712)
    noFill()
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    novo_desenho()
    println("'s' to save, and 'n' for a new drawing")

def new_node():
    return Node(                   # elemento/"nó" uma namedtuple com:
        rnd.choice(X_LIST),        # x
        rnd.choice(Y_LIST),        # y
        rnd.choice([10, 20, 30]),  # t_size (tail/circle size)
        rnd.choice([2, 4, 6]),     # s_weight (espessura da linha)
        rnd.choice([True, False]), # is_arrow? (se é seta ou 'linha')
        []  # points_to... (lista com ref. a outro elem.))
    )

def novo_desenho():
    # esvazia a lista elementos (setas e linhas) do desenho anterior
    # clears the list of nodes (drawing elements: arrows & lines)
    DESENHO[:] = []
    # create a a new drawing (DESENHO, a list of drawing elements)
    for _ in range(NUM_NODES):
        DESENHO.append(new_node())
    for node in DESENHO:  # para cada elemento do desenho
        random_node = rnd.choice(DESENHO)  # sorteia outro elemento
        if (node.x, node.y) != (random_node.x, random_node.y):
            # 'aponta' para este elemento, acrescenta na sub_lista
            node.points_to.append(random_node)
    # previous process might generate non-point_to nodes / podem rolar nós que não 'apontam'
    lonely_nodes = [n for n in DESENHO if not n.points_to]  # points with no points_to
    if not lonely_nodes:            # check if there is at least one non-pointing node
        DESENHO.append(new_node())  # I want at least one (non-pointing nodes will be red)

def seta(x1, y1, x2, y2, shorter=12, head=12):
    """
    O código horrível para fazer as setas, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    breve no sketch #54 em diante uma versão melhor...
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
    for node in (n for n in DESENHO if not n.is_arrow):
        strokeWeight(node.s_weight)
        stroke(255)
        ellipse(node.x, node.y, node.t_size, node.t_size)  # desenha o círculo
        for other in node.points_to:  # se estiver apontando para alguém
            line(node.x, node.y, other.x, other.y)

    # then draws black arrows
    # for node in filter(lambda n: n.is_arrow, DESENHO):
    for node in (n for n in DESENHO if n.is_arrow):
        strokeWeight(node.s_weight)
        stroke(0)
        ellipse(node.x, node.y, node.t_size, node.t_size)  # desenha o círculo
        for other in node.points_to:  # se estiver apontando para alguém
            seta(node.x, node.y, other.x, other.y,
                 node.t_size, node.s_weight * 5)
    # then draws 'lonely nodes' in red (nodes that do not point anywhere)
    for node in (n for n in DESENHO if not n.points_to):
        strokeWeight(node.s_weight)
        stroke(255, 0, 0)
        ellipse(node.x, node.y, node.t_size, node.t_size)  # desenha círculo vermelho

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'n':
        novo_desenho()
