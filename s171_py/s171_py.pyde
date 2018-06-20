# Inpired on http://10print.org/
# s171 180619

tam = 20

def setup():
    rectMode(CENTER)
    size(500, 500)
    noStroke()
    noLoop()

def draw():
    background(0)
    num = int(width / tam)
    for i in range(num):
        for j in range(num):
            fill(random(128), random(128), random(128))
            rect(tam / 2 + j * tam, tam / 2 + i * tam, tam, tam)

    for i in range(num):
        for j in range(num):
            stroke(255)
            strokeWeight(6)
            pushMatrix()
            translate(tam / 2 + j * tam, tam / 2 + i * tam)
            rotate(HALF_PI * int(random(2)))
            line(-tam / 2, -tam / 2, tam / 2, tam / 2)
            popMatrix()
