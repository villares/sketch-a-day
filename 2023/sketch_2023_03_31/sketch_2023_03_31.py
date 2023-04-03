import py5

margin = 60

def setup():
    py5.size(800, 800)
    py5.no_loop()

def draw():
    py5.background(0)
    grid(margin, margin, py5.width - margin * 2)

def grid(xo, yo, largura_total, n=3):
    w = largura_total / n
    color_step = 255 / n
    for j in range(n):
        x = xo + w * j
        for i in range(n):
            y = yo + w * i
            py5.fill(i * color_step,        # red
                     j * color_step,        # green
                     255 - i * color_step)  # blue
            if w > 10 and py5.random(9) > 5:
                grid(x, y, w)
            else:
                py5.circle(x + w / 2, y + w / 2, w * 0.98)

def key_pressed():
    py5.save_frame('###.png')
    redraw()

py5.run_sketch()
