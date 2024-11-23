from functools import cache
import py5

STEP = 10

def setup():
    py5.size(910, 570)
    py5.background(0)
    py5.color_mode(py5.HSB)
    
    y = x = 10
    
    for n in range(1, 11):
        w = fib(n) * STEP
        print(w)
        py5.fill(10 + w / 3, 200, 200)
        py5.square(x, y, w)
        last = fib(n - 1) * STEP
        if n % 2:
            x += w
            if n > 1:
                y -= last
        else:
            y += w
            x -= last

    py5.save('out.png')

@cache
def fib(n):
    #print(n)
    if n < 3:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
    
py5.run_sketch(block=False)