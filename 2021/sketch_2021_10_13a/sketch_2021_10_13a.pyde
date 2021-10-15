steps = (2, 3, 4, 5, 6, 8, 9, 10, 12, 15)

def setup():
    size(500, 500)
    
def draw():
    background(0)
    translate(250, 250)
    noStroke()
    colorMode(HSB)
    i_step = enumerate(reversed(steps))
    for i , step in i_step:
        r = 25 + 22 * i + 12 * sin(radians(i * 20 + frameCount))
        # fill(18 * step % 256, 255, 255)
        fill(r % 256, 255, 255)
        for a in range(0, 360, step):
            x = r * cos(radians(a + i * 2))
            y = r * sin(radians(a + i * 2)) 
            s = TWO_PI * r / (360 / step)
            circle(x, y, s)
    if frameCount < 361 and frameCount % 2:
        saveFrame("###.png")
