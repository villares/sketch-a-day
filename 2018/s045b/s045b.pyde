"""
sketch 45b 180214 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

LIST = []
SRINK = .50
OFFSET = .25
SIZE = 512  # base size
SAVE_FRAME = False
DRAW_MODE = rect

def setup():
    size(512 + 200, 512 + 200)
    rectMode(CENTER)
    colorMode(HSB)
    strokeWeight(2)
    LIST.append(Cell())

def draw():
    translate(width / 2, height / 2)
    background(200)
    for cell in LIST:
        cell.update()
    save_frame()  # saves frame if SAVE_FRAME is set True

def keyPressed():
    global SAVE_FRAME, DRAW_MODE
    if key == " ":
        LIST[:] = [Cell()]
    if key == "r":
        if DRAW_MODE == rect:
            DRAW_MODE = ellipse
        else: DRAW_MODE = rect
        SAVE_FRAME = True


class Cell():

    def __init__(self, x=0, y=0, gen=0, gen_offset=0,
                     xo=0, yo=0, mother=None):
        self.LIST = []
        self.x, self.y, self.xo, self.yo = x, y, xo, yo
        self.gen = gen
        self.mother = mother
        self.color = color(random(0, 200), 200, 200, 200)

    def s(self):  # size
        return SIZE * (SRINK ** self.gen)

    def update(self):
        self.draw()  # draws itself
        if not self.LIST:
            # if no sub-cells, its a lead (para células sem sub-células)
            # and if  mouse is pressed inside it
            if mousePressed and self.on_mouse():
                self.divide()  # will create new sub-cells
        # otherwise will recursively update sub-cells and draw a line to them
        else:
            for sub_cell in self.LIST:
                sub_cell.update()
                stroke(0)
                line(self.x, self.y, sub_cell.x, sub_cell.y)

    def draw(self):
        draw_function = DRAW_MODE
        x =self.x + self.xo * self.s() * OFFSET
        y =self.y + self.yo * self.s() * OFFSET
        noStroke()
        fill(self.color)
        draw_function(x, y, self.s(), self.s())
        fill(0)
        draw_function(x, y, 4, 4)
        #text(str(self.gen), self.x, self.y)

    def divide(self):
        if self.gen < 6:
            global SAVE_FRAME
            SAVE_FRAME = True
            new_gen = self.gen + 1
            o = self.s() * OFFSET
            go = 0 #new_gen * 2
            self.LIST.append(Cell(gen=new_gen, xo=+1, yo=+1, mother=self))
            self.LIST.append(Cell(gen=new_gen, xo=+1, yo=-1, mother=self))
            self.LIST.append(Cell(gen=new_gen, xo=-1, yo=+1, mother=self))
            self.LIST.append(Cell(gen=new_gen, xo=-1, yo=-1, mother=self))
            #self.gen = 6

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
        # saveFrame("45-######.tga")