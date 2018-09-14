# Alexandre B A Villares - https://abav.lugaralgum.com/sketch-a-day
SKETCH_NAME = "s244"  # 20180830
OUTPUT = ".png"

curvas = []
n = 6

def setup():
    size(1024, 300)
    blendMode(ADD)
    background(0)
    
def keyPressed():
    curvas[:] = []
    for i in range(n):
        curvas.append((random(-height/4,height/4),
                  random(-height/4, height/4),
                  random(.2, 5),
                  random(.2, 5),
                  random(.2, 5),
                 ))
    saveFrame(SKETCH_NAME+OUTPUT)


def draw():
    background(0)
    translate(0, height/2)
    for x in range(width):
          for h, a, f1, f2, f3 in curvas:
            ang = x / 30.
            if int(a) % 3 == 0:
                stroke(255, 0, 0)
            elif int(a) % 3 == 1:
                stroke(0, 255, 0)
            else:
                stroke(0, 0, 255)
            s = sin(ang * f1) + sin(ang * f2) + sin(ang * f3) 
            line(x, 0, x, h+ s * a)
            
            
def settings():
    print_text_for_readme(SKETCH_NAME, OUTPUT)
    
def print_text_for_readme(name, output):
    """ prints text in the console to add to project README.md """
    println("""
![{0}]({0}/{0}{2})

{1}: [code](https://github.com/villares/sketch-a-day/tree/master/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]

""".format(name, name[1:], output)
    )
