def setup():
    global ra, rb, n
    size(700, 700) 
    randomize()
    ra, rb, n = next_ra, next_rb, next_n

def randomize():
    global next_ra, next_rb, next_n
    next_ra = random_int(100, 350)  # raio a
    next_rb = random_int(100, 350)  # raio br
    next_n = random_int(3, 13)  # n_pointed

def draw():
    global ra, rb, n
    background(0, 100, 100)
    ra = lerp(ra, next_ra, 0.05)
    rb = lerp(rb, next_rb, 0.1)
    n = round(lerp(n, next_n, 0.6))
    #print(n, next_n)
    cx, cy = 350, 350
    step = TWO_PI / n  # passo
    begin_shape()
    for i in range(n):  # for each tip/point
        ang = step * i  + frame_count / 100.0 # angle
        ax = cx + cos(ang) * ra
        ay = cy + sin(ang) * ra
        vertex(ax, ay)
        bx = cx + cos(ang + step / 2.0) * rb
        by = cy + sin(ang + step / 2.0) * rb
        vertex(bx, by)
    end_shape(CLOSE)

def key_pressed():
    randomize()