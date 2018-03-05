"""
sketch 63 180304 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

STROKE_W = [10, 5, 4, 3, 2, 1]

def setup():
    size(500, 500)
    rectMode(CENTER)
    generate()

def draw():
    background(128)
    noFill()
    translate(width / 2, height / 2)
    for c in nodes:
        c.update()
    for c in nodes:
        c.plot()
    for c in nodes:
        if random(10) > 9.99 or len(nodes) < 2:  # c.isOn(mouseX, mouseY):
            if c.gen < 5:
                c.sub()
                break
    #if not frameCount % 10: saveFrame("###.tga") # para salvar frames

def keyPressed():
    generate()

def generate():
    global nodes
    nodes = []
    nodes.append(Node(0, 0, 400))


class Node:
    def __init__(self, x, y, s):
        self.edges = set()
        self.x = x
        self.y = y
        self.ix = x
        self.iy = y
        self.s = s
        colorMode(RGB)
        self.ncol = color(255, 0, 0)
        colorMode(HSB)
        self.col = color(random(256), 200, 200)
        self.gen = 0

    def update(self):
        self.x = lerp(self.x, self.ix, 0.09)
        self.y = lerp(self.y, self.iy, 0.09)
        self.col = lerpColor(self.col, self.ncol, 0.05)

    def plot(self):
        strokeWeight(STROKE_W[self.gen])
        if self.edges:
            for e in self.edges:
                stroke(self.col)
                ellipse(self.x, self.y, self.s / 5, self.s / 5)
                if self.gen % 2:
                    stroke(0)
                else:
                    stroke(255)
                seta(e.x, e.y, self.x, self.y, self.s / 4,
                     None, rect, tail_size=self.s / 4)
        #text(str(self.gen), self.x, self.y)

    def isOn(self, mx, my):
        return dist(self.x,
                    self.y,
                    mx,
                    my) < self.s / 2

    def sub(self):
        ms = self.s * 0.5
        mms = ms / 2
        c0 = Node(self.ix - mms, self.iy + mms, ms)
        c0.edges = self.edges
        c0.gen = self.gen + 1
        # replace egges from any child
        for c in nodes:
            if self in c.edges:
                c.edges.remove(self)
                c.edges.add(c0)
        nodes.append(c0)
        c1 = Node(self.ix - mms, self.iy - mms, ms)
        c1.x = self.ix 
        c1.y = self.iy 
        c1.gen = self.gen + 1
        c1.edges.add(c0)
        nodes.append(c1)
        c2 = Node(self.ix + mms, self.iy - mms, ms)
        c2.x = self.ix
        c2.y = self.iy
        c2.gen = self.gen + 1
        c2.edges.add(c0)
        nodes.append(c2)
        c3 = Node(self.ix + mms, self.iy + mms, ms)
        c3.x = self.ix
        c3.y = self.iy
        c3.gen = self.gen + 1
        c3.edges.add(c0)
        nodes.append(c3)
        nodes.remove(self)

def seta(x1, y1, x2, y2, shorter=0, head=None,
         tail_func=None, tail_size=None):
    """
    Seta means arrow in Portuguese
    """
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 10, 5)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        strokeCap(ROUND)
        if L > head:
            line(0, L - offset, -head / 3, L - offset - head)
            line(0, L - offset, head / 3, L - offset - head)
            strokeCap(SQUARE)
            line(0, offset, 0, L - offset)
        if tail_func and tail_size:
            tail_func(0, 0, tail_size, tail_size)
