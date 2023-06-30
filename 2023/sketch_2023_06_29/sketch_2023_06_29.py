import py5
from py5 import random, random_seed

s = 10
N = 200


def setup():
    py5.size(1000, 500)
    py5.fill(0)
    py5.text_font(py5.create_font('Source Code Pro', 40))
    py5.color_mode(py5.HSB)
    
def draw():
    py5.scale(0.5)
    py5.background(240)
    py5.fill(0)
    py5.text('random(1)              '
             'random(1) * random(1)   '
             'random(1) ** 2',
         100, 50)
    random_seed(s)
    rs =(
        a := [random(1) for _ in range(N)],
        sorted(a),
        b := [random(1) * random(1) for _ in range(N)],
        sorted(b),
        c := [random(1) ** 2 for _ in range(N)],
        sorted(c)
    )
     
    py5.stroke(0)
    x = 100
    for i, r in enumerate(rs):
        bucket = {i: 0 for i in range(10)}
        for n in r:
            y = n * 400
            bucket[int(n * 10)] += 1
            py5.stroke(n * 255, 255, 128)
            py5.line(x, 500, x, 500 - y)
            x += 1
        if i % 2 == 0:
            for b in range(10):
                py5.no_stroke()
                py5.fill(b * 25.5, 255, 128)
                py5.rect(x - N, (9 - b) * 40 + 510, bucket[b] * 5, 30)
            x += N / 3
        else:
            x += N / 2

def key_pressed():
    global s
    py5.save_frame(f'{s}.png')
    s += 1

py5.run_sketch()


