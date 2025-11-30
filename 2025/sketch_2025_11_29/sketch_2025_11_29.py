import py5

particles = []  

def setup():
    global b
    py5.size(800, 800)
    py5.background(0)
    py5.color_mode(py5.CMAP, 'viridis', 255)
  
def draw():
    py5.fill(0, 10)
    #py5.rect(0, 0, py5.width, py5.height)
    for p in particles.copy():
        p.update()
    print(len(particles))
 
def mouse_dragged():
    if py5.frame_count % 2:
        particles.append(Particle(py5.mouse_x, py5.mouse_y))

def key_pressed():
    if py5.key == ' ':
        particles.clear()
        py5.background('k')
    elif py5.key == 'p':
        py5.save_frame('###.png')

class Particle:
    
    def __init__(self, x, y):
        self.pos = py5.Py5Vector(x, y)
        self.vel = py5.Py5Vector2D.random() * 2        
        self.d = py5.random(20, 50)
        self.handedness = py5.random_choice((-1, 1))
         
    def update(self):
        self.display()
        self.move()
        self.d = self.d * 0.99
        if self.d < 1:
            particles.remove(self)
        
    def display(self):
        py5.no_stroke()
        py5.fill(py5.remap(self.d, 0, 50, 0, 255), 32)
       # py5.fill(self.cor, py5.random(200, 255))
        py5.circle(*self.pos, self.d)
    
    def move(self):
        self.pos += self.vel
        self.pos.x %= py5.width
        self.pos.y %= py5.height
        self.vel.rotate(py5.radians(2))
        self.vel *= 0.99
        
py5.run_sketch(block=False)
