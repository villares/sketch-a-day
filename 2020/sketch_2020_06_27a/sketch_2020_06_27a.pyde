n = 8
t = 0
def setup():
    global s
    size(400, 400)
    s = width / n
    textAlign(CENTER, CENTER)
    colorMode(HSB)
    noStroke()
#  (t+abs((x+y-t)^(x-y+t))**3)%1023<109

def draw():
    # t = frameCount
    for x in range (n):
        for y in range(n):
            a = x + y - t
            b = x - y + t
            c = abs(a ^ b)
            d = (c ** 3) % 1023
            if d < 512:
                fill(-1)
                # colorMode(HSB)
                # fill(d % 256, 255, 255)
            else:
                fill(0)
            rect(x * s, y * s, s, s)
            fill(abs(c) * 8, 200, 200)
            text("{}^{}\n{}".format(a, b, a^b),
                 x * s + s / 2, y * s + s / 2)
        
