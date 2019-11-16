"""
Based on //https://twitter.com/ky0ju_art/status/1188400508341383168?s=09
"""
from random import randint as r
x = y = X = Y = a = 0
def setup():
    size(500, 500)
    clear()
    # smooth(8)
    strokeWeight(2)

def draw():
    global x, y, X, Y, a
    translate(250, 250)
    a += 1
    x += X
    y += Y
    if a % 40 == 0:
        X = r(-2, 2)
        Y = r(-2, 2)
        # fill(255)
        # circle(x, y, 5)
    stroke(255)
    fill(255, 0, 0)
    circle(x, y, 10)
    if a>400:
        x = y = a = 0

def keyPressed():
    saveFrame("####.png")
