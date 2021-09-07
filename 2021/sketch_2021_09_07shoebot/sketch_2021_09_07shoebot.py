from random import randint

letras = 'ABCDEFGHIJKLMNOPQRST'

def setup():
    size(800, 800)
    colorrange(255)
    background(0, 0, 100)
    stroke(0)
    strokewidth(0.5)
    print(len(letras))
    margin = 50
    translate(margin / 2, margin / 2)
    for i, l in enumerate(letras):
        h1 = randint(15, 30)
        n = x = 0
        while x < WIDTH - margin:
            n += 1
            h2 = randint(0, 5)
            h = h1 + h2
            w = randint(5, 15)
            if x + w > WIDTH - margin:
                w = (WIDTH - margin) - x
            a = w * h
            if i % 2 == 0:
                y = 35 + i * 38 - h
            else:
                y = i * 38 + 2
            fill(h * 10 - 100, a % 256, w * 16)
            #print((h * 10 - 100, a, w * 16))
            rect(x, y, w, h)
            x += w
    