"""
sketch 54 180223 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
from collections import namedtuple
import random as rnd

SPACING, MARGIN = 120, 120
X_LIST, Y_LIST = [], []  # listas de posições para elementos
NUM_NODES = 12  # número de elementos do desenho / number of nodes
Node = namedtuple(
    'Node', ['x', 'y', 't_size', 's_weight', 'is_arrow', 'points_to'])
DESENHO = []  # lista dos elementos, 'nodes', do desenho

def setup():
    size(600, 600)
    rectMode(CENTER)
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
        rnd.choice([True, False]),  # is_arrow? (se é seta ou 'linha')
        []  # points_to... (lista com ref. a outro elem.))
    )

def novo_desenho():
    """
    esvazia a lista elementos (setas e linhas) do desenho anterior
    clears the list of nodes and creates a a new drawing appending DESENHO,
    a list of nodes/drawing elements: arrows, connecting lines and lonely nodes
    """
    DESENHO[:] = []
    for _ in range(NUM_NODES):
        DESENHO.append(new_node())
    for node in DESENHO:  # para cada elemento do desenho
        random_node = rnd.choice(DESENHO)  # sorteia outro elemento
        if (node.x, node.y) != (random_node.x, random_node.y):
            # 'aponta' para este elemento, acrescenta na sub_lista
            node.points_to.append(random_node)
  
    # the previous process might generate non-point nodes / podem haver nós
    # que não apontam
    lonely_nodes = [n for n in DESENHO if not n.points_to]
    # check if there at least one non-pointing node
    if not lonely_nodes:
        # I want at least one (non-pointing nodes will be red)
        DESENHO.append(new_node())

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
        line(0, L - offset, -head / 3, L - offset - head)
        line(0, L - offset, head / 3, L - offset - head)
        strokeCap(SQUARE)
        line(0, offset, 0, L - offset)
        if tail_func and tail_size:
            tail_func(0, 0, tail_size, tail_size)
 
def draw():
    background(200)
    # draws white 'lines', non-arrows, first.
    for node in (n for n in DESENHO if not n.is_arrow):
        for other in node.points_to:  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(255)
            line(node.x, node.y, other.x, other.y)
            # desenha o círculo (repare que só em nós que 'apontam')
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws 'lonely nodes' in red (nodes that do not point anywhere)
    for node in (n for n in DESENHO if not n.points_to):
        strokeWeight(node.s_weight)
        stroke(255, 0, 0)  # red stroke for lonely nodes
        if node.is_arrow:
            rect(node.x, node.y, node.t_size, node.t_size)
        else:    
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws black arrows
    for node in (n for n in DESENHO if n.is_arrow):
        for other in node.points_to:  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(0)
            seta(node.x, node.y, other.x, other.y,
                 node.t_size, node.s_weight * 5,
                 rect, node.t_size)

def keyPressed():
    if key == 's':
        saveFrame("####.png")
    if key == 'n':
        novo_desenho()
