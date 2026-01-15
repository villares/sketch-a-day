def setup():
    size(400, 400)
    window_resizable(True)
    
def draw():
    background(0)
    stroke(255)
    no_fill()
    num_circles = 10
    d = width / num_circles
    for i in range(num_circles):
        x = i * d + d / 2
        circle(x, height / 2, d)
