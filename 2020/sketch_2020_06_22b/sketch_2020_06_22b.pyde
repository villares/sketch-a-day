
from particula import Particula

particulas = []
fontes = []

def setup():
    size(400, 400)
    for i in range(50):
        p = Particula(250, 250, random(18, 80))
        particulas.append(p)
        
def draw():
    background(0)
    for p in particulas:
        p.update()

def mouseDragged():
    nova_particula = Particula(mouseX, mouseY, 10)
    nova_particula.cor = color(255, 100)
    particulas.append(nova_particula)

def keyPressed():    
    particulas.pop()
    
    
    
