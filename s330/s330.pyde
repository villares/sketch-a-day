# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s330"  # 20181124
OUTPUT = ".png"

from collections import deque
max_val = min_val = 0

def setup():
    frameRate(30)
    global gaussian_values
    size(500, 500)
    gaussian_values = deque(maxlen = width)
    for _ in range(width):
        gaussian_values.append(randomGaussian()/4. * height/2.)
    
def draw():
    global max_val, min_val
    noStroke()
    fill(1, 16)
    rect(0, 0, width, height)
    gaussian_values.append(randomGaussian()/4. * height/2)
    translate(0, height/2)
    stroke(255, 64)
    for x, v in enumerate(gaussian_values):
            line(x, -v, x, 0)
            if v > max_val:
                max_val = max_val + (v - max_val)/10.
            if v < min_val:
                min_val = min_val + (v - min_val)/10.
    stroke(255)
    line(0, -max_val, width, -max_val)
    line(0, -min_val, width, -min_val)
    if not frameCount % width:
        reset_max_min()
    
def reset_max_min():    
    global min_val, max_val
    min_val = max_val = 0
    
def keyPressed():
    reset_max_min()
    
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
