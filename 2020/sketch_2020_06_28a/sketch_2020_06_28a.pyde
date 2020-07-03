n = 32
t = 0

def setup():
    global s
    noStroke()
    frameRate(2)
    size(320, 320)

def draw():
    s = width / n
    textAlign(CENTER, CENTER)
    textSize(14)
    colorMode(HSB)
    for x in range(n):
        for y in range(n):
            c = (frameCount + y) ** 2
            bv = left_padded_bin(c, n)
            if bv[x] == '0':
                fill(0)
            else:
                fill(255)
            rect(x * s, y * s, s, s)


def left_padded_bin(v, n):
    f = '{{:0{}b}}'.format(n)
    return f.format(v)
