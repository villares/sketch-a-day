from itertools import product
from random import sample

def setup():
    global grade
    size(500, 500)
    grade = list(product(range(50, 500, 100), repeat=2))    
    frameRate(2)
           
def draw():
    colorMode(RGB)
    background(200, 200, 180)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    fill(255, 100)
    
    a, b, c, d = sample(grade, 4)
    line(a[0], a[1], b[0], b[1])          
    line(c[0], c[1], d[0], d[1])          
    
    ab = degrees(atan2(a[1] - b[1], a[0] - b[0]))
    cd = degrees(atan2(c[1] - d[1], c[0] - d[0]))
    p = abs(ab - cd)
    textAlign(CENTER, CENTER)
    if p == 0 or p == 90 or p == 180:
        fill(255, 0, 0)
    else:
        fill(0)
    textSize(40)
    text(format(p, ".0f"), 250, 200)
    # text(cd, 250, 290)
              
