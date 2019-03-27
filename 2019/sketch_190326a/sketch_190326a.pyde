# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190326a", ".gif"

"""
A retake of sketch_190207a + work from sketch_190321 :)
Will stall sometimes... as there is an unsage while loop
selecting pointing nodes...
"""

add_library('GifAnimation')
from gif_exporter import gif_export
add_library('peasycam')
from collections import namedtuple
import random as rnd
import copy as cp

SPACING, MARGIN = 100, 100
X_LIST, Y_LIST = [], []  # listas de posições para elementos
desenho_atual, outro_desenho, desenho_inter, desenho_inicial = [], [], [], []
NUM_NODES = 32  # número de elementos do desenho / number of nodes
Node = namedtuple(
    'Node', 'x y t_size s_weight is_special points_to')
save_frames = False

def setup():
    smooth(16)
    size(600, 600, P3D)
    colorMode(HSB)
    rectMode(CENTER)
    noFill()
    cam = PeasyCam(this, 500)
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    novo_desenho(desenho_atual)
    desenho_inicial[:] = cp.deepcopy(desenho_atual)

def keyPressed():
    global save_frames
    if key == 's':
        saveFrame("####.png")
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
    for _ in range(NUM_NODES):
        desenho.append(new_node())
    make_nodes_point(desenho)
    outro_desenho[:] = cp.deepcopy(desenho)
    make_nodes_point(outro_desenho)


def new_node():
    return Node(                   # elemento/"nó" uma namedtuple com:
        rnd.choice(X_LIST),        # x
        rnd.choice(Y_LIST),        # y
        rnd.choice([10, 15, 20]),  # t_size (tail/circle size)
        rnd.choice([2, 3, 4]),     # s_weight
        # rnd.choice([True, False]),  # is_special? (se é seta ou 'linha')
        True,
        []  # points_to... (lista com ref. a outro elem.))
    )

def make_nodes_point(desenho):
    for node in desenho:  # para cada elemento do desenho
        node.points_to[:] = []
        random_node = rnd.choice(desenho)  # sorteia o,utro elemento
        while not ((node.x, node.y) != (random_node.x, random_node.y)
                   and dist(node.x, node.y,
                            random_node.x, random_node.y) <= SPACING * 2):
            #print(node)
            random_node = rnd.choice(desenho)
        # 'aponta' para este elemento, acrescenta na sub_lista
        node.points_to.append(random_node)

def draw():
    translate(-width / 2, -height / 2)
    global desenho_atual, outro_desenho
    background(0)
    fc = frameCount % 300 - 50
    if fc < 0:
        desenho = desenho_atual
    elif 0 <= fc < 49:
        if frameCount % 10 == 0:
            make_inter_nodes(map(fc, 0, 150, 0, 1))
        desenho = desenho_inter
    elif fc == 49:
        desenho_atual, outro_desenho = outro_desenho, desenho_atual
        desenho = desenho_atual
        if not mousePressed:
            make_nodes_point(outro_desenho)
            print("will reset")
        else:
            outro_desenho[:] = cp.deepcopy(desenho_inicial)

    # then draws black specials
    for node in (n for n in desenho if n.is_special):
        for other in node.points_to:  # se estiver apontando para alguém
            # strokeWeight(node.s_weight)
            with pushMatrix():
                for i in range(-4, 11, 2):
                    stroke(48 + i * 8, 200, 200)
                    translate(0, 0, 15)
                    wave(node.x, node.y, other.x, other.y,
                         node.t_size - i, node.s_weight * 5 - i)

    if frameCount % 4 == 0:
        gif_export(GifMaker)


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

# print text to add to the project's README.md
def settings():
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
