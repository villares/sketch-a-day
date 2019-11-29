# L-System

iterations = 7
stroke_len = 600
angle_deg = 45
axiom = "G"
sentence = axiom
rules = {
         "F": "F--F++F",
         "G": "+GFH[-GF]",
         "H": "HH",
}

def setup():
    size(700, 700)
    global xo, yo
    xo, yo = width / 2, height / 2
    strokeWeight(1)
    noFill()
    generate(iterations)

def draw():
    background(0)
    translate(xo, yo)
    plot(radians(angle_deg))

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
        stroke_len *= 0.5
        next_sentence = ""
        for c in sentence:
            next_sentence += rules.get(c, c)
        sentence = next_sentence

def plot(angle):
    for c in sentence:
        if c == "F":
            stroke(255)
            line(0, 0, 0, -stroke_len / 2)
            translate(0, -stroke_len)
            # ellipse(0, 0, 10, 10)
        elif c == "G":
            stroke(0, 255, 0)
            line(0, 0, 0, -stroke_len / 2)
            translate(0, -stroke_len)
        elif c == "H":
            stroke(0, 0, 255)
            line(0, 0, 0, -stroke_len / 2)
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
    global angle_deg, xo, yo, stroke_len
    if key == '-':
        angle_deg -= 5
        print(angle_deg)
    if str(key) in "=+":
        angle_deg += 5
        print(angle_deg)
    if key == 's':
        saveFrame("####.png")
    if key == 'a':
        stroke_len *= 2
    if key == 'z':
        stroke_len /= 2
    if keyCode == LEFT:
        xo -= 50
    if keyCode == RIGHT:
        xo += 50
    if keyCode == UP:
        yo -= 50
    if keyCode == DOWN:
        yo += 50
def settings():
    """ print markdown to add at the sketch-a-day page"""
    from os import path
    global SKETCH_NAME, OUTPUT
    SKETCH_NAME = path.basename(sketchPath())
    OUTPUT = ".png"
    println(
        """
![{0}]({2}/{0}/{0}{1})

[{0}](https://github.com/villares/sketch-a-day/tree/master/{2}/{0}) [[Py.Processing](https://villares.github.io/como-instalar-o-processing-modo-python/index-EN)]
""".format(SKETCH_NAME, OUTPUT, year())
    )
