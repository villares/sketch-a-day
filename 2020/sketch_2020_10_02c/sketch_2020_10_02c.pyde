from random import choice


def setup():
    size(400, 400)
    noFill()
    generate(50)

def draw():
    background(240, 240, 200)
    translate(width / 2, height / 2)
    draw_e(elements)

def draw_e(els):    
    for i, e in enumerate(els):
        t, v, w = e
        strokeWeight(w)
        if t == 'L':
            line(0, 0, v[0], v[1])
            translate(v[0], v[1])
        if t == 'C':
            line(0, 0, v[0], v[1])
            circle(0, 0, dist(0, 0, v[0], v[1]))
            translate(v[0], v[1])
        if t == 'M' and len(els) > 2:
            pushMatrix()
            scale(.8)
            draw_e(els[i:-i])
            popMatrix()



def generate(n):
    global elements
    elements = [(choice('LLLLLMCCCC'),
                 (random(-width / 4, width / 4),
                  random(-height / 4, height / 4)),
                 choice((1, 3)),)
                for _ in range(n)] 

def keyPressed():
    generate(50)
