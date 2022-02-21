
def setup():
    size(600, 600, P3D)
    noStroke()
    s
def draw():
    background(0)
    translate(300,300,-150)
    for b in range(0,360,10):
        for a in range(-90,90,5):
            push()
            rotateY(radians(b + a*.5 + frameCount*.5))
            rotateX(radians(a))
            r = 100 * sin(radians(b)) + 100 * cos(radians(a))
            translate(0,0,100 + r)
            fill(90 + a * 2,
                    128 + 128 * sin(radians(b)),
                    128 + 128 * cos(radians(a)))
            circle(0,0,10)
            pop()
            
            
