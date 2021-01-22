

def setup():
    size(500, 500)
    frameRate(5)
    
def draw():
    background(240)
    noFill()
    stroke(0, 64)
    f(250)

def f(x): 
    # push()
    DRAW(x) 
    if x > 1:
        f(1 * x / 4)
        f(2 * x / 4)
        f(3 * x / 4) 
    # pop()

def DRAW(x):
      triangle(0, 0,
               x, 0,
               x, x)
      translate(x, x)
      rotate(radians(frameCount))
      
