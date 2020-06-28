#  (t+abs((x+y-t)^(x-y+t))**3)%1023<109
n = 16
t = 0
def setup():
    global s
    size(400, 400)
    s = width / n
    textAlign(CENTER, CENTER)
    colorMode(HSB)

    for x in range (n):
        for y in range(n):
            a = x + y - t
            b = x - y + t
            c = a ^ b
            fill(-1)
            rect(x * s, y * s, s, s)
            fill(abs(c) * 8), 200, 200)
            text("{}^{}\n{}".format(a, b, a^b),
                 x * s + s / 2, y * s + s / 2)
        
