tam = 20
margem = 40

def setup():
    size(300, 500)
    rect_mode(CENTER)
    no_fill()
    no_loop()

def draw():
    background(240)
    t = 0
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
    push_matrix()
    translate(x, y)
    rect_mode(CENTER)
    rotate(ang)
    rect(0, 0, w, h)
    pop_matrix()

def key_pressed():
  redraw()
