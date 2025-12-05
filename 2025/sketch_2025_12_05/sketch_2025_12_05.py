from itertools import product

import py5
from py5_tools import animated_gif


particles = []  

def setup():
    py5.size(800, 800)
    py5.color_mode(py5.CMAP, 'cividis', 255)
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
        for x, y in product(range(200, py5.width - 199, 200), repeat=2):
            for _ in range(1):
                particles.append(Particle(x, y, d=60))
 

class Particle:
    
    def __init__(self, x, y, d=None, v=None, h=None):
        self.pos = py5.Py5Vector(x, y)
        self.vel = v or py5.Py5Vector2D.random() * 2        
        self.d = d or py5.random(20, 50)
        self.handedness = h or py5.random_choice((-1, 1))
         
    def update(self):
        if py5.random(100) < 1:
             particles.append(
                 Particle(self.pos.x, self.pos.y,
                          d=self.d,
                          v=-self.vel,#.rotate(py5.HALF_PI),
                          h=self.handedness
                          )
                 )
        if self.d < 1:
            particles.remove(self)
        self.display()
        self.move()
        self.d = self.d * 0.99



    def display(self):
        py5.no_stroke()
        py5.fill(py5.remap(self.d, 0, 60, 0, 255), 64)
       # py5.fill(self.cor, py5.random(200, 255))
        py5.circle(*self.pos, self.d)
    
    def move(self):
        self.pos += self.vel
        self.pos.x %= py5.width
        self.pos.y %= py5.height
        self.vel.rotate(py5.radians(2 * self.handedness))
        self.vel *= 0.995
        
py5.run_sketch(block=False)
