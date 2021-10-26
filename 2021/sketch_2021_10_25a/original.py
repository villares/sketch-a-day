D = 500

def setup():
    size(D, D, P3D)
    smooth(4)
    strokeWeight(1.5)

def draw():
    background(200)
    randomSeed(1)
    translate(250, 250, -D)
    rotateX(frameCount / 12.0)
    translate(-250, -250, 0)
    stroke(0)    
    for x in range(width):
        for y in range(height):
            if dist(x, y, 250, 250) > random(D * 100):
                line(x, y, -250, x, y, 250)    
    
