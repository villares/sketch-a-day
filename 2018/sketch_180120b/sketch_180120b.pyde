"""
s18020b - Alexandre B A Villares
https://abav.lugaralgum.com/sketch-a-day

Playing with HSB color mode and varying fill
"""

def setup():
    noStroke()
    colorMode(HSB)
    size(500, 500, P2D)
    background(0)
    #noLoop()


def draw():
    background(0)
    translate(width / 2, height / 2)
    npoints, r1, r2 = 3, mouseX, mouseY
    angle = TWO_PI / npoints
    beginShape()
    #vertex(0, 0)
    a = 0
    while a <= TWO_PI:
        sx = cos(a) * r2
        sy = sin(a) * r2
        cor = map(a, 0, TWO_PI, 0, 255)
        fill(cor, 255, 255)
        vertex(sx, sy)
        sx = cos(a + angle / 2) * r1
        sy = sin(a + angle / 2) * r1
        vertex(sx, sy)
        a += angle
    endShape(CLOSE)
    if not frameCount % 10 and frameCount < 500:
        saveFrame("###.tga")