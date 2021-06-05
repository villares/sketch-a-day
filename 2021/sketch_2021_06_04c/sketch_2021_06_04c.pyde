from itertools import product
from random import  sample
from villares.line_geometry import min_max, is_poly_convex, poly_area
from villares.gif_export import gif_export

add_library('gifAnimation')

NUM_ELS = 12
change_b = False

def setup():
    global grade, elements_a, elements_b
    size(500, 500)
    grade = list(product(range(50, 500, 100), repeat=2))    
    elements_a = generate(NUM_ELS)     
    elements_b = generate(NUM_ELS)     
        
def draw():
    global change_b
    colorMode(RGB)
    background(200, 200, 180)
    fill(0)
    for x, y in grade:
        circle(x, y, 5)
    fill(255, 100)
    
    t = brutal_sigmoid(radians(millis() / 100 % 360))
    elements = iter(lerp_tuple(elements_a, elements_b, t))        
    

    for element in elements:
        fill(poly_color(element), 100)
        beginShape()
        for x, y in element:
            vertex(x, y)
        endShape(CLOSE)
    
    # if frameCount % len(rects) == 0:
    #     gif_export(GifMaker, finish='True')
    #     exit()
    # else:
    #     gif_export(GifMaker, 'output', delay=400, quality=0)
    if t == 0 and change_b:
        elements_b[:] = generate(NUM_ELS)
        change_b = False
    elif t == 1: 
        elements_a[:] = generate(NUM_ELS)
        change_b = True
    
def generate(n):
    return [special_sample() for _ in range(n)]

def special_sample():
    while True:
       s =  tuple(sample(grade, 4))
       a, b = min_max(s)
       sqd = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
       if sqd < 80000 and is_poly_convex(s):
           # print sqd
           return s

def poly_color(p):
    return color(poly_area(p) % 256, 200, 200)

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))

def brutal_sigmoid(angle):
    m = cos(angle) * 10
    r = 1 / (1 + exp(-m))            
    if r < 0.001: return 0
    elif r > 0.999: return 1
    else: return r
