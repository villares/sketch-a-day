balls = []

def setup():
    size(700, 700)
    color_mode(HSB)
    background(0)
    
def draw():
    fill(10, random(20, 40))
    rect(0, 0, width, height)
    #background(0)
    for b in balls[:]:
        b.update()
        if b.size < 1:
            balls.remove(b)
#     if balls:
#         print(balls[-1].size)  # speed of the last ball
#     print(len(balls))  # number of balls in list

def mouse_dragged():
    b = Ball(mouse_x, mouse_y)
    balls.append(b)
 
class Ball:
    
    def __init__(self, x, y):
        self.p = Py5Vector(x, y)
        self.v = Py5Vector.random(2) * random(1, 5)
        self.size = random(5, 32)
        
    def update(self):
        self.draw()
        self.move()
        self.bounce()
        self.size = self.size * 0.98

    def draw(self):
        no_stroke()
        fill(self.size * 8, 200, 200)
        circle(self.p.x, self.p.y, self.size)

    def move(self):
        self.p += self.v
        self.v.y += 0.05 # gravity
        
    def bounce(self):
        if self.p.x >= width or self.p.x < 0:
            self.v.x = -self.v.x * 0.70
        if self.p.y >= height or self.p.y < 0:
            self.v.y = -self.v.y * 0.70