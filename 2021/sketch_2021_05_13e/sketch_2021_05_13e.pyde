# You will need Processing Python mode to run this. Instructions at: https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/index-EN

from bola import Bolinha

bolinhas = []

def setup():
    size(600, 600)
    background(0)
      
def draw():
    # background(0)
    # blendMode(SUBTRACT)
    # fill(100, 100)
    # rect(0, 0, width, height)
    # blendMode(BLEND)
    for bola in reversed(bolinhas):
        bola.update(bolinhas)
    println(len(bolinhas))
    
def mouseDragged():
    nova_bola()

def keyPressed():
    background(0)
        
def nova_bola():
    dx = mouseX - pmouseX
    dy = mouseY - pmouseY
    nova_cor = color(0, 128, random(256), 32)           
    novo_tamanho = 0 # random(5, 30)
    nova_bola = Bolinha(mouseX, mouseY, novo_tamanho, nova_cor)
    nova_bola.vx = -dx * 1.2
    nova_bola.vy = -dy * 1.2
    nova_bola.tam = 10 + dx + dy  # overrides tamanho on this experiment
    bolinhas.append(nova_bola)

    
    
    
