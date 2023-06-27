import py5
from py5 import random, random_seed

s = 1

def setup():
    py5.size(1000, 1000)
    py5.fill(0)
    py5.text_font(py5.create_font('Consolas Bold', 20))
    
def draw():
    py5.background(240)
    py5.text('random(1)                 '
             'random(1) * random(1)    '
             'random(1) ** 2',
         100, 50)
    random_seed(s)
    rs =(
        a := [random(1) for _ in range(100)],
        sorted(a),
        b := [random(1) * random(1) for _ in range(100)],
        sorted(b),
        c := [random(1) ** 2 for _ in range(100)],
        sorted(b)
    )
    
    py5.stroke(200, 0, 0)
    for j in range(21):
        for k in range(3):
            py5.line(100 + k * 283.4, 100 + 40 * j, 333.4 + k * 283.4, 100 + 40 * j)   
    py5.stroke(0)
    x = 100
    for i, r in enumerate(rs):
        bucket = {i: 0 for i in range(10)}
        for n in r:
            y = n * 400
            bucket[int(n * 10)] += 1
            py5.line(x, 500, x, 500 - y)
            x += 1
        if i % 2 == 0:
            for b in range(10):
                py5.rect(x - 100, (9 - b) * 40 + 510, bucket[b] * 5, 30)
            x += 33.4
        else:
            x += 50

def key_pressed():
    global s
    s += 1

py5.run_sketch()
