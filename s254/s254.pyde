# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s254"  # 20180909
OUTPUT = ".png"

def setup():
    size(400, 400)
    colorMode(HSB)

def draw():
    background(200)
    #rect(0, 0, width, height)
    r = 100  # radius
    x1, y1 = 100, 200
    x2, y2 = 300, 200
    for i in range(64):
        stroke(i * 4, 200, 200)
        a1 = i * TWO_PI * map(mouseX, 0, width, 0.1, 64)
        sx1 = x1 + cos(a1) * r
        sy1 = y1 + sin(a1) * r
        a2 = i * TWO_PI * map(mouseY, 0, height, 0.1, 64)
        sx2 = x2 + cos(a2) * r
        sy2 = y2 + sin(a2) * r
        line(sx1, sy1, sx2, sy2)
        
# print text in the console to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
    
