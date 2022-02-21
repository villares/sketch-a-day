
def setup():
    size(600, 600, P3D)
    noStroke()
    
def draw():
    background(0)
    translate(300,300,0)
    for b in range(0,360,10):
        for a in range(-90,90,5):
            push()
            rotateY(radians(b + a*.5 + frameCount*.5))
            rotateX(radians(a))
            translate(0,0,-200)
            fill(90 + a * 2,
                    128 + 128 * sin(radians(b)),
                    128 + 128 * cos(radians(b)))
            circle(0,0,10)
            pop()
