
add_library('gifAnimation')
from villares.gif_export import gif_export

iterations = 7 #6
axiom = "F"
sentence = axiom
# stroke_len = 900
stroke_len = 1300   #a=120 sl=1200

rules = {"F": "[+G-F]-G+F",
         "G": "GHG",
         "H": "H-FH"
         }
a = 0
# a = 15

colors = (color(250, 50, 0),
          color(150, 0, 0),
          color(250, 0, 0),
          color(0, 150, 0),
          color(50, 50, 250),
          color(0, 50, 150),
          color(150, 50, 250),
          color(50, 150, 250)
          )


def setup():
    size(750, 750)
    strokeWeight(1)
    generate(iterations)
    fonte = createFont("Tomorrow Light",18)
    textFont(fonte)
    
def draw():
    global a
    background(240)    
    translate(width * .50, height * .5)
    # rotate(-HALF_PI)
    angle = radians(a)
    plot(angle)
    if a <= 180:
        delay(400)
        gif_export(GifMaker, "grow", delay=2200)

    # #     saveFrame("sketch###.png")        print a
        a += 5
    else:
          gif_export(GifMaker, finish=True)
        

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
        stroke_len *= 0.5
        nextSentence = ""
        for c in sentence:
            nextSentence += rules.get(c, c)
        sentence = nextSentence

def plot(angle):
    for i, c in enumerate(sentence):
        # fill(colors[i % len(colors)])
        fill(0)
        t = linhas[::-1][i % len(linhas)]
        if c == "F":
            rotate(HALF_PI)
            text(t, 0, 0)
            rotate(-HALF_PI)
            translate(0, -stroke_len)
        elif c == "G":
            rotate(HALF_PI)
            text(t, 0, 0)
            rotate(-HALF_PI)
            translate(0, -stroke_len)
        elif c == "H":
            rotate(HALF_PI)
            text(t, 0, 0)
            rotate(-HALF_PI)
            translate(0, -stroke_len)
        elif c == "+":
            rotate(angle)
        elif c == "-":
            rotate(-angle)
        elif c == "[":
            pushMatrix()
        elif c == "]":
            popMatrix()
 
def keyPressed():
    global a
    if key == 's':
        # saveFrame("{}-{}-##.png".format(a, stroke_len))
        saveFrame("{}-{}-bw.png".format(a, stroke_len))

    if key == 'a':
        a += 5
    if key == 'z':
        a -= 5
    print("angle: {}".format(a))
         
linhas = u"""
memento mori
"""        
