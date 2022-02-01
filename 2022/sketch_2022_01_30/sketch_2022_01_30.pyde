

def setup():
    size(600, 600)
    noFill()
    rectMode(CENTER)
    
def draw():
    background(220, 240, 240)
    translate(width / 2, height / 2)
    r = 200
    for d in range(360):
        a = radians(d)
        x = r * cos(a)
        y = r * sin(a)
        s0 = 15 + 15 * cos(a * 5 + radians(frameCount))
        s1 = 15 + 15 * sin(a * 3)
        s3 = 20 + 15 * sin(a * 11  + radians(frameCount))
        s = s0 + s1 + s3
        push()
        translate(x, y)
        rotate(a)
        square(0, 0, s)
        pop()
        
    
                
                
