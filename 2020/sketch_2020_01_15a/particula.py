# Author: Berin
# Sketches repo: https://github.com/berinhard/sketches
# berin lib: https://github.com/berinhard/berin/
class Particula(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.raio = random(50, 60)
        self.angulo = random(TWO_PI)
        self.angulo_inc = random(TWO_PI / 36)
        self.raio_inc = random(1, 6)

    def atualize(self):
        self.color = color(250, random(50, 100), 50)
        self.raio -= self.raio_inc
        self.angulo += self.angulo_inc
        self.x += random(-5, 2)
        self.y += random(-2, 5)
        
    def desenha(self):
        if self.raio > 0:
            with pushMatrix():
                translate(self.x, self.y)
                rotate(self.angulo)
                fill(self.color)
                ellipse(0, 0, self.raio, self.raio)
