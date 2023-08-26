from random import choice, sample, seed

cores = [color(50, 50, 50), color(130, 100, 100)    ]

def setup():
    size(800, 800)
    no_loop()
    no_stroke()

def predio(x, y, w):
    c, c2 = sample(cores, 2)
    n = choice((3, 4, 6))
    h = n * w
    fill(c)
    rect(x, y + w - h , w, h)
    for j in range(n):
        jy = j * -w
        for i in range(n // 2):
            #stroke(0)
            fill(choice((c2, color(255, 255, 0))))
            square(x + 2 + i * w / n, y + jy + 2, w / n - 3)


def draw():
    #seed(1)
    #random_seed(1)
    background(0)
    fill(0, 50, 0)
    for x in range(10):    
        rect(x * width / 10, random(height / 3, height / 2),
             width / 10, height /  2)
#    predio(100, 300, 30) 
#    predio(200, 300, 30)
    n = 20
    w = width / n  # n 10 -> w 40
    for j in range(n):
        y = 100 + w / 2 + j * w 
        for i in range(n * 20):   # 0, 1, 2 ... 9
            x = w / 2 + i * w / (10 - j / 10) + random(-w / 2, w / 2)
            predio(x, y, random(w / 2, w) - 2 * (10 - j))

def key_pressed():
    redraw()