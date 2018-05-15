# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s135"  # 180515

LINE_SPACE = 22
ITEM_WIDTH = 80
ITEM_HEIGHT = 20
MOUSE_PRESSED = False
LINKS = []

CONCEPT_LIST = ["sin.com",
                "mat.geo.coo",
                "pst.rcr",
                ]

def setup():
    size(500, 500)
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    textSize(10)
    strokeWeight(2)
    for c in CONCEPT_LIST:
        Concept.CONCEPTS.append(Concept(c))

def draw():
    background(200)
    for e in LINKS:
        e.update()
    for i in Concept.CONCEPTS:
        i.update()


class Concept():

    CONCEPTS = []
    y_stack = 0

    def __init__(self, content, x=50, y=None):

        self.under_mouse = False
        self.selected = False
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
        noFill()
        if self.under_mouse:
            B = 255
        else:
            B = 0
        if self.selected:
            R = 255
        else:
            R = 0
        stroke(R, 0, B)
        fill(200)
        rect(self.x, self.y, ITEM_WIDTH, ITEM_HEIGHT, ITEM_HEIGHT / 4)
        fill(0)
        text(self.content, self.x, self.y)

    def mouse_over(self):
        return self.relative_pos(mouseX, mouseY) == 11  # 11 means inside

    def relative_pos(self, ox, oy):
        """ compares self position with other (ox, oy) position"""
        if self.x - ITEM_WIDTH / 2 <= ox <= self.x + ITEM_WIDTH / 2:
            rx = 10  # inside on x
        elif ox < self.x - ITEM_WIDTH / 2:
            rx = 0  # x to the left
        elif ox > self.x + ITEM_WIDTH / 2:
            rx = 20  # x to the right
        if self.y - ITEM_HEIGHT / 2 <= oy <= self.y + ITEM_HEIGHT / 2:
            ry = 1  # inside on y
        elif oy < self.y - ITEM_HEIGHT / 2:
            ry = 0  # y is upwards
        elif oy > self.y + ITEM_HEIGHT / 2:
            ry = 2  # y us downwards
        return rx + ry

    def linking_point(self, other_x, other_y):
        rp = self.relative_pos(other_x, other_y)
        if rp >= 11:
            return (self.x + ITEM_WIDTH / 2, self.y)
        else:
            return (self.x - ITEM_WIDTH / 2, self.y)

class Link():

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def update(self):
        self.plot()

    def plot(self):

        p1x, p1y = self.a.linking_point(self.b.x, self.b.y)
        p2x, p2y = self.b.linking_point(self.a.x, self.a.y)
        mpx = (p1x + p2x) / 2
        noFill()
        stroke(0)
        bezier(p1x, p1y, mpx, p1y,
               mpx, p2y, p2x, p2y)

def mouseClicked():
    for i in Concept.CONCEPTS:
        if i.under_mouse:
            i.selected = not i.selected
    if keyPressed and keyCode == SHIFT:
        x, y = mouseX, mouseY
        c = input('new item')
        if c:
            Concept.CONCEPTS.append(Concept(c, x, y))

def keyPressed():
    if key == "l":
        selected = [i for i in Concept.CONCEPTS if i.selected]
        if len(selected) == 2:
            a, b = selected
            LINKS.append(Link(a, b))


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
