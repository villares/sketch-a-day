from itertools import product
from random import  sample
from villares.line_geometry import min_max, is_poly_convex, poly_area
from villares.gif_export import gif_export

add_library('gifAnimation')

NUM_ELS = 6
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
    fill(0)
    t = brutal_sigmoid(radians(frameCount % 360))
    elements = iter(lerp_tuple(elements_a, elements_b, t))        
    strokeWeight(2)
    for element in elements:
        stroke(poly_color(element))
        beginShape()
        for x, y in element:
            vertex(x, y)
        endShape(CLOSE)
    
    # if frameCount % 2 == 0:
    #     gif_export(GifMaker, 'output', delay=200)
    if t == 0 and change_b:
        elements_b[:] = generate(NUM_ELS)
        change_b = False
    elif t == 1: 
        elements_a[:] = generate(NUM_ELS)
        change_b = True
        noStroke()
        fill(200, random(32))
        print('fade')
        rect(0, 0, width, height)
        
def generate(n):
    return [special_sample() for _ in range(n)]

def special_sample():
    while True:
       s =  tuple(sample(grade, 4))
       # a = poly_area(s)
       a, b = min_max(s)
       sqd = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
       if (is_poly_convex(s) and 
           (a[0] - b[0]) ** 2 < 42000 and
           (a[1] - b[1]) ** 2 < 42000
           ):
           return s

def poly_color(p):
    colorMode(HSB)
    return color(64 + poly_area(p) / 200.0 % 256, 200, 200)

def lerp_tuple(a, b, t):   
    return tuple(lerp_tuple(ca, cb, t) if isinstance(ca, tuple)
                 else lerp(ca, cb, t)             
                 for ca, cb in zip(a, b))

def ang_to_easing(angle):
    return (cos(angle) + 1) / 2
    
def brutal_sigmoid(angle):
    m = cos(angle) * 10
    r = 1 / (1 + exp(-m))            
    if r < 0.001: return 0
    elif r > 0.999: return 1
    else: return r
