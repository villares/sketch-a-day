particles = []  # lista que começa vazia
#gravidade = Py5Vector(0, 0.1)

def setup():
    size(800, 400)
    background(4)

def draw():
    fill(0, 10)
    rect(0, 0, width, height)
    # best to iterate over a copy here!
    for p in particles.copy(): 
        p.update()
        
    print(len(particles))
    
def mouse_dragged():
    p = Particle(mouse_x, mouse_y)
    particles.append(p)
    
def key_pressed():
    if key == ' ':
        background(0)
        particles.clear()
    elif key == 's':
        save_frame('###.png')
        
class Particle:
    
    def __init__(self, x, y):
        self.pos = Py5Vector(x, y)
        self.dia = 50 #random(3, 51)
        self.vel = Py5Vector.random(2) * 0.5
        #self.cor = color(random(255), random(255), random(255))
        
    def update(self):
        self.draw()
        self.move()
        self.dia = self.dia * 0.99
        if self.dia < 1:
            particles.remove(self)
            
    def draw(self):
        no_stroke()
        color_mode(HSB)  # Hue/Matiz, Sat, Bri
        fill(self.dia * 5, 255, 255, 100 - 2 * self.dia)
        circle(self.pos.x, self.pos.y, self.dia)
        
    def move(self):
        self.vel *= 0.95
        self.vel += Py5Vector.random(2) * 0.5
        self.pos += self.vel
        
        self.pos.x %= width
        self.pos.y %= height
        


