from pvector_for_py5 import PVector

particles = []

def setup():
    size(400, 400)
    baclground(0)
    stroke_weight(5)
    for i in range(200):
        particles.append(Particle(random(width),random(height)))
     
def draw():
    no_stroke()
    fill(0, 10)
    rect(0, 0, width, height)
    mouse_pos = PVector(mouse_x, mouse_y)
    for p in particles:
        p.update(mouse_pos)

class Particle:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector(0, 0)  # PVector.random2D()

    def update(self, mouse_pos):
        delta = self.pos - mouse_pos
        d = delta.mag()
        if 0 < d < 50:
            delta.normalize()
            acel = delta * 0.01
            self.vel += acel
        self.pos += self.vel
        self.vel = self.vel * 0.995 # slow down
         
        stroke(max(0, 255 - d * 5,), 100, 100)    
        point(self.pos.x, self.pos.y)
        
        if self.pos.x < 0:
            self.pos.x = width
        elif self.pos.x > width:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = height
        elif self.pos.y > height:
            self.pos.y = 0 