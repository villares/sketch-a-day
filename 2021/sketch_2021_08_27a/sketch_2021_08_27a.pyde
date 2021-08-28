add_library('peasycam')

GRID_SIZE = 16

def setup():
    global spacing
    size(400, 400, P3D)
    border = 20
    spacing = (height - border * 2) / GRID_SIZE
    Ponto.spacing = spacing
    for j in range(GRID_SIZE):
        for i in range(GRID_SIZE):
            Ponto.pontos.append(Ponto(border + spacing / 2 + i * spacing,
                                      border + spacing / 2 + j * spacing)
                                )
    cam = PeasyCam(this, 400)
    
def draw():
    background(200)
    translate(-width / 2, -height / 2) 
    for i in range(GRID_SIZE):
        translate(0, 0, 5)
        for p in Ponto.pontos:
            p.update()
    
class Ponto():
    pontos = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.px = x
        self.py = y

    def update(self):
        rx = random(-0.5, 0.5)
        ry = random(-0.5, 0.5)
        if abs(self.px + rx - self.x) < Ponto.spacing * 0.33:
            self.px += rx
        if abs(self.py + ry - self.y) < Ponto.spacing * 0.33:
            self.py += ry
        self.plot()

    def plot(self):
        for p in Ponto.pontos:
            d = dist(p.px, p.py, self.px, self.py)
            if  Ponto.spacing * .9 <= d <= Ponto.spacing * 1.05:
                stroke(0)
                line(p.px, p.py, self.px, self.py)
            elif  d < Ponto.spacing * 0.9:
                stroke(255)    
                line(p.px, p.py, self.px, self.py)
        fill(128, 0 ,0)
        noStroke()
        ellipse(self.px, self.py, 4, 4)
