
circulos = []  # uma lista vazia
tam_min = 2
tam_max = 130


def setup():
    size(600, 400)
    colorMode(HSB)
    noStroke()
          
              
def draw():
    background(0)
    for x, y, t in circulos:
        fill(t * 2 - 4, 255, 255)
        circle(x, y, t)
        
    tamanho, x, y = -1, 0, 0
    while colisao(x, y, tamanho):
        tamanho = random(tam_min, tam_max)
        x = random(tamanho / 2, width - tamanho / 2)
        y = random(tamanho / 2, height - tamanho / 2)
    circulos.append((x, y, tamanho))
    print(tamanho) 
            
                                                    
def colisao(x, y, tamanho):
        if tamanho < 0:
            return True
        for xc, yc, tamanho_c in circulos:
            if dist(x, y, xc, yc) < tamanho / 2 + tamanho_c / 2:
                 return True
        return False
            
            
def keyPressed():
    if key == ' ':
        circulos[:] = []
    if key == 'p':
        saveFrame('######.png')
            
