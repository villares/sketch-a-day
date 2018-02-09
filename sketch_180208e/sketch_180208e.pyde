
LIST = []

def setup():
    size(512, 512)
    ellipseMode(CORNER)
    noStroke()
    LIST.append(Cell(size=width))

def draw():
    background(0)
    for cell in LIST:
        cell.update()


class Cell():

    def __init__(self, x=0, y=0, size=1):
        self.LIST = []
        self.x = x
        self.y = y
        self.size = size
        self.color = color(random(256))

    def update(self):
        self.draw()
        if not self.LIST:
            if mousePressed and self.on_mouse():
                self.divide()
        else:
            for sq in self.LIST:
                    sq.update()

    def draw(self):
        fill(self.color)
        if keyPressed:
           ellipse(self.x, self.y, self.size, self.size)
        else:
            rect(self.x, self.y, self.size, self.size)

    def divide(self):
        x, y, new_size = self.x, self.y, self.size / 2
        if new_size > 2:
            self.LIST.append(Cell(x, y, new_size))
            self.LIST.append(Cell(x + new_size, y, new_size))
            self.LIST.append(Cell(x, y + new_size, new_size))
            self.LIST.append(Cell(x + new_size, y + new_size, new_size))

    def on_mouse(self):
        if (self.x < mouseX < self.x + self.size and
                self.y < mouseY < self.y + self.size):
            return True
