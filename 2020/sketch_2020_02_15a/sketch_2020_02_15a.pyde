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
        # lista[-1] é o último item de uma lista
        # lista[a:b] é do item [a] até o item [b-1]
        # lista[:-1] é do começo até o penúltimo item de uma lista
        # lista[1:] é a partir do segundo até o final
        for p, pp in zip(gesto[:-1], gesto[1:]):
            lw = 1 + 5 / (1 + dist(p[0], p[1], pp[0], pp[1]))
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
    if not keyPressed:
        gesto.append((mouseX, mouseY))
    if key == 'm':
        if select_gesto >= 0:
            dx = mouseX - pmouseX
            dy = mouseY - pmouseY
            sel_gesto = gestos[select_gesto]
            for i, (x, y) in enumerate(sel_gesto):
                sel_gesto[i] = (x + dx, y + dy)
                
    
def mouseReleased():
    novo_gesto = gesto[:] # cria uma cópia
    gestos.append(novo_gesto)
    gesto[:] = [] # esvazia a lista gesto original
    
def keyPressed():
    global select_gesto
    if key == 's':
        saveFrame("####.png")
    if key == ' ':
        gestos[:] = [] # esvazia a lista gestos 
          
    if key == 'r' and select_gesto >= 0:
        gestos.pop(select_gesto)
        select_gesto = -1
        
    if key == 'd' and select_gesto >= 0:
        new_gesto = gestos[select_gesto][:]
        for i, (x, y) in enumerate(new_gesto):
            new_gesto[i] = (x + 20, y + 20)
        gestos.append(new_gesto)
        select_gesto = len(gestos) - 1
        
    if key == 'z' and len(gestos) > 0:
        gestos.pop() # apaga o último gesto
        
