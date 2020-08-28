

def setup():
    size(600, 600)
    frameRate(2)
    colorMode(HSB)

def draw():
    background(0)
    translate(width / 2, height / 2)
    s = 10 / sqrt(fib(frameCount))
    scale(s)
    if s == 0:
        exit()
    # strokeWeight(1 / s)
    x, y = 0, 0
    for n in range(1, frameCount):
        fill((n * 12) % 256, 255, 255)
        fib_n = fib(n)
        square(x, y, fib_n)
        fib_next = fib(n + 1)
        translate(fib_n + fib_next, 0)
        rotate(HALF_PI)


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

# for i in range(1, 101):
#     print(fib(i + 1) / float(fib(i)))
