
def setup():
    size(500, 500)
    translate(250, 250)
    fill(0)
    s = 5
    for i in range(11):
        step = 11 - i
        r = 20 + 20 * i 
        for a in range(0, 360, step):
            x = r * cos(radians(a))
            y = r * sin(radians(a))
            circle(x, y, s)
