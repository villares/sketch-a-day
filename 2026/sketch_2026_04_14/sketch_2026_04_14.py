# This is a py5 "imported mode" sketch
# you'll need py5-run-sketch tool or the thonny-py5mode plug-in on Thonny
# learn about py5 modes at https://py5coding.org

bolinhas = []

def setup():
    global ba, bb
    size(600, 600)
    background(200, 100, 100)
#     for i in range(50):
#         b = Bolinha(300, 300)
#         bolinhas.append(b)
        
def draw():
    # fill(200, 100, 100, random(1, 15))  # r, g, b, opacidade (alpha)
    # rect(0, 0, width, height) 
    
    for bolinha in bolinhas.copy():
        bolinha.atualizar()
        if bolinha.diametro < 1:
            bolinhas.remove(bolinha)
    print(len(bolinhas))

def mouse_dragged():
    bolinhas.append(Bolinha(mouse_x, mouse_y))

class Bolinha:
        
    def __init__(self, x, y):
        # atributos x, y, d, vx, vy
        self.x = x
        self.y = y
        self.diametro = random(10, 50)
        self.vx = random(-3, 3)
        self.vy = random(-3, 3)
        self.cor = color(random(128), random(128), 255) 
    # métodos desenhar e mover
    
    def atualizar(self):
        self.desenhar()
        self.mover()
        self.diametro = self.diametro * 0.98
        
    
    def desenhar(self):
        no_stroke()
        fill(self.cor)
        circle(self.x, self.y, self.diametro)
        
    def mover(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        if self.y > height - self.diametro / 2:  # rebate em baixo
            self.vy = -self.vy # inverte velocidade y
        if self.y < self.diametro / 2: # rebatem em cima
            self.vy = -self.vy   # inverte velocidade y
        if self.x > width + self.diametro / 2: # saída à direita
            self.x = -self.diametro / 2  # volta à esquerda
        if self.x < -self.diametro / 2:   # saída à esquerda
            self.x = width + self.diametro / 2  # volta à direita


    

