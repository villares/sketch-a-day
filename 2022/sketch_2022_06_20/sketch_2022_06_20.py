# From @introscopia's code
# https://twitter.com/Introscopia/status/1538966209114390529

def setup():
    size(700, 700)
    mouse_pressed()

def draw():
    background(0, 0, 100)
    stroke_weight(5)
    stroke(255)
    johns_star(350, 350, 300,
               frame_count / 100,
               n_pointed,
               1 + int(mouse_x / 50))

def johns_star(cx, cy, d, a, n, skip):
    if skip >= n:
        return
    done = False
    first = 1
    k = c = i = 0
    step = TWO_PI / n  # passo
    while not done:
        if i == n + k or (i == k and not first):
            if c == n:
                done = True
            elif c < n:
                k += 1
                i = k
                first = 1
        else:
            offset = 0
            if i + skip > n:
                offser = -n
            line(cx + d * cos(i * step + a),
                 cy + d * sin(i * step + a),
                 cx + d * cos((i + skip + offset) * step + a),
                 cy + d * sin((i + skip + offset) * step + a))
            if i + skip > n:
                i = (i + skip) -n
            else:
                i += skip
            c += 1
            first = 0

def mouse_pressed():
    global n_pointed 
    n_pointed = random_int(5, 15)  # n_pointed