

def setup():
    size(500, 500)
    d = 10
    vezes = 50
    for i in range(vezes):  # 0, 1, ... vezes - 1
        x = i * d + d / 2
        circle(x, 100, d)
        line(x, 100, x, 400)
    for i in range(vezes):  # 0, 1, ... vezes - 1
        x = i * d + d / 2
        line(x, 100, x * 2, 400)
    save('saida.png')    
  