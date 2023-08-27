def setup():
    size(960, 960)
    frame_rate(1)

def draw():
    background(0)
    rect_mode(CENTER) # quadrados e rects pelo centro
    n = 32
    w = width / n
    no_stroke()
    fill(200, 200, 0)
    for j in range(n):
        y = w / 2 + j * w
        for i in range(n): # 0, 1, 2 ... 9
            x = w / 2 + i * w
            d = 6 + ((i + frame_count) % 10) * 2
            square(x, y, d)
    fill(0, 0, 255)
    for j in range(n):
        y = w / 2 + j * w
        for i in range(n): # 0, 1, 2 ... 9
            x = w / 2 + i * w
            d = 4 + ((j + i) % 10) * 2
            square(x, y, d)
    fill(0, 255, 0)
    for j in range(n):
        y = w / 2 + j * w
        for i in range(n): # 0, 1, 2 ... 9
            x = w / 2 + i * w
            d = 2 + ((i - j) % 10) * 2
            square(x, y, d)
    if frame_count < 11:        
        save_frame('###.png')  # __file__[:-3] + '.png'
    
