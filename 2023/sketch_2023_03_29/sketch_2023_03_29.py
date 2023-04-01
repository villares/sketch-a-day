# Trying to recreate this work by Vera Molnár:
# https://collections.vam.ac.uk/item/O1488630/print/

def setup():
    size(900, 450)
    rect_mode(CENTER)
    no_fill()
    
    largura = 70
    margem = (width - 10 * largura) / 2
    altura = largura / 2
    
    for j in range(10):
        for i in range(10): # 0, 1, 2, 3, ... 9
            x = i * largura + largura / 2 + margem
            y = j * altura + altura / 2 + margem / 2
            no_fill()
            moldura_molnar(x, y, largura * 0.90)
            fill(0)
            #text(str(x), x, y)
    
def moldura_molnar(x, y, largura):
    reducao = largura / 5
    altura = largura / 2
    for n in range(5):   # 0, 1, 2, 3, 4
        rect(x, y, largura, altura)
        largura = largura - reducao
        altura = altura - (reducao / 2)