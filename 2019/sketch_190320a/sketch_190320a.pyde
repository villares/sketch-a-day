# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190320a", ".gi"

"""
based on sketch 57 180226 
"""
from collections import namedtuple
import random as rnd

add_library('GifAnimation')
from gif_exporter import gif_export

SPACING, MARGIN = 120, 120
X_LIST, Y_LIST = [], []  # listas de posições para elementos
DESENHO = []  # lista dos elementos, 'nodes', do desenho
NUM_NODES = 8  # número de elementos do desenho / number of nodes
Node = namedtuple(
    'Node', ['x', 'y', 't_size', 's_weight', 'is_arrow', 'points_to'])

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
    if key == 'g':
        gif_export(GifMaker, filename=SKETCH_NAME)

def novo_desenho(desenho):
    """
    esvazia a lista elementos (waves e linhas) do desenho anterior
    clears the list of nodes and creates a a new drawing appending DESENHO,
    a list of nodes/drawing elements: arrows, connecting lines and lonely nodes
    """
    desenho[:] = []
    for _ in range(NUM_NODES):
        desenho.append(new_node())
    make_nodes_point(desenho)

def new_node():
    return Node(                   # elemento/"nó" uma namedtuple com:
        rnd.choice(X_LIST),        # x
        rnd.choice(Y_LIST),        # y
        rnd.choice([10, 20, 30]),  # t_size (tail/circle size)
        rnd.choice([2, 4, 6]),     # s_weight (espessura da linha)
        rnd.choice([True, False]),  # is_arrow? (se é wave ou 'linha')
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
            wave(node.x, node.y, other.x, other.y,
                 node.t_size)

def wave(x1, y1, x2, y2, s=None):
    """
    O código para fazer as waves, dois pares (x, y),
    """
    L = int(dist(x1, y1, x2, y2))
    if not s:
        s = int(max(L / 10, 10))
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = 0
        N = 10
        dy = L / (N-1)
        for i in range(N-2):
            # y = dy/2 + map(i, 0, N-1, 0, L)
            # if i % 2: pass
            #     # line(0, y -dy, -s, y)
            #     # line(0, y +dy, -s, y)
            # else:
            #     line(-s, y -dy, s, y)
            #     line(-s, y +dy, s, y)
            y = map(i, 0, N-1, 0, L)
            if i % 2: 
                line(s, y , -s, y)
                line(s, y + 2*dy, -s, y)
            else:
                line(-s, y , s, y)
                line(-s, y + 2*dy, s, y)
        line(0, 0, 0, L)
        


# print text to add to the project's README.md
def settings():
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
