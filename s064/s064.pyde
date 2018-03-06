"""
sketch 64 180395 - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""
import random as rnd

LIST = []
SRINK = .50
OFFSET = .25
SIZE = 236  # base size
SAVE_FRAME = False
NODE_DRAW = [rect,
             ellipse,
             ]

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
    global SAVE_FRAME, DRAW_F, SRINK, OFFSET
    if key == " ":
        LIST[:] = [Cell()]
        SRINK = .50
        OFFSET = .25
    if key == "r":
        NODE_DRAW.append(NODE_DRAW.pop(0))  # circles drawing functions list
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
        global SAVE_FRAME
        self.draw()  # draws itself
        if not self.LIST:
            # if random(100) < 7 / (self.gen + 1):
            #     self.divide()
            #     SAVE_FRAME = True
            if mousePressed and self.on_mouse():
                self.divide()  # will create new sub-cells
                SAVE_FRAME = True
        # otherwise will recursively update sub-cells and draw a line to them
        else:
            for sub_cell in self.LIST:
                sub_cell.update()
                if self.gen % 2:
                    stroke(0)
                else:
                    stroke(255)
                strokeWeight((6-self.gen))
                seta(self.x, self.y, sub_cell.x, sub_cell.y,
                     sub_cell.s(), tail_func=ellipse,
                     tail_size=sub_cell.s() )

    def draw(self):
        noStroke()
        fill(self.color)
        NODE_DRAW[0](self.x, self.y, self.s(), self.s())
        noFill()
        #NODE_DRAW[0](self.x, self.y, 4, 4)
        #text(str(self.gen), self.x, self.y)

    def divide(self):
        if self.gen < 6:
            x, y = self.x, self.y
            new_gen = self.gen + 1
            o = self.s() * OFFSET * new_gen
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
        #if frameCount < 600: #and not frameCount % 3:
        saveFrame("48-######.tga")
        
def seta(x1, y1, x2, y2, shorter=0, head=None,
         tail_func=None, tail_size=None):
    """
    Seta means arrow in Portuguese
    """
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 5, 5)
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