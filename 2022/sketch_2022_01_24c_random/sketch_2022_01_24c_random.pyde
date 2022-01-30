from random import random as rnd

size(500, 500)
colorMode(HSB)
background(0)

translate(0, 250)  # normal random
for x in range(width):
    r = rnd() * 250 #random(250)
    stroke(r, 200, 200)
    line(x, 0, x, 0 + r)

translate(0, -250) # this is mine
for x in range(width):
    n = x + int(random(1000))
    r = (abs(sin(n * 3) + sin(n * 7) + sin(n * 11) + (n * 13)) * 1000) % 250
    stroke(r, 200, 200)
    line(x, 0, x, 0 + r)
    
    
    
