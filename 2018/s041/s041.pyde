"""
sketch 41 180210a - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day
"""

LIST = []

def setup():
    size(512, 512)
    ellipseMode(CORNER)
    noStroke()
    colorMode(HSB)
    strokeWeight(2)
    LIST.append(Cell(size=width))  # repare no "named argument"

def draw():
    background(255)
    for cell in LIST:
        cell.update()

def keyPressed():
    if key == " ":
        LIST[:] = [Cell(size=width)]

class Cell():
    # os parâmetros default servem também de "named arguments"

    def __init__(self, x=0, y=0, size=1):
        self.LIST = []
        self.x = x
        self.y = y
        self.size = size
        self.color = color(random(100, 200),200, 200)

    def update(self):
        self.draw()
        if not self.LIST:  # para listas vazias (células sem sub-células)
            if mousePressed and self.on_mouse():
                self.divide()
        else:  # senão update as sub-células!
            for cell in self.LIST:
                cell.update()

    def draw(self):
        fill(self.color)
        if keyPressed:
            ellipse(self.x, self.y, self.size, self.size)
        else:
            rect(self.x, self.y, self.size, self.size)

    def divide(self):
        x, y, new_size = self.x+2, self.y+2, self.size / 2 -2
        if new_size > 0:
            self.LIST.append(Cell(x, y, new_size))
            self.LIST.append(Cell(x + new_size, y, new_size))
            self.LIST.append(Cell(x, y + new_size, new_size))
            self.LIST.append(Cell(x + new_size, y + new_size, new_size))

    def on_mouse(self):
        if (self.x < mouseX < self.x + self.size and
                self.y < mouseY < self.y + self.size):
            return True
        # implícito (seria o else) Python retorna None que é considerado False