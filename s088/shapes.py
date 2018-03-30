COLORS = [color(0), color(0), color(0),
          color(255), color(255),
          color(200, 0, 100),
          ]

def my_ellipse(x, y, d, _):
    pushStyle()
    noStroke()
    ellipse(x, y, d, d)
    popStyle()
    
def my_rect(x, y, d, _):
    pushStyle()
    rectMode(CENTER)
    noStroke()
    rect(x, y, d, d)
    popStyle()


def exes(x, y, c, _):
    pushStyle()
    strokeWeight(3)
    with pushMatrix():
        translate(x, y)
        line(-c / 2, -c / 2, c / 2, c / 2)
        line(c / 2, -c / 2, -c / 2, c / 2)
    popStyle()

def losang(x, y, c, _):
    pushStyle()
    noStroke()
    with pushMatrix():
        translate(x, y)
        rotate(radians(45))
        rect(0, 0, c, c)
    popStyle()
