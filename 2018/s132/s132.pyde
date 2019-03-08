# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s132"  # 180512

LINE_SPACE = 22
ITEM_WIDTH = 80
ITEM_HEIGHT = 20

ITEMS, EDGES = [], []

ThemeS = ["sin.com",
          "mat.geo.coo",
          "pst.rcr",
          ]

def setup():
    size(500, 500)
    rectMode(CENTER)
    textAlign(CENTER, CENTER)
    textSize(10)
    for t in ThemeS:
        ITEMS.append(Theme(t))

def draw():
    background(200)
    for i in ITEMS:
        i.update()
    for e in EDGES:
        e.update()


class Theme():
    y_stack = 0

    def __init__(self, content, x=50, y=None):

        self.under_mouse = False
        self.selected = False
        self.x = x
        if y == None:
            Theme.y_stack += LINE_SPACE
            self.y = Theme.y_stack
        else:
            self.y = y
        self.content = content

    def update(self):
        self.move()
        self.plot()

    def move(self):
        if self.mouse_over():
            self.under_mouse = True
            if keyPressed and keyCode == CONTROL:
                self.x = mouseX - ITEM_WIDTH / 2
                self.y = mouseY - ITEM_HEIGHT / 2
            if keyPressed and keyCode == ALT:
                self.selected = not self.selected
        else:
            self.under_mouse = False

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
        rect(self.x, self.y, ITEM_WIDTH, ITEM_HEIGHT)
        fill(0)
        text(self.content, self.x + 6, self.y + 3)

    def mouse_over(self):
        return (self.x < mouseX < self.x + ITEM_WIDTH and
                self.y < mouseY < self.y + ITEM_HEIGHT)
        
class Link():

    def __init__(self, a, b):

        self.under_mouse = False
        self.selected = False
        self.a = a
        self.b = b

    def update(self):
        self.plot()

    def plot(self):
        mx = (self.a.x + self.b.x) / 2
        noFill()
        bezier(self.a.x, self.a.y, mx, self.a.y,
               mx, self.b.y, self.b.x, self.b.y)

def mousePressed():
    if keyPressed and keyCode == SHIFT:
        x, y = mouseX, mouseY
        c = input('new item')
        if c:
            ITEMS.append(Theme(c, x, y))

def keyPressed():
    if key == "l":
        selected = [i for i in ITEMS if i.selected]
        if len(selected) == 2:
            a, b = selected
            EDGES.append(Link(a, b))


def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)




    # def mouse_over(self):
    #     return (self.x < mouseX < self.x + ITEM_WIDTH and
    #             self.y < mouseY < self.y + ITEM_HEIGHT)
