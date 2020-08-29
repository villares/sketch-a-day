

def setup():
    size(400, 400)
    frameRate(2)
    colorMode(HSB)
    noStroke()

def draw():
    background(0)
    translate(width / 2, height / 2)
    s = 80 / (fib(frameCount + 1) / 4.)
    scale(s)
    print(s)
    x, y = 0, 0
    for n in range(1, frameCount):
        fill((n * 16) % 256, 255, 255)
        fib_n = fib(n)
        square(x, y, fib_n)
        fib_next = fib(n + 1)
        translate(fib_n + fib_next, 0)
        rotate(HALF_PI)


# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# for i in range(1, 101):
#     print(fib(i + 1) / float(fib(i)))
