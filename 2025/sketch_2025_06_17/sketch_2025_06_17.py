
bolinhas = []  # lista que começa vazia
#gravidade = Py5Vector(0, 0.1)

def setup():
    size(800, 400)
    # enchendo a lista de bolinhas    
#     for _ in range(100): # 0 até 99 
#         b = Bolinha(random(50, width - 50), random(50, height - 50))
#         bolinhas.append(b)
    print(len(bolinhas))
    background(0)

def draw():
    #fill(0, 10)
    #rect(0, 0, width, height)
    # atualizando as bolinhas
    for bola in bolinhas.copy():
        bola.atualizar()
        if bola.diametro < 1:
            bolinhas.remove(bola)
        
    print(len(bolinhas))
    
def mouse_dragged():
    b = Bolinha(mouse_x, mouse_y)
    bolinhas.append(b)
    
def key_pressed():
    if key == ' ':
        background(0)
        bolinhas.clear()
    elif key == 's':
        save_frame('###.png')
        
class Bolinha:
    
    def __init__(self, x, y):
        self.pos = Py5Vector(x, y)
        self.diametro = 50 #random(3, 51)
        self.vel = Py5Vector.random(2) * 0.5
        #self.cor = color(random(255), random(255), random(255))
        
    def atualizar(self):
        self.desenhar()
        self.mover()
        self.diametro = self.diametro * 0.99
        #self.vel = self.vel + gravidade
        
    def desenhar(self):
        no_stroke()
        #color_mode(HSB)  # Hue/Matiz, Sat, Bri
        fill(self.diametro * 5, 255, 255, 100)
        circle(self.pos.x, self.pos.y, self.diametro)
        
    def mover(self):
        self.vel *= 0.99
        self.vel += Py5Vector.random(2) * 0.5
        self.pos += self.vel
        
        self.pos.x %= width
        self.pos.y %= height
        


