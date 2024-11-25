from functools import cache
import py5

STEP = 3.8

def setup():
    py5.size(910, 570)
    py5.background(0)
    py5.color_mode(py5.HSB)
    py5.no_stroke()
    
    y = x = 10
    
    for n in range(1, 13):
        
        w = quadrado(x, y, n)
        last = fib(n - 1) * STEP
        if n % 2:
            x += w
            if n > 1:
                y -= last
        else:
            y += w
            x -= last

    py5.save('out.png')

def quadrado(x, y, n):
    tw = fib(n) * STEP
    for w in [fib(n) * STEP for n in range(1, n)]:
        sw = 2 + tw - w
        py5.fill(py5.remap(sw, 0, fib(13) * STEP, 0, 255), 200, 200)
        py5.square(tw / 2 + x - sw/2, tw / 2 + y - sw/2, sw)
    return tw
    
@cache
def fib(n):
    print(n)
    if n < 3:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)
    
py5.run_sketch(block=False)