# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s260"  # 20180914
OUTPUT = ".png"

def setup():
    size(400, 400)
    colorMode(HSB)
    frameRate(30)
    strokeWeight(2)

def draw():
    background(200)
    #rect(0, 0, width, height)
    r = 125  # radius
    x1, y1 = 150, 200
    x2, y2 = 250, 200
    for i in range(128):
        stroke(i * 2, 200, 200)
        a1 = i * TWO_PI / 128 + HALF_PI
        sx1 = x1 + sin(a1) * r #* cos(frameCount/50.)
        sy1 = y1 + cos(a1) * r * sin(frameCount/77.)
        a2 = i * TWO_PI / 128 + QUARTER_PI
        sx2 = x2 + cos(a2) * r #* sin(frameCount/141.)
        sy2 = y2 + sin(a2) * r * cos(frameCount/30.)
        line(sx1, sy1, sx2, sy2)

# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
   
