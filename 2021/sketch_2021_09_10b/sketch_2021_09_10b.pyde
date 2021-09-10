
m = 100
w = 10

def setup():
    size(800, 800)
    strokeWeight(3)
    

def draw():
    background(240)
    for xg in range(m, width - m, w): 
        for yg in range(m, height - m, w):
            a = frameCount / 20.0
            # r = 5 + 5 * sin(-a + xg  * 3 - yg * 5)
            d = sin(dist(400, 400, xg, yg) / 10.0)
            r = 5
            x = xg + r * cos(a + d)
            y = yg + r * sin(a + d)
            point(x, y) 
