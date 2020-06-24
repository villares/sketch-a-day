
class Particula:

    def __init__(self, x, y, tam=40):
        self.fade = 255
        self.x = x
        self.y = y
        self.vx = random(-3, 3)
        self.vy = random(-3, 3)
        self.tam = tam
        self.cor = color(random(100, 200),
                             random(100, 200),
                             random(100, 200))

    def update(self):
        self.desenha()
        self.move()
        if (frameCount % 10 == 0 and 
            self.fade > 100):
            self.fade -= 1
            
    def desenha(self):
        noStroke()
        fill(color(self.cor, self.fade))
        textSize(20)
        textAlign(CENTER, CENTER)
        # text(self.txt, self.x, self.y)
        ellipse(self.x, self.y, self.tam, self.tam)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if (self.x < self.tam / 2 or
            self.x > width - self.tam / 2):
            self.vx = -self.vx


        if self.y < -self.tam / 2:
            self.y = height + self.tam / 2
        if self.y > height + self.tam / 2:
            self.y = -self.tam / 2
