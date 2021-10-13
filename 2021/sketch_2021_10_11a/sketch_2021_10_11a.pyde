
def setup():
    size(500, 500)
    
def draw():
    background(0)
    translate(250, 250)
    noStroke()
    colorMode(HSB)
    s = 5
    for i in range(11):
        step = (11 - i) * 2
        t = 1 + 1 * sin(radians(frameCount / 5.0))
        r = 20 + 20 * i * t
        fill(r % 256, 255, 255)
        for a in range(0, 360, step):
            x = r * cos(radians(a))
            y = r * sin(radians(a)) 
            circle(x, y, s)
