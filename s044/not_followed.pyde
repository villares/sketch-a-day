"""
sketch 44 180213b - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

LIST = []

def setup():
    size(512, 512)
    rectMode(CENTER)
    colorMode(HSB)
    strokeWeight(2)
    # x, y, size
    LIST.append(Cell(size=width * .66))

def draw():
    translate(width / 2, height / 2)
    background(255)
    for cell in LIST:
        cell.update()

def keyPressed():
    if key == " ":
        LIST[:] = [Cell(size=width * .66)]

class Cell():

    def __init__(self, x=0, y=0, size=1):
        self.LIST = []
        self.x = x
        self.y = y
        self.size = size
        self.color = color(random(0, 128), 200, 200, 100)

    def update(self):
        self.draw()
        if not self.LIST:  # para listas vazias (células sem sub-células)
            if mousePressed and self.on_mouse():
                self.divide()
        else:  # senão update as sub-células!
            for cell in self.LIST:
                cell.update()
                stroke(0)
                line(self.x, self.y, cell.x, cell.y)

    def draw(self):
        noStroke()
        fill(self.color)
        if keyPressed:
            ellipse(self.x, self.y, self.size, self.size)
        else:
            rect(self.x, self.y, self.size, self.size)

    def divide(self):
        x, y, new_size = self.x, self.y, self.size *.50
        o = self.size * 0.50
        if new_size > 5:
            self.LIST.append(Cell(x + o, y + o, new_size))
            self.LIST.append(Cell(x + o, y - o, new_size))
            self.LIST.append(Cell(x - o, y + o, new_size))
            self.LIST.append(Cell(x - o, y - o, new_size))
            self.LIST.append(Cell(x, y - o, new_size))
            self.LIST.append(Cell(x, y + o, new_size))
            self.LIST.append(Cell(x - o, y, new_size))
            self.LIST.append(Cell(x + o, y, new_size))
            self.size = new_size


    def on_mouse(self):
        x, y = self.x + width / 2, self.y + height / 2
        r = self.size / 2
        if (x - r < mouseX < x + r and
            y - r < mouseY < y + r):
            return True
        