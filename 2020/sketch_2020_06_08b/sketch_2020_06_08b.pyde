tam = 20
margem = 40
t = 0

def setup():
    size(300, 500)
    rectMode(CENTER)
    noFill()
    noLoop()

def draw():
    global t
    background(240)
    for j in range(20):
       for i in range(12):
            y = j * tam + random(-t/3, t/3)
            x = i * tam + random(-t/3, t/3)
            r = random(-t, t)
            print(r)
            rr(margem + x,
               margem + y,
               tam, tam, radians(r)
               )
            t += .12  # t = t + 1

def rr(x, y, w, h, ang):
    # push()
    # pushStyle()
    pushMatrix()
    translate(x, y)
    rectMode(CENTER)
    rotate(ang)
    rect(0, 0, w, h)
    popMatrix()
    # popStyle()
    # pop()
