
m = 100
w = 8

def setup():
    size(800, 800)
    strokeWeight(3)
    

def draw():
    background(240)
    for xg in range(m, width - m, w): 
        for yg in range(m, height - m, w):
            a = radians(frameCount % 720) / 2
            d = sin(dist(400 + 200 * cos(a + xg / 120.0),
                         400 + 200 * sin(a - yg / 120.0), xg, yg) / 20.0)
            r = 12
            x = xg + r * cos(a + d)
            y = yg + r * sin(a + d)
            point(x, y) 
            
    saveFrame('###.tga')
    if frameCount == 720: exit()
    
    
