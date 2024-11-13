import py5

D = 20
dragged = None  # None quer dizer nenhum elemento sendo arrastado
handles = [
    (100, 100),
    (200, 100),
    (200, 100),
    (200, 200),
    (150, 50),
    (150, 250),
    
    ]  # lista com coordenadas e tamanhos dos círculos
elements = [
    (0, 1),
    (2, 3),
    (4, 5),
    ]


def setup():
    py5.size(400, 400)
    py5.no_fill()
    

def draw():
    py5.background(150)
    py5.stroke_weight(3)
    for i, (x, y) in enumerate(handles):
        if i == dragged:
            py5.stroke(200, 0, 0)
        elif mouse_over(i):
            py5.stroke(0, 200, 0)
        else:
            py5.stroke(255)
        py5.circle(x, y, D)
    py5.stroke(0)
    for a, b in elements:
        py5.line(*handles[a], *handles[b])

def mouse_pressed():  # quando um botão do mouse é apertado
    global dragged
    # vamos olhar um círculo por vez da lista `handles`
    for i, (x, y) in enumerate(handles):  # i é o índice na lista
        if mouse_over(i):  # se o mouse estiver dentro
            dragged = i
            break  # interrompe o laço, não checa mais outros!

def mouse_over(i):
    return py5.dist(py5.mouse_x, py5.mouse_y, *handles[i])  < D / 2

        
        
def mouse_released():  # quando um botão do mouse é solto
    global dragged
    dragged = None

def mouse_dragged():  # quando o mouse é movido apertado
    if dragged is not None:
        x, y = handles[dragged]
        x += py5.mouse_x - py5.pmouse_x
        y += py5.mouse_y - py5.pmouse_y
        handles[dragged] = (x, y)

py5.run_sketch()