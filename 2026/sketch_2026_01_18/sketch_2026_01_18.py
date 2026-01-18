import py5

STEP = 5

def eratosthenes(n):
    prime_map = [True for i in range(n+2)]  
    p = 2
    while p * p <= n:
        if prime_map[p]:
            for i in range(p * p, n + 2, p):
                prime_map[i] = False
        p += 1
    #return [p for p in range(2, n + 1) if prime_map[p]]
    return prime_map

def setup():
    py5.size(800, 800)
    py5.background(0)
    py5.stroke(255)
    prime_map = eratosthenes(10000)
    py5.translate(py5.width / 2, py5.height / 8)
    for b in prime_map:
        if b:
            py5.rotate(py5.radians(30))
        else:
            py5.rotate(py5.radians(-30))            
        py5.line(0, 0, 0, STEP)
        py5.translate(0, STEP)
    
py5.run_sketch(block=False)
        
