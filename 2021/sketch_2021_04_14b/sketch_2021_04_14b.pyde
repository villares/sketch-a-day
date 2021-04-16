def setup():
    size(800, 800)
    strokeWeight(2)
    stroke(255)

def f(x):
    return (x * 2 + 100) / 4

def g(x):
    return (x ** 2) / (1+mouseX) - mouseY

def draw():
    background(0, 0, 100)
    translate(width / 2, height / 2)
    scale(1, -1)                
    for x10 in range(-width * 10, width * 10):
        x = x10 / 10.0
        point(x, f(x))
        point(x, g(x))
