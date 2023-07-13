speed = 2
s = 0.01

def setup():
    global things, w, h, wo
    size(1200, 800)
    #full_screen()
    color_mode(HSB)
    rect_mode(CENTER)
    no_stroke()
    
    wo = width / 12
    N = int(wo)
    w = width / N
    h = height / N
    things = []
    for i in range(N):
        for j in range(N):
            things.append([w / 2 + i * w,
                           h / 2 + j * h,
                            random(200)])

def draw():
    background(0)
    
    
    for x, y, c in things:
        # smooth noise
#         nw = noise((frame_count * 2 + x) * s, y * s, 100 + frame_count * speed * s)
#         nh = noise((frame_count * 2 + x) * s, y * s, frame_count * speed * s)
        # # light crossing noise#
#         nw = noise(x * s, y * s, x + 100 + frame_count * speed * s)
#         nh = noise(x * s, y * s, y + frame_count * speed * s)
        # dense crossing noise
#         nw = noise(x * s, y * s, y + wo + frame_count * speed * s)
#         nh = noise(x * s, y * s, x + frame_count * speed * s)
        # # vertical formations
        nw = noise(x * s, y * s, x + 100 + frame_count * speed * s)
        nh = noise(x * s, y * s, x + frame_count * speed * 2 * s)

        fw = (2 + w) * nw
        fh = (2 + h) * nh
        a = (6 * fw * fh) % 256
        b = (6 * fw * fh) % 256
        fill(a, 150, 150)
        fill(b, 150, c)    
        # fill(c, 150, 150)
        rect(x + 2* w * (-.5+nw), y + 2 * h * (-.5+nh), fw, fh)
        # rect(x + x * (-.5+nw), y + y * (-.5+nh), fw, fh)