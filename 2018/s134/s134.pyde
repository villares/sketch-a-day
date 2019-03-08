# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s134"  # 180514

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

    def relative_pos(self, x, y):
        if self.x - ITEM_WIDTH / 2 <= x <= self.x + ITEM_WIDTH / 2:
            rx = 10  # inside on x
        elif x < self.x - ITEM_WIDTH / 2:
            rx = 0  # x to the left
        elif x > self.x + ITEM_WIDTH / 2:
            rx = 20  # x to the right
        if self.y - ITEM_HEIGHT / 2 <= y <= self.y + ITEM_HEIGHT / 2:
            ry = 1  # inside on y
        elif y < self.y - ITEM_HEIGHT / 2:
            ry = 0  # y is upwards
        elif y > self.y + ITEM_HEIGHT / 2:
            ry = 2  # y us downwards
        return rx + ry


class Link():

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def update(self):
        self.plot()

    def plot(self):
        mx = (self.a.x + self.b.x) / 2
        noFill()
        stroke(0)
        bezier(self.a.x, self.a.y, mx, self.a.y,
               mx, self.b.y, self.b.x, self.b.y)

def mousePressed():
    # global MOUSE_DOWN_POS
    # MOUSE_DOWN_POS = (mouseX, mouseY)
    if keyPressed and keyCode == SHIFT:
        x, y = mouseX, mouseY
        c = input('new item')
        if c:
            Concept.CONCEPTS.append(Concept(c, x, y))

def mouseReleased():
    #if (mouseX, mouseY) != MOUSE_DOWN_POS:
        for i in Concept.CONCEPTS:
            if i.under_mouse:
                i.selected = not i.selected

def keyPressed():
    if key == "l":
        selected = [i for i in Concept.CONCEPTS if i.selected]
        if len(selected) == 2:
            a, b = selected
            LINKS.append(Link(a, b))


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)
