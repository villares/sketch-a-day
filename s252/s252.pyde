

def setup():
    size(400, 400)

def draw():
    fill(200, 10)
    rect(0, 0, width, height)
    r = 100  # radius
    x1, y1 = 100, 200
    a1 = frameCount / map(mouseX, 0, width, 1, 50)
    sx1 = x1 + cos(a1) * r
    sy1 = y1 + sin(a1) * r
    x2, y2 = 300, 200
    a2 = frameCount / map(mouseY, 0, height, 1, 50)
    sx2 = x2 + cos(a2) * r
    sy2 = y2 + sin(a2) * r
    line(sx1, sy1, sx2, sy2)
