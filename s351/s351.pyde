


def setup():
    size(600, 600)
    rectMode(CENTER)
    noFill()
    noLoop()
    
def draw():
    # background(220)
    # for n in range(1, 11):
        n = 20
        s = width / (n + 1)
        for i in range(n):
            for j in range(n):
                draw_grid_el(i, j, s, rule(i, j))
            
def draw_grid_el(i, j, s, f):
    r = int(random(4))
    x = s + i * s
    y = s + j * s
    with pushMatrix():
        translate(x, y)
        rotate(r * HALF_PI)
        noFill()
        stroke(150)
        rect(0, 0, s, s)
        fill(0)
        noStroke()
        f(s)
        
def rule(i, j):
    
    def square(s):
        rect(s/4., s/4., s/2., s/2.)

    def circle(s):
        ellipse(s/4., s/4., s/2., s/2.)

    if (i + j)  % 3:
        return square
    else:
        return circle
