def setup():
    size(700, 700) 
    randomize()

def randomize():
    global small_r, big_r, n_pointed
    small_r = random_int(100, 200)  # raio menor
    big_r = random_int(200, 350)  # raio maior
    n_pointed = random_int(3, 7)  # n_pointed

def draw():
    background(0, 0, 100)
    star(350, 350, small_r, big_r, n_pointed) 
    
def star(cx, cy, ra, rb, n):  # estrela
    step = TWO_PI / n  # passo
    begin_shape()
    for i in range(n):  # for each tip/point
        ang = step * i  + frame_count / 50.0 # angle
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay)
        bx = cx + cos(ang + step / 2.0) * rb
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by)
    end_shape(CLOSE)

def key_pressed():
    randomize()