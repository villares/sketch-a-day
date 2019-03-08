# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
# SKETCH_NAME = "s137"  # 180516
# data/list.txt contém a lista

add_library('pdf')

def setup():
    CONCEPT_LIST = leitura_tabela("list.txt")
    size(500, 3000)
    #size(500, 3000, PDF, "diagram.pdf")

    for c in CONCEPT_LIST:
        Concept.CONCEPTS.append(Concept(c))
        
    c0_list = [c for c in Concept.CONCEPTS if c.level == 0]
    c1_list = [c for c in Concept.CONCEPTS if c.level == 1]
    c2_list = [c for c in Concept.CONCEPTS if c.level == 2]

    for c0 in c0_list:
        for c1 in c1_list:
            if c0.l0 == c1.l0:
                 Link.LINKS.append(Link(c0, c1))        
                
    for c1 in c1_list:
        for c2 in c2_list:
            if c1.l0 + c1.l1 == c2.l0 + c2.l1:
                 Link.LINKS.append(Link(c1, c2))

def draw():
    background(200)
    for l in Link.LINKS:
        l.update()
    for c in Concept.CONCEPTS:
        c.update()
    noLoop()
    # exit() # para uso com o size(500, 300, PDF...) exportação de PDF...


def mouseClicked():
    """ select and de-select items, shift+click to add items """
    for c in Concept.CONCEPTS:
        if c.under_mouse:
            c.selected = not c.selected
    if keyPressed and keyCode == SHIFT:
        x, y = mouseX, mouseY
        ct = input('new item')
        if ct:
            Concept.CONCEPTS.append(Concept(ct, x, y))

def keyPressed():
    """ Key pressed event, 'l' to create a link between items """
    if key == "l":
        list_of_selected_items = [c for c in Concept.CONCEPTS if c.selected]
        if len(list_of_selected_items) == 2:
            a, b = list_of_selected_items 
            Link.LINKS.append(Link(a, b))


class Concept():
    
    WIDTH, HEIGHT, SPACING = 80, 20, 25
    MAX_W = 500
    C0, C1, C2 = MAX_W/4, MAX_W/2, 3*MAX_W/4 
    TEXT_SIZE = 9
    CONCEPTS = []
    Y_STACK = 0

    def __init__(self, content, x=None, y=None):
        self.under_mouse = False
        self.selected = False
        self.content = content
        if len(self.content) == 3:
            self.level = 0
            self.l0 = content
        elif len(self.content) == 7:
            self.level = 1
            self.l0 = content[:3]
            self.l1 = content[3:7]
        elif len(self.content) == 11:
            self.level = 2
            self.l0 = content[:3]
            self.l1 = content[3:7]
            self.l2 = content[7:]    
        else:
            self.level = None    
        
        if x == None:
            if self.level == 0:
                self.x = Concept.C0
            elif self.level == 1:
                self.x =  Concept.C1
            else:
                self.x =  Concept.C2
        else:
            self.x = x
        if y == None:
            Concept.Y_STACK += Concept.SPACING
            self.y = Concept.Y_STACK
        else:
            self.y = y
            

    def update(self):
        self.under_mouse = self.mouse_over()
        self.move()
        self.plot()
        

    def move(self):
        if self.selected and mousePressed:
            deltaX = mouseX - pmouseX
            deltaY = mouseY - pmouseY
            self.x += deltaX
            self.y += deltaY

    def plot(self):
        rectMode(CENTER)
        textAlign(CENTER, CENTER)
        textSize(Concept.TEXT_SIZE)
        strokeWeight(2)
        fill(200)
        if self.under_mouse:
            B = 0
        else:
            B = 255
        if self.selected:
            R = 255
        else:
            R = 0
        stroke(R, 0, B)
        # fill(200)
        rect(self.x, self.y, Concept.WIDTH, Concept.HEIGHT, Concept.HEIGHT / 4)
        fill(0)
        text(self.content, self.x, self.y)

    def mouse_over(self):
        return (self.x - Concept.WIDTH / 2 <= mouseX <= self.x + Concept.WIDTH / 2 and
                self.y - Concept.HEIGHT / 2 <= mouseY <= self.y + Concept.HEIGHT / 2)

    def relative_pos(self, ox, oy):
        """ compares self position with other (ox, oy) position"""
        if self.x - Concept.WIDTH <= ox <= self.x + Concept.WIDTH:
            rx = 10  # inside on x
        elif ox < self.x - Concept.WIDTH:
            rx = 0  # x to the left
        elif ox > self.x + Concept.WIDTH:
            rx = 20  # x to the right
        if self.y - Concept.HEIGHT <= oy <= self.y + Concept.HEIGHT:
            ry = 1  # inside on y
        elif oy < self.y - Concept.HEIGHT:
            ry = 0  # y is upwards
        elif oy > self.y + Concept.HEIGHT:
            ry = 2  # y is downwards
        return rx + ry

    def linking_point(self, other):
        rp = self.relative_pos(other.x, other.y)

        mpx = (self.x + other.x) / 2
        mpy = (self.y + other.y) / 2

        if rp < 10:
            px, py = self.x - Concept.WIDTH / 2, self.y
            cx, cy = mpx, self.y
        elif rp > 12:
            px, py = self.x + Concept.WIDTH / 2, self.y
            cx, cy = mpx, self.y
        else:
            if rp <= 11:
                px, py = self.x, self.y - Concept.HEIGHT / 2
            else:
                px, py = self.x, self.y + Concept.HEIGHT / 2
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

def leitura_tabela(nome_arquivo):
    import csv
    with open(nome_arquivo) as arquivo:
        tabela = []
        for linha in csv.reader(arquivo):
            #linha = unicode(linha.strip(), 'utf-8')
            #linha = [unicode(item.strip(), 'utf-8') for item in linha]
            tabela.append(linha[0])
    return tabela
