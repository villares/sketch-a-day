from bola import Bolinha

bolinhas = []

def setup():
    size(600, 600)
    background(0)
    for i in range(10):     
        nova_cor = color(random(256), random(256), 255, 100)           
        novo_tamanho = random(5, 30)
        nova_bola = Bolinha(300, 300, novo_tamanho, nova_cor)
        bolinhas.append(nova_bola)
      
def draw():
    # background(0)
    fill(0, 10) # preto muito transparente
    rect(0, 0, width, height)
    for bola in reversed(bolinhas):
        bola.update(bolinhas)
    println(len(bolinhas))
    
def mouseDragged():
    nova_bola()
    
def mousePressed():
    nova_bola()
        
def nova_bola():
    nova_cor = color(random(256), random(256), 255, 100)           
    novo_tamanho = random(5, 30)
    nova_bola = Bolinha(mouseX, mouseY, novo_tamanho, nova_cor)
    bolinhas.append(nova_bola)

    
    
    
