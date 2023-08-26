def setup():
    size(600, 600)
    background(0)
    rect_mode(CENTER) # quadrados e rects pelo centro
    n = 40
    w = width / n
    no_stroke()
    fill(0, 0, 255)
    for j in range(n):
        y = w / 2 + j * w
        for i in range(n): # 0, 1, 2 ... 9
            x = w / 2 + i * w
            d = 6 + (j + i) % 7
            circle(x, y, d)
    fill(0, 255, 0)
    for j in range(n):
        y = w / 2 + j * w
        for i in range(n): # 0, 1, 2 ... 9
            x = w / 2 + i * w
            d = 2 + (i - j) % 7
            circle(x, y, d)
            
    save(__file__[:-3] + '.png')
    
