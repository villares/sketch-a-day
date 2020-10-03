from random import choice, sample

new_origin = PVector()
elements = []

def setup():
    size(600, 600)
    noFill()

def generate(n=60):
    global elements
    new_origin.set(width / 2, height / 2)
    pegs = (-20, -10, 0, 0, 10, 20)
    elements = [(choice('LCCRM'),
                 (choice(pegs),choice(pegs)),
                 choice((1, 3)),)
                for _ in range(n)]

def draw():
    background(240, 240, 200)
    translate(new_origin.x, new_origin.y)
    trans_e(0, 0, start=True)
    stroke(255, 0, 0)
    draw_e(elements)

def draw_e(els):
    for i, e in enumerate(els):
        # print(e)
        stroke(0)
        t, v, w = e
        strokeWeight(w)
        if t == 'L':
            line(0, 0, v[0], v[1])
            trans_e(v[0], v[1])
        if t == 'C':
            line(0, 0, v[0], v[1])
            if w != 1:
                fill(0)
            else:
                noFill()
            circle(0, 0, dist(0, 0, v[0], v[1]) / w ** 2)
            trans_e(v[0], v[1])
        if t == 'M' and len(els) > 1:
            for _ in range(3):
                stroke(0)
                line(0, 0, v[0], v[1])
                trans_e(v[0], v[1])
                draw_e(els[i - 3:i - 1])
                trans_e(-els[i-1][1][0], -els[i-1][1][1])
                # print(els[i - 3:i - 1])
        if t == 'R' and len(els) > 2:
            for _ in range(3):
                stroke(0)
                line(0, 0, v[0], v[1])
                trans_e(v[0], v[1])
                line(0, 0, v[1] / 2, -v[0] / 2)
                trans_e(v[1], -v[0])
                # draw_e([els[i - 1]])

def trans_e(x, y, history=[], start=False):
    if start:
        history[:] = [PVector()]
    translate(x, y)
    history[0].add(PVector(x, y))
    current = history[0]
    if current.x + new_origin.x > width:
        new_origin.x -= 0.2
    if current.y + new_origin.y > height:
        new_origin.y -= 0.2
    if current.x + new_origin.x < 0:
        new_origin.x += 0.2
    if current.y + new_origin.y < 0:
        new_origin.y += 0.2


def keyPressed():
    generate()
