

class Bolinha():
    
    def __init__(self, x, y, tam, cor=color(255)):
        self.x = x
        self.y = y
        self.tam = tam
        self.cor = cor
        self.vx = random(-5, 5)
        self.vy = random(-5, 5)
   
    def update(self, lista_mae):
        self.move()
        self.show()
        if self.tam < 0:
            lista_mae.remove(self)
        self.tam = self.tam - 0.1
                          
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.x > width + self.tam:
            self.x = -self.tam
        if self.x < - self.tam:
            self.x = width + self.tam
        if self.y > height + self.tam:
            self.y = -self.tam
        if self.y <  -self.tam:
            self.y = height + self.tam
    
    def show(self):
        noStroke()
        fill(self.cor)
        circle(self.x, self.y, self.tam)
