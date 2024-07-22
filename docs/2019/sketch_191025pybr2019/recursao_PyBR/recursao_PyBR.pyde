
def setup():
    size(500, 500)
 
def draw():
    background(240, 240, 200)
    translate(250, 300)
    galho(60)
    
def galho(tamanho):
    ang = radians(mouseX)
    encurtar = .8
    line(0, 0, 0, -tamanho)  
    if tamanho > 5:
        translate(0, -tamanho)
        rotate(ang)
        galho(tamanho * encurtar)  
        rotate(2 * -ang)
        galho(tamanho * encurtar) 
        rotate(ang)
        translate(0, tamanho)
    
