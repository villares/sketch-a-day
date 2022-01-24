

size(500, 500)
colorMode(HSB)
background(0)

for x in range(width):
    r = (abs(sin(x * 7) + sin(x * 13) + sin(x * 3) + (x * 11)) * 1000) % 250
    stroke(r, 200, 200)
    line(x, 0, x, 0 + r)

translate(0, 250)
for x in range(width):
    r = random(250)
    stroke(r, 200, 200)
    line(x, 0, x, 0 + r)
    
    
