particulas = [] # para por as partículas dentro

def setup():
    size(800, 800)
    no_stroke()
    background(0)

    
def draw():
    global x, y, vx, vy
#     background(0)
    for p in particulas.copy():
        p.atualiza()
        if p.d < 1:
            particulas.remove(p)
    print(len(particulas))
    
def key_pressed():
    if key == 's':
        save_frame('###.png')
    elif key == ' ':
        particulas.clear()
        background(0)
    
def mouse_dragged():
    diametro = random(10, 50)
    p = Particula(mouse_x, mouse_y, diametro)
    particulas.append(p)
    
class Particula:
    
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d
        self.vx = random(-3, 3)
        self.vy = random(-3, 3)
        self.cor = color(128, random(128, 255), 255, 200)

    def atualiza(self):
        self.vx = random(-1, 1) * self.d
        self.vy = random(-1, 1) * self.d
        self.desenha()
        self.move()
        self.d = self.d * 0.99
    def desenha(self):
        fill(self.cor)
        circle(self.x, self.y, self.d)
        
    def move(self):
        self.x += self.vx # self.x = self.x + self.vx
        self.y += self.vy
#         if self.x > width - self.d / 2:
#             self.vx = -self.vx
#         if self.x < self.d / 2:
#             self.vx = -self.vx
#         if self.y > height - self.d /2:
#             self.vy = -self.vy
#         if self.y < self.d / 2:
#             self.vy = -self.vy