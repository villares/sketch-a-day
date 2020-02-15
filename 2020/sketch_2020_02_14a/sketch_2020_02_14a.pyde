gestos = [] # lista de gestos
gesto = []  # lista de pontos, tuplas (x, y)
select_gesto = -1 # -1 significa nenhum gesto selecionado

def setup():
    size(500, 500)
    noFill()
    strokeWeight(5)
    
def draw():
    background(200)
    for i, gesto in enumerate(gestos):
        if i == select_gesto:
            stroke(200, 0, 0)
        else:
            stroke(0)
        # beginShape()
        # for p in gesto:        
        #     vertex(p[0], p[1])
        # endShape()
        
        # lista[-1] é o último item de uma lista
        # lista[a:b] é do item [a] até o item [b-1]
        # lista[:-1] é do começo até o penúltimo item de uma lista
        # lista[1:] é a partir do segundo até o final
        for p, pp in zip(gesto[:-1], gesto[1:]):
            lw = 5 + 5 / (1 + dist(p[0], p[1], pp[0], pp[1]))
            strokeWeight(lw)        
            line(p[0], p[1], pp[0], pp[1])
        
def mousePressed():
    global select_gesto
    if keyPressed and keyCode == SHIFT:
        for i, gesto in enumerate(gestos):
            for x, y in gesto:
                if dist(x, y, mouseX, mouseY) < 10:
                    select_gesto = i
                    return
        select_gesto = -1 # deixa nenhum gesto selecionado
    
def mouseDragged():
    gesto.append((mouseX, mouseY))
    
def mouseReleased():
    novo_gesto = gesto[:] # cria uma cópia
    gestos.append(novo_gesto)
    gesto[:] = [] # esvazia a lista gesto original
    
def keyPressed():
    if key == ' ':
        gestos[:] = [] # esvazia a lista gestos    
