# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME, OUTPUT = "sketch_190313a", ".gif"
"""
Basedo on sketch_190228a + deque history
"""
from collections import namedtuple, deque
import random as rnd
import copy as cp
from gif_exporter import gif_export
from arcs import poly_rounded2
add_library('peasycam')
add_library('GifAnimation')

X_LIST, Y_LIST = [], []  # listas de posições para elementos
desenho_atual, outro_desenho, desenho_inter, desenho_inicial = [], [], [], []

SPACING, MARGIN = 200, 0
history = deque(maxlen=40)
MAX_S = 2 
LEVELS = 5
NUM_NODES = 20  # número de elementos do desenho / number of nodes
Node = namedtuple('Node', 'x y radius_size points_to')
radius_modifier = 10
end_mode = False

def setup():
    smooth(16)
    size(600, 600, P3D)
    #hint(DISABLE_DEPTH_TEST)
    #blendMode(MULTIPLY)
    colorMode(HSB)
    cam = PeasyCam(this, 660)
    X_LIST[:] = [x for x in range(MARGIN, 1 + width - MARGIN, SPACING)]
    Y_LIST[:] = [y for y in range(MARGIN, 1 + height - MARGIN, SPACING)]
    novo_desenho(desenho_atual)
    desenho_inicial[:] = cp.deepcopy(desenho_atual)

def draw():
    global radius_modifier, desenho_atual, outro_desenho, end_mode
    #ortho()
    #rotateX(HALF_PI / 2)
    translate(-width / 2, -height / 2, - 600) # + 150)
    background(200)
    fc = frameCount % 100 - 50
    if fc < 0:
        desenho = desenho_atual
    elif 0 <= fc < 49:
        make_inter_nodes(map(fc, 0, 50, 0, 1))
        desenho = desenho_inter
    elif fc == 49:
        desenho_atual, outro_desenho = outro_desenho, desenho_atual
        desenho = desenho_atual
        if end_mode: exit()
        if not mousePressed:
            make_nodes_point(outro_desenho)
        else:
            print("will reset")
            end_mode = True
            outro_desenho[:] = cp.deepcopy(desenho_inicial)
     
    history.append(desenho)
    for i, d in enumerate(history):
        translate(0, 0, 1)
        desenho_plot(i, d)
        
    if frameCount % 3 == 0:
          gif_export(GifMaker, filename=SKETCH_NAME, delay=300)
    
def desenho_plot(i, d):
    #noStroke()
    for node in d:
        translate(0, 0, 1)
        p1, p2 = node.points_to  # se estiver apontando para alguém
        with pushMatrix():
           # for i in range(LEVELS):
                fill(128 + 128 * sin((i + frameCount)/20.), 100) #, 255, 255) #164 + i * 8,, 255, 255, 64)
                stroke(128 + 128 * cos((i + frameCount)/20.))
                 # translate(0, 0, 48)
                rs = [(node.radius_size + 10 + 10 * sin(i/4.)),
                      (p1.radius_size + 10 + 10 * sin(i/4.)),
                      (p2.radius_size + 10 + 10 * sin(i/4.)), ]
                poly_rounded2([node, p1, p2], rs)

def keyPressed():
    if key == 'g':
        gif_export(GifMaker, filename=SKETCH_NAME)
    if key == 'r':
        make_nodes_point(desenho_atual)
    if key == 'n':
        novo_desenho(desenho_atual)
    if key == 'p':
        saveFrame(SKETCH_NAME+".png")

def novo_desenho(desenho):
    """
    Esvazia a lista elementos do desenho anterior e cria um novo
    """
    desenho[:] = []
    for X in X_LIST:
        for Y in Y_LIST:
            desenho.append(Node(X, Y, rnd.choice([2, 4, 6]), []))
    make_nodes_point(desenho)
    outro_desenho[:] = cp.deepcopy(desenho)
    make_nodes_point(outro_desenho)


def new_node(base=None):
    if not base:
        return Node(                   # elemento/"nó" uma namedtuple com:
            rnd.choice(X_LIST),        # x
            rnd.choice(Y_LIST),        # y
            10,
            #rnd.choice([0, 0, 0, 0, 100]),     # radius_size
            []  # points_to... (lista com ref. a outro elem.))
        )
    else:
        n =  new_node()
        while dist(n.x, n.y, base.x, base.y) > MAX_S * SPACING:
            n =  new_node()
        return n

def make_nodes_point(desenho):
    # AREA = (x1y2 + x2y3 + x3y1 – x1y3 – x2y1 – x3y2)/2.
    # x₁ (y₂ - y₃) + x₂ (y₃ - y₁) + x₃ (y₁ - y₂) == 0
    for n0 in desenho:  # para cada elemento do desenho
        n1, n2 = new_node(n0), new_node(n0)
        while (n1.x * (n2.y - n0.y) +
               n2.x * (n0.y - n1.y) +
               n0.x * (n1.y - n2.y) == 0
               or dist(n1.x, n1.y, n0.x, n0.y) > SPACING * 1.5
               or dist(n2.x, n2.y, n0.x, n0.y) > SPACING * 1.5):
            # if the points are colinear, choose new nodes
            n1, n2 = new_node(n0), new_node(n0)
        n0.points_to[:] = []
        n0.points_to.append(n1)
        n0.points_to.append(n2)


def make_inter_nodes(amt):
    desenho_inter[:] = []
    for n1, n2 in zip(desenho_atual, outro_desenho):
        desenho_inter.append(Node(                   # elemento/"nó" uma namedtuple com:
            n1.x,        # x
            n1.y,        # y
            n1.radius_size,   # radius_size
            # cp.deepcopy(n1.points_to)
            [Node(lerp(p1.x, p2.x, amt),
                  lerp(p1.y, p2.y, amt),
                  lerp(p1.radius_size, p2.radius_size, amt), [])
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
