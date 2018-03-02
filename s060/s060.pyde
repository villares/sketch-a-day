"""
sketch 60 180301 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
from collections import namedtuple
import random as rnd
import copy as cp

SPACING, MARGIN = 50, 75
POSITIONS = []  # listas de posições para elementos
Point = namedtuple('Point', 'x y')
DRAWING = []
SAVE_FRAMES = False

def setup():
    size(600, 600)
    rectMode(CENTER)
    noFill()
    for x in range(MARGIN, 1 + width - MARGIN, SPACING):
        for y in range(MARGIN, 1 + height - MARGIN, SPACING):
            POSITIONS.append((x, y))
    create_drawing(DRAWING)
    println("'s' to save, and 'n' for a new drawing")

def keyPressed():
    global SAVE_FRAMES
    if key == 's':
        SAVE_FRAMES = not SAVE_FRAMES
        print "Saving " + repr(SAVE_FRAMES)
    if key == 'n':
        create_drawing(DRAWING)

def create_drawing(drawing):
    """
    clears the list of nodes and creates a a new drawing appending a
    list of nodes/drawing elements: arrows, connecting lines and lonely nodes
    """
    drawing[:] = []
    for x, y in POSITIONS:
        drawing.append(D_node(x, y, DRAWING))
    for node in drawing:  # para cada elemento do drawing
        node.randomize_target(0)  # set of random targets
        node.copy_target(0, -1)  # backup of original targets
        node.randomize_target(1)  # secondary set of random targets

def draw():
    background(200)
    fc = frameCount % 301 - 150
    if fc < 0 : fase = 0    
    elif 0 <= fc < 150:
        fase= map(fc, 0, 150, 0, 1)
    elif fc == 150: # and frameCount < 1050:
        fase = 0
        for node in DRAWING:
            node.copy_target(1, 0)
            node.randomize_target(1)
    # else:
    #     if TARGET_DRW == INI_DRW:
    #         println('end of last cicle')
    # noLoop()  # stop draw at the end of this frame
    #     else:
    #         println('start of last cicle')
    #     CURRENT_DRW, TARGET_DRW = TARGET_DRW, INI_DRW
    #     DRAWING = CURRENT_DRW

    # draws white 'lines', non-arrows, INI_DRW.
    for node in (n for n in DRAWING if not n.is_arrow):
        for other in node.points_now(fase):  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(node.s_color(fase))
            line(node.x, node.y, other.x, other.y)
            # desenha o círculo (repare que só em nós que 'apontam')
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws 'lonely nodes' in red (nodes that do not point anywhere)
    for node in (n for n in DRAWING if not n.points_now(fase)):
        strokeWeight(node.s_weight)
        stroke(node.s_color(fase))  # red stroke for lonely nodes
        if node.is_arrow:
            rect(node.x, node.y, node.t_size, node.t_size)
        else:
            ellipse(node.x, node.y, node.t_size, node.t_size)
    # then draws black arrows
    for node in (n for n in DRAWING if n.is_arrow):
        for other in node.points_now(fase):  # se estiver apontando para alguém
            strokeWeight(node.s_weight)
            stroke(node.s_color(fase))
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


class D_node(object):

    """
    A class of drawing elements, that might be arrows and point to some other element
    """

    def __init__(self, x, y, drawing):
        self.x = x
        self.y = y
        self.t_size = rnd.choice([5, 10, 15])    # t_size
        self.s_weight = rnd.choice([1, 2, 3])    # s_weight
        self.is_arrow = rnd.choice([True, False])
        self.points_to = [[], [], []]
        self.drawing = drawing

    def randomize_target(self, index=0):
        self.points_to[index][:] = []
        rnd_node = rnd.choice(self.drawing)  # sorteia outro elemento
        while dist(self.x, self.y, rnd_node.x, rnd_node.y) > 2.88 * SPACING:
            rnd_node = rnd.choice(self.drawing)
        if (self.x, self.y) != (rnd_node.x, rnd_node.y):
            # 'aponta' para este elemento, acrescenta na sub_lista
            self.points_to[index].append(Point(rnd_node.x, rnd_node.y))

    def copy_target(self, origin, destination):
        self.points_to[destination] = cp.deepcopy(self.points_to[origin])

    def never_empty(self, points):
        if not points:
            return [Point(self.x, self.y)]
        else:
            return points

    def points_now(self, amt=0):
        p0 = self.never_empty(self.points_to[0])[0]
        p1 = self.never_empty(self.points_to[1])[0]
        if amt == 0 or amt == 1:
            return self.points_to[int(amt)]
        else:
            return [Point(lerp(p0.x, p1.x, amt),
                          lerp(p0.y, p1.y, amt))]
            
    def s_color(self, amt):
        if amt == 0 or amt == 1:
            if not self.points_to[int(amt)]: return color(255, 0, 0)
            elif self.is_arrow:
                return color(0)
            else: return color(255)
        else: return lerpColor(self.s_color(0), self.s_color(1), amt)