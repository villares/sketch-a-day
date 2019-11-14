"""
Based on //https://twitter.com/ky0ju_art/status/1188400508341383168?s=09
"""

x = y = X = Y = a = 0

def setup():
    size(500, 500)
    clear()
    
def draw():
    global x, y, X, Y, a
    translate(250, 250)
    a += 1
    x+=X
    y+=Y    
    if a % 40 == 0:
        X=int(random(-2, 2))
        Y=int(random(-2, 2))
        fill(255)
        circle(x, y, 5)
    stroke(255, 20);
    noFill()
    line(0, 0, x, y)
    if abs(x) > 200 or abs(y) > 200:
        x = y = a = 0
    
def keyPressed():
    saveFrame("####.png")
