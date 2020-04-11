# Ao iterarmos por uma sequência, pode ser útil obter
# ao mesmo tempo que o item, o índice do item na sequência.
# Isso é chamado de enumeração, e usamos a função enumerate()
# Veja um exemplo:
    
def setup():
    size(400, 400)
    pontos = [(50, 50), (300, 370), (200, 50), (150, 150)]
    for i, (x, y) in enumerate(pontos):
        fill(255)
        ellipse(x, y, 5 + i * 5, 5 + i * 5)
        label = "{}: {}, {}".format(i, x, y)
        fill(0)
        text(label, x + 15, y)
        
    saveFrame("enumerate.png")
