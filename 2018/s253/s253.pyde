# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s253"  # 20180908
OUTPUT = ".png"

def setup():
    size(400, 400)
    colorMode(HSB)

def draw():
    fill(200, 10)
    rect(0, 0, width, height)
    r = 100  # radius
    x1, y1 = 100, 200
    x2, y2 = 300, 200
    for i in range(16):
        stroke(i * 16, 200, 200)
        a1 = i * TWO_PI / 16 + frameCount / map(mouseX, 0, width, 1, 50)
        sx1 = x1 + cos(a1) * r
        sy1 = y1 + sin(a1) * r
        a2 = i * TWO_PI / 16 + frameCount / map(mouseY, 0, height, 1, 50)
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
