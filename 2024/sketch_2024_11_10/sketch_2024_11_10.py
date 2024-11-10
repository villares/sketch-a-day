particulas = [] # para por as partículas dentro

def setup():
    size(800, 800)
    no_stroke()
    color_mode(HSB)
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
    diametro = random(10, 30)
    p = Particula(mouse_x, mouse_y, diametro)
    particulas.append(p)
    
class Particula:
    
    def __init__(self, x, y, d):
        self.pos = Py5Vector(x, y)
        self.d = d
        self.hue = random(128, 255)
        self.sat = random(128, 255)

    def atualiza(self):
        ang = radians(random_int(2) * 120)
        self.v = Py5Vector2D.from_heading(ang) * self.d
        self.pos += self.v
        self.d = self.d * 0.995
        fill(color(self.hue, self.sat, 200 - self.d * 5, 200))
        circle(self.pos.x, self.pos.y, self.d)