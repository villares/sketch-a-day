# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s247"  # 20180902
OUTPUT = ".png"

curvas = []
n = 3

def setup():
    size(1024, 300)
    noStroke()
    blendMode(MULTIPLY)
    
def keyPressed():
    if key == "s":
        saveFrame("###.png")
    else: 
        curvas[:] = []
        for i in range(n):
            curvas.append((random(-height/6,height/6),
                  random(-height/6, height/6),
                  random(.33, 3),
                  random(.33, 3),
                  random(.33, 3),
                 ))

def draw():
    background(200)
    translate(0, height/2)
    for i, (h, a, f1, f2, f3) in enumerate(curvas):
        if i % 3 == 0:
            fill(0, 100, 200)
        elif i % 3 == 1:
            fill(200, 0, 100)
        else:
            fill(100, 0, 200)
        beginShape()
        for x in range(width):
            ang = x/30.
            s = sin(ang * f1) + sin(ang * f2) + sin(ang * f3) 
            vertex(x, - h +10 + s * a)
        for xx in range(width):
            x = width-xx
            ang = x/30.
            s = sin(ang * f1)*1.1 + sin(ang * f2)*1.2 + sin(ang * f3)*1.3
            vertex(x, + h  +10 + s * a)
        endShape(CLOSE)
        
# this part is for making it easy to add a markdown static "blog" entry 
def settings():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    
def print_text_for_readme(name, output):
    """ prints text in the console to add to project README.md """
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
