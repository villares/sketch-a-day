# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190220a", ".gif"
"""
Fixed the transition thing
"""
from collections import namedtuple
import random as rnd
import copy as cp
from gif_exporter import gif_export
from arcs import var_bar, poly_rounded2
add_library('peasycam')
add_library('GifAnimation')

SPACING, MARGIN = 250, 50
X_LIST, Y_LIST = [], []  # listas de posições para elementos
desenho_atual, outro_desenho, desenho_inter, desenho_inicial = [], [], [], []
NUM_NODES = 3  # número de elementos do desenho / number of nodes
Node = namedtuple('Node', 'x y r_size points_to')
save_frames = False
strips = 10

def setup():
    ortho()
    smooth(16)
    size(600, 600, P3D)
    colorMode(HSB)
    rectMode(CENTER)
    noFill()
    cam = PeasyCam(this, 600)
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    novo_desenho(desenho_atual)
    desenho_inicial[:] = cp.deepcopy(desenho_atual)
    println("'s' to save, and 'n' for a new drawing")

def draw():
    global strips, desenho_atual, outro_desenho
    translate(-width / 2, -height/4)
    rotateX(HALF_PI/2)
    background(200)
    fc = frameCount % 200 - 100
    if fc < 0:
        desenho = desenho_atual
    elif 0 <= fc < 99:
        # if frameCount % 10 == 0:.
        make_inter_nodes(map(fc, 0, 100, 0, 1))
        desenho = desenho_inter
    elif fc == 99:
        desenho_atual, outro_desenho = outro_desenho, desenho_atual
        desenho = desenho_atual
        if not mousePressed:
            make_nodes_point(outro_desenho)
        else:
            print("will reset")
            outro_desenho[:] = cp.deepcopy(desenho_inicial)

    desenho_plot(desenho)
    # if frameCount % 4 == 0:
    #    gif_export(GifMaker, filename=SKETCH_NAME, delay=200)
    #strips += 1

def keyPressed():
    global save_frames
    if key == 'g':
        gif_export(GifMaker, filename=SKETCH_NAME)
        # save_frames = not save_frames
        # print "Saving "+repr(save_frames)
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


def new_node(*args):
    if not args:
        return Node(                   # elemento/"nó" uma namedtuple com:
            rnd.choice(X_LIST),        # x
            rnd.choice(Y_LIST),        # y
            rnd.choice([2, 4, 6]),     # r_size
            []  # points_to... (lista com ref. a outro elem.))
        )
    else:
        return Node(*args)

def make_nodes_point(desenho):
    # AREA = (x1y2 + x2y3 + x3y1 – x1y3 – x2y1 – x3y2)/2.
    # x₁ (y₂ - y₃) + x₂ (y₃ - y₁) + x₃ (y₁ - y₂) == 0
    for n0 in desenho:  # para cada elemento do desenho
        n1, n2 = new_node(), new_node()
        while (n1.x * (n2.y - n0.y) +
               n2.x * (n0.y - n1.y) +
               n0.x * (n1.y - n2.y) == 0):
            # if the points are colinear, choose new nodes
            n1, n2 = new_node(), new_node()
        n0.points_to[:] = []
        n0.points_to.append(n1)
        n0.points_to.append(n2)

def desenho_plot(d):
    for node in d:
        p1, p2 = node.points_to  # se estiver apontando para alguém
        with pushMatrix():
            for i in range(10):
                strokeWeight(2)
                translate(0, 0, 15)
                rs = [(node.r_size+ i) * strips,
                      (p1.r_size+ i) * strips,
                      (p2.r_size+ i) * strips, ]
                poly_rounded2([node, p1, p2], rs)

def mouseWheel(E):
    global strips
    strips += int(E.getAmount())
    print(strips)

def make_inter_nodes(amt):
    desenho_inter[:] = []
    for n1, n2 in zip(desenho_atual, outro_desenho):
        desenho_inter.append(Node(                   # elemento/"nó" uma namedtuple com:
            n1.x,        # x
            n1.y,        # y
            n1.r_size,   # r_size
            # cp.deepcopy(n1.points_to)
            [Node(lerp(p1.x, p2.x, amt),
                  lerp(p1.y, p2.y, amt),
                  lerp(p1.r_size, p2.r_size, amt), [])
             for p1, p2 in zip(n1.points_to, n2.points_to)]
        ))

# print text to add to the project's README.md
def settings():
    println(
        """
![{0}](2019/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/2019/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT)
    )
