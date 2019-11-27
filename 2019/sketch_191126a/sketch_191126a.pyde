# Noite de Processing: relâmpagos
# live code com noisem, em 5 minutos

def setup():
    size(700, 700)
    
def draw():
    background(255)
    translate(350, 350)
    for i in range(360):
        a = radians(i)
        s = .01
        x = 100 * sin(a)
        y = 100 * cos(a)
        z = frameCount
        n = noise(s * z, s * (x + y + abs(x)), s * (x + y + abs(y)))
        noFill()
        circle(x, y, 100 * n)
                                
