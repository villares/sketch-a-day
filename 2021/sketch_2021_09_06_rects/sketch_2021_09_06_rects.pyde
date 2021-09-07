from random import randint

stands = []
letras = 'ABCDEFGHIJKLMNOPQRST'

def setup():
    size(800, 800)
    background(0, 0, 100)
    print(len(letras))
    translate(50, 0)
    for i, l in enumerate(letras):
        h1 = randint(15, 30)
        x = 0
        for n in range(60):
            h2 = randint(0, 5)
            h = h1 + h2
            w = randint(5, 15)
            a = w * h
            if i % 2 == 0:
                y = 35 + i * 39 -h
            else:
                y = i * 39 + 2
            fill(h * 10 - 100)
            rect(x, y, w, h)
            x += w
    
