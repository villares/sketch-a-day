n, t = 64, 0
def setup():
    noStroke()
    frameRate(2)
    size(320, 320)
    colorMode(HSB)
def draw():
    s = width / n
    for x in range(n):
        for y in range(n):
            c = (frameCount ** y)
            bv = '{:064b}'.format(c)
            if bv[x] == '0':
                fill(0)
            else:
                fill(c % 255, 255, 255)
            rect(x * s, y * s, s, s)
