
pontos = []

def setup():
    size(500, 500)
    novos_pontos()
    
def novos_pontos():
    pontos[:] = []
    for _ in range(5):
        x, y = random(width * .2, width * .8), random(height * .2, height * .8)
        pontos.append((x, y))
    
def draw():
    background(240, 250, 250)
    for i, (x0, y0) in enumerate(pontos):
        x1, y1 = pontos[i - 1]
        curva(x0, y0, x1, y1)
    
def curva(x1, y1, x2, y2):
    """
    linha
    """
    L = dist(x1, y1, x2, y2)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        line(0, 0, 0, L)
        
def keyPressed():
    if key == ' ':
        novos_pontos()
