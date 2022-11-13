bolinhas = []

def setup():
    size(700, 700)
    color_mode(HSB)
    background(0)
    
def draw():
    fill(random(0, 25), random(20, 40))
    rect(0, 0, width, height)
    #background(0)
    for b in bolinhas[:]:
        b.update()
        if b.tamanho < 1:
            bolinhas.remove(b)
    if bolinhas:
        print(bolinhas[-1].tamanho)
    print(len(bolinhas))  # exibe numero de bolinhas na lista
 
def mouse_dragged():
    b = Bolinha(mouse_x, mouse_y)
    bolinhas.append(b)
 
class Bolinha:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random(-3, 3)
        self.vy = random(-3, 3)
        self.tamanho = random(5, 30)
        
    def update(self):
        #if self.tamanho > 1:
            self.draw()
            self.move()
            self.bounce()
            self.tamanho = self.tamanho * 0.97

    def draw(self):
        no_stroke()
        fill(self.tamanho * 8, 200, 200)
        circle(self.x, self.y, self.tamanho)

    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.vy = self.vy + 0.05
        
    def bounce(self):
        if self.x >= width or self.x < 0:
            self.vx = -self.vx * 0.70
        if self.y >= height or self.y < 0:
            self.vy = -self.vy * 0.70