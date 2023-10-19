particles = []

def setup():
    size(800, 800)
#     for i in range(100):
#         p = Particle(300, 300)
#         particles.append(p)
    background(0)


def draw():
    fill(0, 10) # preenchiment preto translúcido
    #rect(0, 0, width, height) # placa translúcido
    for particle in particles:
        particle.update()
    print(len(particles))
    for particle in particles[:]:  #cópia da lista
        if particle.diameter < 0.5:
            particles.remove(particle)

def mouse_dragged():
    p = Particle(mouse_x, mouse_y)
    particles.append(p)

def key_pressed():
    background(0)

class Particle():
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random(-2, 2)
        self.vy = random(-2, 2)
        self.diameter = random(1, 25)
        
    def desenha(self):
        no_stroke()
        color_mode(HSB) # matiz, sat, brilho)
        fill(self.diameter * 10, 200, 200)
        vx, vy = self.vx, self.vy
        slow = (vx * vx + vy * vy) 
        circle(self.x, self.y,
               self.diameter * 1.5
               + self.diameter * sin(frame_count
                                    / slow)
                                    #/ self.diameter ** 2)
               )
        
    def anda(self):
        self.x = self.x + self.vx * self.diameter / 2
        self.y = self.y + self.vy * self.diameter / 2
         
    def limite(self):
#         if self.y > height or self.y < 0:
#             self.vy = -self.vy 
#         if self.x > width or self.x < 0:
#             self.vx = -self.vx
        if self.x > width:
            self.x = 0
        if self.x < 0:
            self.x = width
        if self.y > height:
            self.y = 0
        if self.y < 0:
            self.y = height
  
    def update(self):
        self.desenha()
        self.anda()
        self.limite()
        self.diameter = self.diameter * 0.995
        
        



