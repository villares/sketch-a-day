COLORS = [color(0), color(0), color(0),
          color(255), color(255),
          color(200, 0, 100),
          ]

def circle(x, y, s):
    pushStyle()
    noStroke()
    ellipse(x, y, s, s)
    popStyle()
    
def square(x, y, s):
    pushStyle()
    rectMode(CENTER)
    noStroke()
    rect(x, y, s, s)
    popStyle()


def exes(x, y, s):
    pushStyle()
    strokeWeight(3)
    with pushMatrix():
        translate(x, y)
        line(-s / 2, -s / 2, s / 2, s / 2)
        line(s / 2, -s / 2, -s / 2, s / 2)
    popStyle()

def losang(x, y, s):
    pushStyle()
    noStroke()
    with pushMatrix():
        translate(x, y)
        rotate(radians(45))
        rect(0, 0, s, s)
    popStyle()
