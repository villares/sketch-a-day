from pvector_for_py5 import PVector
import py5

particles = []

def setup():
    py5.size(400, 400)
    py5.background(0)
    py5.smooth()
    py5.stroke_weight(4)
    for i in range(200):
        p = Particle(py5.width / 2, py5.height / 2)
        p.vel = PVector.random2D()
        particles.append(p)
     
def draw():
    py5.no_stroke()
    py5.fill(0, py5.random(4, 16))
    py5.rect(0, 0, py5.width, py5.height)
    mouse_pos = PVector(py5.mouse_x, py5.mouse_y)
    for p in particles:
        p.update(mouse_pos)

class Particle:
    def __init__(self, x, y):
        self.pos = PVector(x, y)
        self.vel = PVector()

    def update(self, mouse_pos):
        delta = self.pos - mouse_pos
        d = delta.magSq()
        if 0 < d < 2500:
            self.vel +=  delta.normalize() * 0.05
        self.pos += self.vel
        self.vel = self.vel * 0.995 # slow down
        v_mag = self.vel.magSq()
        r, g, b = max(0, 255 - d / 50,), min(200, v_mag * 255), 200
        py5.stroke(r, g, b)
        py5.point(self.pos.x, self.pos.y)
        
        if self.pos.x <= 0 or self.pos.x >= py5.width:
            self.vel.x = -self.vel.x
        if self.pos.y <= 0 or self.pos.y >= py5.height:
            self.vel.y = -self.vel.y
            
py5.run_sketch()