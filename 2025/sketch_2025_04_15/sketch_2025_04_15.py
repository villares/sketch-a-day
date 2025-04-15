
def setup():
    size(500, 200)
    
    fill(200, 0, 0)
    x = 25
    for _ in range(10):
        circle(x, 25, 40)
        x = x + 50
        
    fill(0, 200, 0)
    for x in range(25, 500, 50):
        circle(x, 75, 40)

    fill(0, 0, 200)
    for i in range(10):
        circle(25 + i * 50, 125, 40)

    text_align(CENTER, CENTER)
    y = 175
    w = 50
    for i in range(10):
        x = w / 2 + i * w
        fill(0)
        circle(x, y, w - 10)
        fill(255)
        text(i, x, y)
        
        