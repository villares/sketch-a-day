"""
sketch 62 180303 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

import random as rnd
import copy as cp

SPACING, MARGIN, RANGE = 50, 75, 1
DRAWING = []  # drawing elements 'D_nodes'
SAVE_FRAMES = True

def setup():
    size(500, 500)
    rectMode(CENTER)
    noFill()
    create_drawing(DRAWING)

def keyPressed():
    global RANGE
    if key == 'n':
        create_drawing(DRAWING)
    if key == 'b':
        for node in DRAWING:
            node.copy_target(-1, 1)  # target back to the first points
    if key == '=' or key == "+":
        RANGE += .5
    if key == '-' and RANGE > 1:
        RANGE -= .5

def create_drawing(drawing):
    """
    clears the list of nodes and creates a a new drawing appending a
    list of nodes/drawing elements: arrows, connecting lines and lonely nodes
    """
    drawing[:] = []
    for x in range(MARGIN, 1 + width - MARGIN, SPACING):
        for y in range(MARGIN, 1 + height - MARGIN, SPACING):
            drawing.append(D_node(x, y, DRAWING))
    for node in drawing:  # para cada elemento do drawing
        node.randomize_target(0, RANGE * SPACING)  # set of random targets
        node.copy_target(0, -1)   # backup of original targets
        node.randomize_target(1, RANGE * SPACING)  # secondary set of random targets

def draw():
    background(200)
    fc = frameCount % 300 - 150
    if fc < 0:
        fase = 0
    elif 0 <= fc < 149:
        fase = map(fc, 0, 149, 0, 1)
    # and frameCount < 1050:  # add/remove 300 for longer/shorter
    elif fc == 149:
        fase = 0
        for node in DRAWING:
            node.copy_target(1, 0)
            node.randomize_target(1, RANGE * SPACING)

    # draws circles/'lines', non-arrows
    for node in (n for n in DRAWING if not n.is_arrow):
        node.plot(fase)
    # draws arrows
    for node in (n for n in DRAWING if n.is_arrow):
        node.plot(fase)
    if SAVE_FRAMES and not fc % 10:
        saveFrame("####.tga")

class D_node(object):

    """ Drawing elements,  arrows or circles that might point to another element """

    def __init__(self, x, y, drawing):
        self.x = x
        self.y = y
        self.t_size = rnd.choice([5, 10, 15])    # t_size
        self.s_weight = rnd.choice([1, 2, 3])    # s_weight
        self.is_arrow = rnd.choice([True, False])
        self.points_to = [[], [], []] # current targets, next targets, initial targets
        self.drawing = drawing

    def plot(self, amt, other=None):
        strokeWeight(self.s_weight)
        stroke(self.s_color(amt))
        for other in self.points_now(amt):
            if self.is_arrow:
                seta(self.x, self.y, other.x, other.y,
                     self.t_size, self.s_weight * 5, # shorten amount, head size
                     rect, self.t_size) # tail func, tail size
            else:
                line(self.x, self.y, other.x, other.y)
                ellipse(self.x, self.y, self.t_size, self.t_size)
        if not other:
            if self.is_arrow:
                other = self
                seta(self.x, self.y, other.x, other.y,
                     self.t_size, self.s_weight * 5,
                     rect, self.t_size)
            else:
                ellipse(self.x, self.y, self.t_size, self.t_size)

    def randomize_target(self, index, range_times_spacing):
        self.points_to[index][:] = []
        for _ in range(3):
            rnd_node = rnd.choice(self.drawing)
            while dist(self.x, self.y, rnd_node.x, rnd_node.y) > range_times_spacing:
                rnd_node = rnd.choice(self.drawing)
            if (self.x, self.y) != (rnd_node.x, rnd_node.y) and random(10) < 5:
                self.points_to[index].append(PVector(rnd_node.x, rnd_node.y))

    def copy_target(self, origin, destination):
        self.points_to[destination] = cp.deepcopy(self.points_to[origin])

    def never_empty(self, points):
        if not points:
            return [PVector(self.x, self.y)]
        else:
            return points

    def points_now(self, amt=0):
        points = []
        if amt == 0 or amt == 1:
            return self.points_to[int(amt)]
        else:
            #for p0 in self.never_empty(self.points_to[0]):
                p0 = self.never_empty(self.points_to[0])[0]   # not all interpolated arrows are shown
                for p1 in self.never_empty(self.points_to[1]):
                    points.append(PVector(lerp(p0.x, p1.x, amt),
                                          lerp(p0.y, p1.y, amt)))
        return points

    def s_color(self, amt):
        if amt == 0 or amt == 1:
            if not self.points_to[int(amt)]:
                return color(0, 0, 255)
            elif self.is_arrow:
                return color(0)
            else:
                return color(255)
        else:
            return lerpColor(self.s_color(0), self.s_color(1), amt)

def seta(x1, y1, x2, y2, shorter=0, head=None,
         tail_func=None, tail_size=None):
    """
    Seta means arrow in Portuguese
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
