particulas = []

def setup():
    size(900, 900)
    background(0)
#     for _ in range(100):
#         p = Particula(width / 2, height / 2)
#         particulas.append(p)
    
def draw():
    #background(0)
    for i, p in reversed(list(enumerate(particulas))):
        p.update()
        if p.tam <= 0:
            del particulas[i]
    #print(len(particulas))
        
def mouse_dragged():
    particulas.append(Particula(mouse_x, mouse_y))

class Particula:
    
    def __init__(self, x, y, tam=None):
        self.pos = Py5Vector(x, y)
        self.vel = Py5Vector.random(dim=2) * random(1, 5)
        self.tam = tam or random(10, 50)
        
    def update(self):
        self.tam -= 0.5
        self.display()
        self.move()
        
    def display(self):
        no_stroke()
        fill(255, 32)
        circle(self.pos.x, self.pos.y, self.tam)
        
    def move(self):
        self.pos += self.vel
