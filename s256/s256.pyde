# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s256"  # 20180911
OUTPUT = ".png"

def setup():
    size(400, 400)
    colorMode(HSB)

def draw():
    background(200)
    #rect(0, 0, width, height)
    r = 125  # radius
    x1, y1 = 150, 200
    x2, y2 = 250, 200
    for i in range(64):
        stroke(i * 4, 200, 200)
        a1 = i * TWO_PI / 64 + frameCount/30.
        sx1 = x1 + cos(a1) * r #* cos(frameCount/20.)
        sy1 = y1 + sin(a1) * r #* cos(frameCount/20.)
        a2 = i * TWO_PI / 64 -  frameCount/30.
        sx2 = x2 + cos(a2) * r #* sin(frameCount/20.)
        sy2 = y2 + sin(a2) * r #* sin(frameCount/20.)
        line(sx1, sy1, sx2, sy2)
        
        
# print text to add to the project's README.md             
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
    )
   
