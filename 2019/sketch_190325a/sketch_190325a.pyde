# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190325a", ".gif"

"""
A retake of sketch 58 180228 + work from sketch_190321 :)
"""
from collections import namedtuple
import random as rnd
import copy as cp

add_library('GifAnimation')
from gif_exporter import gif_export

SPACING, MARGIN = 120, 120
X_LIST, Y_LIST = [], []  # listas de posições para elementos
desenho_atual, outro_desenho, desenho_inter, desenho_inicial = [], [], [], []
# NUM_NODES = 32  # número de elementos do desenho / number of nodes
Node = namedtuple(
    'Node', 'x y t_size s_weight is_special points_to')
save_frames = False

def setup():
    smooth(16)
    size(600, 600, P2D)
    rectMode(CENTER)
    noFill()
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    novo_desenho(desenho_atual)
    desenho_inicial[:] = cp.deepcopy(desenho_atual)
    println("'s' to save, and 'n' for a new drawing")

def keyPressed():
    global save_frames
    if key == 's':
        saveFrame("####.png")
        #save_frames = not save_frames
        print "Saving " + repr(save_frames)
    if key == 'r':
        make_nodes_point(desenho_atual)
    if key == 'n':
        novo_desenho(desenho_atual)
    if key == ' ':
        background(200)

def novo_desenho(desenho):
    """
    esvazia a lista elementos (setas e linhas) do desenho anterior
    clears the list of nodes and creates a a new drawing appending desenho_atual,
    a list of nodes/drawing elements: specials, connecting lines and lonely nodes
    """
    desenho[:] = []
    for x in X_LIST:
        for y in Y_LIST:
            desenho.append(new_node(x, y))
    make_nodes_point(desenho)
    outro_desenho[:] = cp.deepcopy(desenho)
    make_nodes_point(outro_desenho)


def new_node(x=None, y=None):
    if x == None or y == None:
        x = rnd.choice(X_LIST)
        y = rnd.choice(Y_LIST)
    return Node(                   # elemento/"nó" uma namedtuple com:
        x,        # x
        y,        # y
        rnd.choice([10, 20, 30]),  # t_size (tail/circle size)
        rnd.choice([1, 2, 3]),     # s_weight (espessura da linha)
        rnd.choice([True, False]),  # is_special? (se é wave ou 'linha')
        []  # points_to... (lista com ref. a outro elem.))
    )

def make_nodes_point(desenho):
    for node in desenho:  # para cada elemento do desenho
        node.points_to[:] = []
        random_node = rnd.choice(desenho)  # sorteia o,utro elemento
        while not ((node.x, node.y) != (random_node.x, random_node.y)
                   and dist(node.x, node.y,
                            random_node.x, random_node.y) <= SPACING * 2):
            random_node = rnd.choice(desenho)
        # 'aponta' para este elemento, acrescenta na sub_lista
        node.points_to.append(random_node)

def draw():
    global desenho_atual, outro_desenho
    background(200)
    fc = frameCount % 300 - 150
    if fc < 0:
        desenho = desenho_atual
    elif 0 <= fc < 149:
        if frameCount % 10 == 0:
            make_inter_nodes(map(fc, 0, 150, 0, 1))
        desenho = desenho_inter
    elif fc == 149:
        desenho_atual, outro_desenho = outro_desenho, desenho_atual
        desenho = desenho_atual
        if not mousePressed:
            make_nodes_point(outro_desenho)
            print("will reset")
        else:
            outro_desenho[:] = cp.deepcopy(desenho_inicial)

    # draws white 'lines', non-specials, first.
    for node in (n for n in desenho if not n.is_special):
        for other in node.points_to:  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(255)
            line(node.x, node.y, other.x, other.y)
            # desenha o círculo (repare que só em nós que 'apontam')
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws 'lonely nodes' in red (nodes that do not point anywhere)
    for node in (n for n in desenho if not n.points_to):
        strokeWeight(node.s_weight)
        stroke(100)  # grey stroke for lonely nodes
        if node.is_special:
            ellipse(node.x, node.y, node.t_size * 2, node.t_size * 2)
        else:
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws black specials
    for node in (n for n in desenho if n.is_special):
        for other in node.points_to:  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(0)
            wave(node.x, node.y, other.x, other.y,
                 node.t_size, node.s_weight * 5)
            ellipse(node.x, node.y, node.t_size / 2, node.t_size / 2)
            ellipse(other.x, other.y, node.s_weight, node.s_weight)

    # if frameCount % 4 == 0:
    #     gif_export(GifMaker)


def make_inter_nodes(amt):
    desenho_inter[:] = []
    for n1, n2 in zip(desenho_atual, outro_desenho):
        if n1.points_to:
            p1x, p1y = n1.points_to[0].x, n1.points_to[0].y
        else:
            p1x, p1y = n1.x, n1.y
        if n2.points_to:
            p2x, p2y = n2.points_to[0].x, n2.points_to[0].y
        else:
            p2x, p2y = n2.x, n2.y
        desenho_inter.append(Node(                   # elemento/"nó" uma namedtuple com:
            n1.x,        # x
            n1.y,        # y
            n1.t_size,  # t_size (tail/circle size)
            n1.s_weight,     # s_weight (espessura da linha)
            n1.is_special,  # is_special? (se é barra ou 'linha')
            # cp.deepcopy(n1.points_to)
            [PVector(lerp(p1x, p2x, amt), lerp(p1y, p2y, amt))]
        ))


def wave(x1, y1, x2, y2, s=None, n=2):
    from arcs import roundedCorner
    """
    dois pares (x, y), largura, número de ondas
    """
    L = dist(x1, y1, x2, y2)
    if not s:
        s = int(max(L / 5, 10))
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = 0
        dy = L / (n + 2.)
        line(0, 0, 0, dy / 2.)
        point_L = []
        point_L.append(PVector(0, 0))
        for i in range(1, n + 1):
            point_L.append(PVector(0, i * dy))
            if i % 2:
                point_L.append(PVector(-s, i * dy + dy / 2.))
                point_L.append(PVector(0, i * dy + dy))
            else:
                point_L.append(PVector(s, i * dy + dy / 2.))
                point_L.append(PVector(0, i * dy + dy))
        point_L.append(PVector(0, L))
        for p0, p1, p2 in zip(point_L[:-2],
                              point_L[1:-1],
                              point_L[2:]
                              ):
            roundedCorner(p1, (p0 + p1) / 2., (p2 + p1) / 2., 10)
        line(0, L - dy / 2., 0, L)
        stroke(0)

def zigzag(x1, y1, x2, y2, s=None, n=2):
    """
    dois pares (x, y), largura, número de ondas
    """
    L = dist(x1, y1, x2, y2)
    if not s:
        s = int(max(L / 5, 10))
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = 0
        dy = L / (n + 2)
        beginShape()
        stroke(0)
        vertex(0, 0)
        for i in range(1, n + 1):
            vertex(0, i * dy)
            if i % 2:
                stroke(255, 0, 0)
                vertex(-s, i * dy + dy / 2.)
            else:
                stroke(0, 0, 255)
                vertex(s, i * dy + dy / 2.)
        stroke(0)
        vertex(0, L - dy)
        vertex(0, L)
        endShape()

# print text to add to the project's README.md
def settings():
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
