def setup():
    size(600, 600)
    rect_mode(CENTER)
    no_fill()
    moldura_molnar(200, 100, 150)  # x, y, largura
    moldura_molnar(width / 2, height / 2, width * 0.80) 

def moldura_molnar(x, y, largura, reducao=None, n=5):
    reducao = reducao if reducao else largura / 5
    if n > 0:
        altura = largura / 2
        rect(x, y, largura, altura)
        nova_largura = largura - reducao
        moldura_molnar(x, y, nova_largura, reducao, n - 1)
    