# D'aprés @ntsutae つぶやきProcessing 
# https://twitter.com/ntsutae/status/1268432505356513280?s=20

t = 0
a, b, c = 3.1, 1024, 256
def setup():
    size(1000, 1000)
    noSmooth()
    noStroke()
    fill(0)
    colorMode(HSB)
    frameRate(30)
    
def draw():
    global t
    t += 1
    background(240)
    for y in range(width // 4):
        for x in range(width // 4):
            s = (t + abs((x + y - t) ^ (x - y + t)) ** a) % b
            if s < c:
                fill(s , 200, 200)
                rect(x * 4, y * 4, 4, 4)
            
