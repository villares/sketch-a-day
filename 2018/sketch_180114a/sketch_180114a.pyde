"""
s180114 3D Graphs!
(c)2018 Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

add_library('peasycam')
import random as rnd

CEL_SIZE = 100
HALF_CEL = CEL_SIZE / 2
CELLS = []
Z_INC = 20

def setup():
    global ROWS, COLS, CELLS  # filas e colunas
    size(500, 500, P3D)
    ROWS, COLS = int(height / CEL_SIZE), int(width / CEL_SIZE)
    rectMode(CENTER)
    colorMode(HSB)
    cam = PeasyCam(this, 500)
    grid(CELLS, Circle, ROWS, COLS)

def draw():
    global ANG, mm
    mm = 1
    background(255)
    for c in CELLS:
        c.update()
        #c.showEdges()
        if c.isOn(mouseX, mouseY):
            c.sub()


def grid(list, func, num_rows, num_cols):
    for r in range(num_rows):
        for c in range(num_cols):
            with pushMatrix():
                list.append(func(HALF_CEL + c * CEL_SIZE,
                                  HALF_CEL + r * CEL_SIZE)
                             )

def keyPressed():
    global CELLS
    if key == ' ':
        CELLS = []
        grid(CELLS, Circle, ROWS, COLS)

        

class Circle:

    def __init__(self, x, y, s=CEL_SIZE, c=color(255, 200, 200)):
        self.edges = set()
        self.x = x
        self.y = y
        self.ix = x
        self.iy = y
        self.s = s
        self.b = 12
        self.ncol = color(random(256), 200, 200)
        self.col = c
        self.z = 0
        print COLS * ROWS, len(CELLS)
        if 1 < len(CELLS) < 26 and random(10) < 5:
            self.edges.add(rnd.choice(CELLS))

    def mouseMovement(self):
        mx, my = mouseX, mouseY
        cx = self.x
        cy = self.y
        maxDist = 50
        dis = dist(cx, cy, mx, my)
        ang = atan2(cy - my, cx - mx)
        if (dis < maxDist):
            dd = map(dis, 0, maxDist, 1, 0)
            dd = pow(dd, 0.9) * 20 * mm
            self.x += cos(ang) * dd
            self.y += sin(ang) * dd

    def update(self):

        self.x = lerp(self.x, self.ix, 0.09)
        self.y = lerp(self.y, self.iy, 0.09)
        self.col = lerpColor(self.col, self.ncol, 0.05)
        with pushMatrix():
            translate(-width/2, -height/2)
            self.mouseMovement()
            self.showShadow()
            self.show()
            self.showEdges()

    def showShadow(self):
        # noStroke()
        fill(0, 20)
        stroke(self.col)
        ellipse(self.x, self.y, self.s, self.s)

    def showEdges(self):
        strokeWeight(3)
        stroke(0)
        for e in self.edges:
            line(self.x, self.y, self.z, e.x, e.y, e.z)

    def show(self):
        noStroke()
        fill(0)
        pushMatrix()
        translate(self.x, self.y, self.z)
        sphere(self.b/2)
        #ellipse(self.x, self.y, self.b, self.b)
        popMatrix()

    def isOn(self, mx, my):
        return dist(self.x, self.y, mx, my) < self.s / 2

    def sub(self):
        ms = self.s * 0.5
        mms = ms / 2
        c0 = Circle(self.ix - mms, self.iy + mms, ms, self.col)
        c0.edges = self.edges
        c0.z = self.z + Z_INC
        # replace egges from any child
        for c in CELLS:
            if self in c.edges:
                c.edges.remove(self)
                c.edges.add(c0)
        CELLS.append(c0)

        c1 = Circle(self.ix - mms, self.iy - mms, ms, self.col)
        c1.x += self.x - self.ix
        c1.y += self.y - self.iy
        c1.z = self.z + Z_INC
        c1.edges.add(c0)
        CELLS.append(c1)

        c2 = Circle(self.ix + mms, self.iy - mms, ms, self.col)
        c2.x += self.x - self.ix
        c2.y += self.y - self.iy
        c2.z = self.z + Z_INC
        c2.edges.add(c0)
        CELLS.append(c2)

        c3 = Circle(self.ix + mms, self.iy + mms, ms, self.col)
        c3.x += self.x - self.ix
        c3.y += self.y - self.iy
        c3.z = self.z + Z_INC
        c3.edges.add(c0)
        CELLS.append(c3)

        CELLS.remove(self)