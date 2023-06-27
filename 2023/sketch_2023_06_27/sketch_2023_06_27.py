import py5
from py5 import random, random_seed

s = 1

def setup():
    py5.size(1000, 600)
    
def draw():
    py5.background(240)
    random_seed(s)
    rs =(
        a := [random(1) for _ in range(100)],
        sorted(a),
        b := [random(1) * random(1) for _ in range(100)],
        sorted(b),
        c := [random(1) ** 2 for _ in range(100)],
        sorted(b)
    )
    py5.stroke(0)
    x = 100
    for i, r in enumerate(rs):
        for n in r:
            y = n * 400
            py5.line(x, 500, x, 500 - y)
            x += 1
        x += 33.4 if i % 2 == 0 else 50
    py5.stroke(200, 0, 0)
    py5.line(100, 100, 900, 100)
    py5.line(100, 300, 900, 300)


def key_pressed():
    global s
    s += 1

py5.run_sketch()