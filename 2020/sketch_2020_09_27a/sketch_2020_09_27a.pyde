# inspired by https://twitter.com/senbaku/status/1310226594141630464/photo/3
def setup():
    global things, w, h
    size(500, 500)
    colorMode(HSB)
    rectMode(CENTER)
    noStroke()
    
    N = 50
    w = width / N
    h = height / N
    things = []
    for i in range(N):
        for j in range(N):
            things.append([w / 2 + i * w,
                           h / 2 + j * h,
                            random(200)])

def draw():
    colorMode(RGB)
    background(240, 240, 200)
    colorMode(HSB)
    
    s = 0.01
    for x, y, c in things:
        # # smooth noise
        # nw = noise(x * s, y * s, 200 + frameCount / 2. * s)
        # nh = noise(x * s, y * s, frameCount / 2. * s)
        # light crossing noise
        # nw = noise(x * s, y * s, x + 100 + frameCount / 2. * s)
        # nh = noise(x * s, y * s, y + frameCount / 2. * s)
        # dense crossing noise
        # nw = noise(x * s, y * s, y + 100 + frameCount / 2. * s)
        # nh = noise(x * s, y * s, x + frameCount / 2. * s)
        # vertical formations
        nw = noise(x * s, y * s, x + 100 + frameCount / 2. * s)
        nh = noise(x * s, y * s, x + frameCount / 2. * s)

        fw = (2 + w) * nw
        fh = (2 + h) * nh
        a = (6 * fw * fh) % 256
        b = (c + 6 * fw * fh) % 256
        fill(a, 150, 150)
        # fill(b, 150, 150)    
        # fill(c, 150, 150)
        rect(x, y, fw, fh)
