"""
sketch 42 180211a - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

LIST = []

def setup():
    size(512, 512)
    rectMode(CENTER)
    colorMode(HSB)
    strokeWeight(2)
    LIST.append(Cell(-width/4, -height/4, width/2))  # x, y, size

def draw():
    translate(width/2, height/2)
    background(255)
    for cell in LIST:
        cell.update()

def keyPressed():
    if key == " ":
        LIST[:] = [Cell(-width/4, -height/4, size=width/2)]

class Cell():

    def __init__(self, x=0, y=0, size=1):
        self.LIST = []
        self.x = x
        self.y = y
        self.size = size
        self.color = color(random(100, 200),200, 200, 100)

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
        offset = self.size/5
        x, y, new_size = self.x + offset, self.y+offset, self.size / 2
        if new_size > 0:
            self.LIST.append(Cell(x, y, new_size))
            self.LIST.append(Cell(x + new_size, y, new_size))
            self.LIST.append(Cell(x, y + new_size, new_size))
            self.LIST.append(Cell(x + new_size, y + new_size, new_size))

    def on_mouse(self):
        x, y = self.x + width/2, self.y + height/2
        print (x, y)
        if (x < mouseX < x + self.size and
            y< mouseY < y + self.size):
            return True
        # implícito (seria o else) Python retorna None que é considerado False