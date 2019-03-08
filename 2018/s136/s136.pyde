# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day

SKETCH_NAME = "s136"  # 180516

LINE_SPACE = 22
ITEM_WIDTH = 80
ITEM_HEIGHT = 20
MOUSE_PRESSED = False

CONCEPT_LIST = ["sin", "sin.com",
                "mat", "mat.geo", "mat.geo.coo",
                "pst",
                "pst.oop",
                "pst.rcr",
                "con", "con.cnd", "con.ite",
                ]

def setup():
    size(500, 500)
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    textSize(10)
    for c in CONCEPT_LIST:
        Concept.CONCEPTS.append(Concept(c))

def draw():
    background(200)
    for l in Link.LINKS:
        l.update()
    for c in Concept.CONCEPTS:
        c.update()


def mouseClicked():
    for c in Concept.CONCEPTS:
        if c.under_mouse:
            c.selected = not c.selected
    if keyPressed and keyCode == SHIFT:
        x, y = mouseX, mouseY
        ct = input('new item')
        if ct:
            Concept.CONCEPTS.append(Concept(ct, x, y))

def keyPressed():
    """ Key pressed event """
    if key == "l":
        selected = [c for c in Concept.CONCEPTS if c.selected]
        if len(selected) == 2:
            a, b = selected
            Link.LINKS.append(Link(a, b))


class Concept():

    CONCEPTS = []
    y_stack = 0

    def __init__(self, content, x=None, y=None):
        self.under_mouse = False
        self.selected = False
        if x == None:
            if len(content) > 7:
                self.x = 450
            elif len(content) > 4:
                self.x = 250
            else:
                self.x = 50
        else:
            self.x = x
        if y == None:
            Concept.y_stack += LINE_SPACE
            self.y = Concept.y_stack
        else:
            self.y = y
        self.content = content

    def update(self):
        self.move()
        self.plot()
        self.under_mouse = self.mouse_over()

    def move(self):
        if self.selected and mousePressed:
            deltaX = mouseX - pmouseX
            deltaY = mouseY - pmouseY
            self.x += deltaX
            self.y += deltaY

    def plot(self):
        strokeWeight(2)
        noFill()
        if self.under_mouse:
            B = 0
        else:
            B = 255
        if self.selected:
            R = 0
        else:
            R = 255
        stroke(R, 255, B)
        # fill(200)
        rect(self.x, self.y, ITEM_WIDTH, ITEM_HEIGHT, ITEM_HEIGHT / 4)
        fill(0)
        text(self.content, self.x, self.y)

    def mouse_over(self):
        return (self.x - ITEM_WIDTH / 2 <= mouseX <= self.x + ITEM_WIDTH / 2 and
                self.y - ITEM_HEIGHT / 2 <= mouseY <= self.y + ITEM_HEIGHT / 2)

    def relative_pos(self, ox, oy):
        """ compares self position with other (ox, oy) position"""
        if self.x - ITEM_WIDTH <= ox <= self.x + ITEM_WIDTH:
            rx = 10  # inside on x
        elif ox < self.x - ITEM_WIDTH:
            rx = 0  # x to the left
        elif ox > self.x + ITEM_WIDTH:
            rx = 20  # x to the right
        if self.y - ITEM_HEIGHT <= oy <= self.y + ITEM_HEIGHT:
            ry = 1  # inside on y
        elif oy < self.y - ITEM_HEIGHT:
            ry = 0  # y is upwards
        elif oy > self.y + ITEM_HEIGHT:
            ry = 2  # y is downwards
        return rx + ry

    def linking_point(self, other):
        rp = self.relative_pos(other.x, other.y)

        mpx = (self.x + other.x) / 2
        mpy = (self.y + other.y) / 2

        if rp < 10:
            px, py = self.x - ITEM_WIDTH / 2, self.y
            cx, cy = mpx, self.y
        elif rp > 12:
            px, py = self.x + ITEM_WIDTH / 2, self.y
            cx, cy = mpx, self.y
        else:
            if rp <= 11:
                px, py = self.x, self.y - ITEM_HEIGHT / 2
            else:
                px, py = self.x, self.y + ITEM_HEIGHT / 2
            cx, cy = self.x, mpy

        return px, py, cx, cy

class Link():

    LINKS = []

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def update(self):
        self.plot()

    def plot(self):
        p1x, p1y, c1x, c1y = self.a.linking_point(self.b)
        p2x, p2y, c2x, c2y = self.b.linking_point(self.a)
        noFill()
        stroke(0)
        strokeWeight(1)
        bezier(p1x, p1y, c1x, c1y,
               c2x, c2y, p2x, p2y)


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
