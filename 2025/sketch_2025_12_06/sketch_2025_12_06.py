from itertools import product

import py5
from py5_tools import animated_gif

particles = []  

def setup():
    py5.size(800, 800)
    py5.color_mode(py5.CMAP, 'jet_r', 255)
    py5.background(255)
    #animated_gif('out.gif', duration=1/30, frame_numbers=range(1, 400, 2))

def draw():
    py5.fill(0, 10)
    #py5.rect(0, 0, py5.width, py5.height)
    for p in particles.copy():
        p.update()
    print(len(particles))
 
def mouse_dragged():
    if py5.frame_count % 2:
        particles.append(Particle(py5.mouse_x, py5.mouse_y))

def mouse_clicked():
    mouse_dragged()

def key_pressed():
    if py5.key == ' ':
        particles.clear()
        py5.background(255)
    elif py5.key == 'p':
        py5.save_frame('###.png')
    elif py5.key == 'r':
        for x, y in product(range(250, py5.width - 249, 150), repeat=2):
            for _ in range(4):
                particles.append(Particle(x, y, d=60))
 

class Particle:
    
    def __init__(self, x, y, d=None, v=None, h=None):
        self.pos = py5.Py5Vector(x, y)
        self.vel = v or py5.Py5Vector2D.random() * 2        
        self.d = d or py5.random(20, 50)
        self.h = h or py5.random_choice((-1, 1))
         
    def update(self):
        self.display()
        self.move()
        self.d = self.d * 0.99
        # random division
        if py5.random(1000) < 2:
            p = py5.random_choice((1, 0)) # simetrical branch or backwards 
            particles.append(
                Particle(
                    self.pos.x, self.pos.y,
                    d=self.d,
                    v=self.vel.copy if p else -self.vel.copy,
                    h=-self.h if p else self.h,
                )
            )
        # self removal
        if self.d < 1:
            particles.remove(self)
            
    def display(self):
        py5.no_stroke()
        py5.fill(py5.remap(self.d, 0, 60, 0, 255), 64)
        py5.circle(*self.pos, self.d)
    
    def move(self):
        self.pos += self.vel
        self.pos.x %= py5.width
        self.pos.y %= py5.height
        self.vel.rotate(py5.radians(2 * self.h))
        self.vel *= 0.995
        
py5.run_sketch(block=False)