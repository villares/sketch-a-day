"""
Based on //https://twitter.com/ky0ju_art/status/1188400508341383168?s=09
"""
from random import randint as r
x = y = X = Y = a = 0
p = [(0, 0)]
def setup():
    size(500, 500)
    colorMode(HSB)
    clear()

def draw():
    global x, y, X, Y, a
    translate(250, 250)
    a += 1
    x += X
    y += Y
    stroke(a % 255, 255, 255)
    if a % 40 == 0:
        while a < 400:
            X, Y = r(-1, 1), r(-1, 1)
            xy = x+X*40, y+Y*40
            if xy not in p:
                p.append(xy)
                break    
        else:
            x = int(random(-width, width) / 80) * 40
            y = int(random(-height, height) / 80) * 40
            if (x, y) not in p:
                p.append((x, y))
            else:
                x, y = 0, 0 
                return        
        print(x, y)
        strokeWeight(5)
        point(x, y)
        strokeWeight(1)
    point(x, y)
    if abs(x) > 200 or abs(y) > 200:
        x = y = a = 0

def keyPressed():
    saveFrame("####.png")
