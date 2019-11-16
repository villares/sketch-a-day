"""
Based on //https://twitter.com/ky0ju_art/status/1188400508341383168?s=09
"""
from random import randint as r
x = y = X = Y = a = 0
p = []
def setup():
    size(500, 500)
    clear()

def draw():
    global x, y, X, Y, a
    translate(250, 250)
    a += 1
    x += X
    y += Y
    if a % 40 == 0:
        while a < 1000:
            X, Y = r(-1, 1), r(-1, 1)
            xy = x+X*40,y+Y*40
            if xy not in p:
                p.append(xy)
                break            
        fill(255)
        circle(x, y, 5)
    stroke(255)
    noFill()
    point(x, y)
    if abs(x) > 200 or abs(y) > 200:
        x = y = a = 0

def keyPressed():
    saveFrame("####.png")
