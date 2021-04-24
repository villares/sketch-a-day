moleculas = []

def setup():
    size(800, 800)
    for _ in range(2000):
        x = random(width)
        y = random(height)
        moleculas.append([x, y])
        
def draw():
    background(0)        
    stroke(255, 100)    
    for molecula in moleculas:
        for outra in reversed(moleculas):
            if molecula is outra:
                break
            xa, ya = molecula
            xb, yb = outra 
            d = dist(xa, ya, xb, yb)
            a = int(degrees(atan2(ya -yb, xa - xb)))
            if d < 80 and (a == 30 or a == 90 or a == -30):
                line(xa, ya, xb, yb)
    
    for x, y in moleculas:
        noStroke()
        circle(x, y, 3)
        
def keyPressed():
    saveFrame("agua.png")
