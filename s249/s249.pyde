# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s249"  # 20180904
OUTPUT = ".png"

curvas = []
n = 3

def setup():
    size(1024, 300)
    noStroke()
    blendMode(MULTIPLY)
    strokeCap(SQUARE)
    
def keyPressed():
    if key == "s":
        saveFrame("###.png")
    else: 
        curvas[:] = []
        for i in range(n):
            curvas.append((random(-height/7,height/7),
                  random(-height/7, height/7),
                  random(.33, 3),
                  random(.33, 3),
                  random(.33, 3),
                 ))

def draw():
    background(200)
    translate(0, height/2)
    for i, (h, a, f1, f2, f3) in enumerate(curvas):
        if i % 3 == 0:
            stroke(100, 0, 200)
        elif i % 3 == 1:
            stroke(0, 100,200)
        else:
            stroke(200, 0, 100)
        beginShape()
        strokeWeight(5 + abs(h) / 5)
        for x in range(width):
            ang = frameCount/30. + x/30.
            ang2 = frameCount/15. + x/30.
            s = sin(ang * f1) + sin(ang2 * f2) + sin(ang2 * f3) 
            vertex(x, h + s * a)
        endShape()
        
# this part is for making it easy to add a markdown static "blog" entry 
def settings():
    println(
"""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(SKETCH_NAME, SKETCH_NAME[1:], OUTPUT)
)
