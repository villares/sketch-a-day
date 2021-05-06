

def setup():
    size(600, 600)
    background(0, 0, 100)
    translate(width / 2, height / 2)
    scale(25, -25)
    textSize(0.5)
    textAlign(CENTER, CENTER)
    scale(1, -1)
    stroke(255)
    strokeWeight(0.055)
    line(0, height, 0, -height)
    line(-width, 0, width, 0)
    noStroke()
    fill(128)
    for i in range(-25, 25):
        # text(i, i, 0)
        if  i != 0:
            circle(0, i, 0.1)
            text(i, -2, -i - 1)
        circle(i, 0, 0.1)
        if  i != -1:
            text(i, i if i > 0 else i - 1, 0)
