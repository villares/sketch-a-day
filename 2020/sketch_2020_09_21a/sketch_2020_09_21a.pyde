from ponto import Ponto

pontos = []
dragg = []

def setup():
    size(400, 400)
    for _ in range(20):
        pontos.append(Ponto(random(width),
                            random(height)))
        
def draw():
    background(200)
    
    if len(dragg) == 2:    
        line(dragg[0][0], dragg[0][1], mouseX, mouseY)
        
    for p in pontos:
        if len(dragg) == 2:
            if area(p, dragg[0], dragg[1]) > 0:
                p.f = color(255, 0, 0)
            else:
                p.f = color(0, 0, 255)
        else:
            p.f = 255
        p.draw()
        
                        
def mousePressed():
    dragg[:] = [(mouseX, mouseY)]
    
def mouseDragged():
    if len(dragg) == 1:
        dragg.append((mouseX, mouseY))
    else:
        dragg[1] = (mouseX, mouseY)

def area(p0, p1, p2):
    a = (p1[0] * (p2[1] - p0[1]) +
         p2[0] * (p0[1] - p1[1]) +
         p0[0] * (p1[1] - p2[1]))
    return a

def mouseReleased():
    dragg[:] = []
