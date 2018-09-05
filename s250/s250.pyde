

def setup():
    size(400, 400)

def draw():
    background(220)
    with pushMatrix():
        translate(100, 200)
        rotate(frameCount/10.)
        noFill()
        ellipse(0, 0, 100, 100)
        fill(0)
        ellipse(50, 0, 10, 10)
    with pushMatrix():
        translate(300, 200)
        rotate(frameCount/20.)
        noFill()
        ellipse(0, 0, 100, 100)
        fill(0)
        ellipse(0, 50, 10, 10)
