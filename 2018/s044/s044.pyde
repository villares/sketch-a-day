"""
sketch 44 180213a - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

LIST = []
SRINK = .50
OFFSET = .50
SIZE = 256  # base size
SAVE_FRAME = False
RECT_MODE = True

def setup():
    size(512, 512)
    rectMode(CENTER)
    colorMode(HSB)
    strokeWeight(2)
    LIST.append(Cell())

def draw():
    translate(width / 2, height / 2)
    background(255)
    for cell in LIST:
        cell.update()
    save_frame() # saves frame if SAVE_FRAME is set True

def keyPressed():
    global SAVE_FRAME, RECT_MODE
    if key == " ":
        LIST[:] = [Cell()]
    if key == "r":
        RECT_MODE = not RECT_MODE
        SAVE_FRAME = True


class Cell():

    def __init__(self, x=0, y=0, gen=0):
        self.LIST = []
        self.x, self.y = x, y
        self.gen = gen
        self.color = color(random(0, 200), 200, 200, 200)

    def s(self):  # size
        return SIZE * (SRINK ** self.gen)

    def update(self):
        self.draw() # draws itself
        if not self.LIST:
            # if no sub-cells, its a leaf-cell (células sem sub-células)
            if mousePressed and self.on_mouse(): # and if  mouse is pressed inside it
                self.divide() # will create new sub-cells
        else:
            # otherwise will recursively update sub-cells and draw a line to them
            for sub_cell in self.LIST:
                sub_cell.update()
                stroke(0)
                line(self.x, self.y, sub_cell.x, sub_cell.y)

    def draw(self):
        noStroke()
        fill(self.color)
        if not RECT_MODE:
            ellipse(self.x, self.y, self.s(), self.s())
        else:
            rect(self.x, self.y, self.s(), self.s())
        fill(0)
        #text(str(self.gen), self.x, self.y)

    def divide(self):
        global SAVE_FRAME
        SAVE_FRAME = True
        x, y = self.x, self.y
        o = self.s() * OFFSET
        new_gen = self.gen + 1
        if new_gen < 7:
            self.LIST.append(Cell(x + o, y + o, gen=new_gen))
            self.LIST.append(Cell(x + o, y - o, gen=new_gen))
            self.LIST.append(Cell(x - o, y + o, gen=new_gen))
            self.LIST.append(Cell(x - o, y - o, gen=new_gen))
            #self.gen = new_gen

    def on_mouse(self):
        x, y = self.x + width / 2, self.y + height / 2
        r = self.s() / 2
        if (x - r < mouseX < x + r and
                y - r < mouseY < y + r):
            return True

def save_frame():
    global SAVE_FRAME
    if SAVE_FRAME:
        SAVE_FRAME = False
        saveFrame("######.tga")