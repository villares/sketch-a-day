"""
sketch 58 180226 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

from collections import namedtuple
import random as rnd
import copy as cp
X_LIST = set()

SPACING, MARGIN = 120, 120
X_LIST, Y_LIST = [], []  # listas de posições para elementos
# lista dos elementos, 'nodes', do desenho
DESENHO, OTHER_DESENHO, INTER = [], [], []
NUM_NODES = 8  # número de elementos do desenho / number of nodes
Node = namedtuple(
    'Node', 'x y t_size s_weight is_arrow points_to')

def setup():
    size(600, 600)
    rectMode(CENTER)
    noFill()
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    novo_desenho(DESENHO)

    println("'s' to save, and 'n' for a new drawing")

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'r':
        make_nodes_point(DESENHO)
    if key == 'n':
        novo_desenho(DESENHO)

def novo_desenho(desenho):
    """
    esvazia a lista elementos (setas e linhas) do desenho anterior
    clears the list of nodes and creates a a new drawing appending DESENHO,
    a list of nodes/drawing elements: arrows, connecting lines and lonely nodes
    """
    desenho[:] = []
    for _ in range(NUM_NODES):
        desenho.append(new_node())
    make_nodes_point(desenho)
    OTHER_DESENHO[:] = cp.deepcopy(desenho)
    make_nodes_point(OTHER_DESENHO)


def new_node():
    return Node(                   # elemento/"nó" uma namedtuple com:
        rnd.choice(X_LIST),        # x
        rnd.choice(Y_LIST),        # y
        rnd.choice([10, 20, 30]),  # t_size (tail/circle size)
        rnd.choice([2, 4, 6]),     # s_weight (espessura da linha)
        rnd.choice([True, False]),  # is_arrow? (se é seta ou 'linha')
        []  # points_to... (lista com ref. a outro elem.))
    )

def make_nodes_point(desenho):
    for node in desenho:  # para cada elemento do desenho
        node.points_to[:] = []
        random_node = rnd.choice(desenho)  # sorteia outro elemento
        if (node.x, node.y) != (random_node.x, random_node.y):
            # 'aponta' para este elemento, acrescenta na sub_lista
            node.points_to.append(random_node)

def draw():
    global DESENHO, OTHER_DESENHO
    background(200)
    fc = frameCount % 1100 - 100
    if fc < 0:
        desenho = DESENHO
    elif 0 <= fc < 999:
        make_inter_nodes(map(fc, 0, 1000, 0, 1))
        desenho = INTER
    elif fc == 999:
        DESENHO, OTHER_DESENHO = OTHER_DESENHO, DESENHO
        desenho = DESENHO
        make_nodes_point(OTHER_DESENHO)
    
    # draws white 'lines', non-arrows, first.
    for node in (n for n in desenho if not n.is_arrow):
        for other in node.points_to:  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(255)
            line(node.x, node.y, other.x, other.y)
            # desenha o círculo (repare que só em nós que 'apontam')
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws 'lonely nodes' in red (nodes that do not point anywhere)
    for node in (n for n in desenho if not n.points_to):
        strokeWeight(node.s_weight)
        stroke(255, 0, 0)  # red stroke for lonely nodes
        if node.is_arrow:
            rect(node.x, node.y, node.t_size, node.t_size)
        else:
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws black arrows
    for node in (n for n in desenho if n.is_arrow):
        for other in node.points_to:  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(0)
            seta(node.x, node.y, other.x, other.y,
                 node.t_size, node.s_weight * 5,
                 rect, node.t_size)

def seta(x1, y1, x2, y2, shorter=0, head=None,
         tail_func=None, tail_size=None):
    """
    O código para fazer as setas, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    """
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 10, 10)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        strokeCap(ROUND)
        if L > head*2:
            line(0, L - offset, -head / 3, L - offset - head)
            line(0, L - offset, head / 3, L - offset - head)
            strokeCap(SQUARE)
            line(0, offset, 0, L - offset)
        if tail_func and tail_size:
            tail_func(0, 0, tail_size, tail_size)


def make_inter_nodes(amt):
    INTER[:] = []
    for n1, n2 in zip(DESENHO, OTHER_DESENHO):
        if n1.points_to:
            p1x, p1y = n1.points_to[0].x, n1.points_to[0].y
        else:
            p1x, p1y = n1.x, n1.y
        if n2.points_to:
            p2x, p2y = n2.points_to[0].x, n2.points_to[0].y
        else:
            p2x, p2y = n2.x, n2.y
        INTER.append(Node(                   # elemento/"nó" uma namedtuple com:
            n1.x,        # x
            n1.y,        # y
            n1.t_size,  # t_size (tail/circle size)
            n1.s_weight,     # s_weight (espessura da linha)
            n1.is_arrow,  # is_arrow? (se é seta ou 'linha')
            # cp.deepcopy(n1.points_to)
            [PVector(lerp(p1x, p2x, amt), lerp(p1y, p2y, amt))]
        ))