"""
sketch 59 180228 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

from collections import namedtuple
import random as rnd
import copy as cp

SPACING, MARGIN = 50, 75
POSITIONS = []  # listas de posições para elementos
INI_DRW, CURRENT_DRW, TARGET_DRW, INTER_DRW = [], [], [], []
Node = namedtuple(
    'Node', 'x y t_size s_weight is_arrow points_to')
SAVE_FRAMES = False

def setup():
    size(600, 600)
    rectMode(CENTER)
    noFill()
    for x in range(MARGIN, 1 + width - MARGIN, SPACING):
        for y in range(MARGIN, 1 + height - MARGIN, SPACING):
            POSITIONS.append((x, y))
    create_drawing(CURRENT_DRW)
    println("'s' to save, and 'n' for a new drawing")

def keyPressed():
    global SAVE_FRAMES
    if key == 's':
        SAVE_FRAMES = not SAVE_FRAMES
        print "Saving " + repr(SAVE_FRAMES)
    if key == 'r':
        randomize_points_to(CURRENT_DRW)
    if key == 'n':
        create_drawing(CURRENT_DRW)

def create_drawing(drawing):
    """
    clears the list of nodes and creates a a new drawing appending CURRENT_DRW,
    a list of nodes/drawing elements: arrows, connecting lines and lonely nodes
    """
    drawing[:] = []
    for x, y in POSITIONS:
        drawing.append(Node(x, y,
                            rnd.choice([5, 10, 15]),    # t_size
                            rnd.choice([1, 2, 3]),      # s_weight
                            rnd.choice([True, False]),  # is_arrow?
                            []  # points_to... (lista com ref. a outro elem.))
                            ))
    randomize_points_to(drawing)
    INI_DRW[:] = cp.deepcopy(drawing)  # saves a copy to INItial DRaWing
    TARGET_DRW[:] = cp.deepcopy(drawing)  # creates another drawing
    randomize_points_to(TARGET_DRW)       # randomizes nodes pointed

def randomize_points_to(drawing):
    for node in drawing:  # para cada elemento do drawing
        node.points_to[:] = []
        random_node = rnd.choice(drawing)  # sorteia outro elemento
        while dist(node.x, node.y, random_node.x, random_node.y) > 2.88 * SPACING:
            random_node = rnd.choice(drawing)
        if (node.x, node.y) != (random_node.x, random_node.y):
            # 'aponta' para este elemento, acrescenta na sub_lista
            node.points_to.append(random_node)

def draw():
    global CURRENT_DRW, TARGET_DRW
    background(200)
    fc = frameCount % 301 - 150
    if fc < 0:
        draw_now = CURRENT_DRW
    elif 0 <= fc < 150:
        make_inter_nodes(map(fc, 0, 150, 0, 1), CURRENT_DRW, TARGET_DRW)
        draw_now = INTER_DRW
    elif fc == 150 and frameCount < 1050:
        CURRENT_DRW, TARGET_DRW = TARGET_DRW, CURRENT_DRW
        draw_now = CURRENT_DRW
        randomize_points_to(TARGET_DRW)
    else:
        if TARGET_DRW == INI_DRW:
            println('end of last cicle')
            noLoop()  # stop draw at the end of this frame
        else:
            println('start of last cicle')
        CURRENT_DRW, TARGET_DRW = TARGET_DRW, INI_DRW
        draw_now = CURRENT_DRW

    # draws white 'lines', non-arrows, INI_DRW.
    for node in (n for n in draw_now if not n.is_arrow):
        for other in node.points_to:  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(255)
            line(node.x, node.y, other.x, other.y)
            # desenha o círculo (repare que só em nós que 'apontam')
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws 'lonely nodes' in red (nodes that do not point anywhere)
    for node in (n for n in draw_now if not n.points_to):
        strokeWeight(node.s_weight)
        stroke(255, 0, 0)  # red stroke for lonely nodes
        if node.is_arrow:
            rect(node.x, node.y, node.t_size, node.t_size)
        else:
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws black arrows
    for node in (n for n in draw_now if n.is_arrow):
        for other in node.points_to:  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(0)
            seta(node.x, node.y, other.x, other.y,
                 node.t_size, node.s_weight * 5,
                 rect, node.t_size)
    if SAVE_FRAMES and not fc % 10:
        saveFrame("####.tga")

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
        if L > head * 2:
            line(0, L - offset, -head / 3, L - offset - head)
            line(0, L - offset, head / 3, L - offset - head)
            strokeCap(SQUARE)
            line(0, offset, 0, L - offset)
        if tail_func and tail_size:
            tail_func(0, 0, tail_size, tail_size)

def make_inter_nodes(amt, origin, target):
    INTER_DRW[:] = []
    for n1, n2 in zip(origin, target):
        if n1.points_to:
            p1x, p1y = n1.points_to[0].x, n1.points_to[0].y
        else:
            p1x, p1y = n1.x, n1.y
        if n2.points_to:
            p2x, p2y = n2.points_to[0].x, n2.points_to[0].y
        else:
            p2x, p2y = n2.x, n2.y
        INTER_DRW.append(Node(  # elemento/"nó" uma namedtuple com:
            n1.x,              # x
            n1.y,              # y
            n1.t_size,       # t_size (tail/circle size)
            n1.s_weight,     # s_weight (espessura da linha)
            n1.is_arrow,     # is_arrow? (se é seta ou 'linha')
            # cp.deepcopy(n1.points_to)
            [PVector(lerp(p1x, p2x, amt), lerp(p1y, p2y, amt))]
        ))
