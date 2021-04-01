
from itertools import product            

moleculas = []

def setup():
    size(800, 800)
    for _ in range(2000):
        x = random(width)
        y = random(height)
        moleculas.append([x, y])
        
def draw():
    background(0)        
    for i, (x, y) in enumerate(moleculas):
        m = moleculas[i]
        noStroke()
        ns = 0.01
        m[0] +=  5 - 10 *noise(x, y,  frameCount * ns )
        m[1] += 5 - 10 * noise(x + 1, y + 1, frameCount * ns)
        circle(m[0], m[1], 3)
        # h = 360 * noise(x, y,  frameCount * ns )
        # v = 10 * PVector.fromAngle(radians(h))
        # m[0] += v.x
        # m[1] += v.y
        # circle(m[0], m[1], 3)
         
    for molecula in moleculas:
        for outra in reversed(moleculas):
            if molecula is outra: break
            # c += 1
            xa, ya = molecula
            xb, yb = outra 
            d = dist(xa, ya, xb, yb)
            a = int(degrees(atan2(ya -yb, xa - xb)))
            if d < 80 and (a == 30 or a == 90 or  
                             a == -30):
                stroke(255, 100)    
                line(xa, ya, xb, yb)
                # circle(xa, ya, 3)
      
                        
    if frameCount < 5:    saveFrame("##.png")

        
# def H2O(x, y, tamanho=6):
#     deslocamento = tamanho * 0.66
#     pushMatrix()    
#     translate(x, y)
#     rotate(x + y)
#     fill(0, 0, 200)
#     circle(0, 0, tamanho)
#     fill(255)        
#     circle(tamanho / 2.0, -deslocamento, deslocamento)
#     circle( tamanho / 2.0, +deslocamento, deslocamento)
#     popMatrix()
