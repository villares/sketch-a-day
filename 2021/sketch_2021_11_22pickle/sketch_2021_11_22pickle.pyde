import pickle 

gestos = [[]]

def setup():
    size(500, 200)
    colorMode(HSB) # matiz/Hue, Saturation, Brightness
    strokeWeight(3)
    
def draw():
    background(0)
    noFill()
    strokeWeight(6 + 5 * sin(frameCount / 10.0))
    for i, poligono in enumerate(gestos):
        stroke((i * 32 % 255), 255, 255) 
        beginShape()
        for x, y in poligono:      
            vertex(x, y)
        endShape()
         
def mouseDragged():
    ultimo_gesto = gestos[-1]
    ponto = (mouseX, mouseY)
    ultimo_gesto.append(ponto)
    
def mouseReleased():
    gestos.append([])
    
def keyPressed():
    if key == ' ':
        gestos[:] = [[]]
    elif str(key) in '!@#$%':
        k = '12345'['!@#$%'.find(key)]
        salva_dados(k)
    elif str(key) in '12345':
        carrega_dados(key)
        
def salva_dados(k):
    # open com modo "w" (write, escrita)
    with open('gestos{}.dados'.format(k), 'w') as arquivo:
        pickle.dump(gestos, arquivo)
    print('dados salvos em "gestos.dados"')
    
def carrega_dados(k):
    global gestos
    try:
        with open('gestos{}.dados'.format(k)) as arquivo:
            gestos = pickle.load(arquivo)
    except IOError:
        print(u'não tem esse arquivo')
        
