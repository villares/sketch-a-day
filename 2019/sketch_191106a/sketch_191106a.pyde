# Baseado no L-System apresentado pela Tatasz na
# Noite de Processing

iterations = 5 
# axiom = "F"
axiom = "HGF"
sentence = axiom
stroke_len = 200
rules = (
         # ("F", "F-F++F-F"),
         ("F", "[+F]-F"),
         ("G", "[HG]HGF"),
         ("H", "F[-GH]+GH")
         ,)
a = 45

def setup():
    size(700, 700)
    strokeWeight(1)
    noFill()
    generate(iterations)
    
def draw():
    global a
    background(220, 220, 200)    
    translate(width / 2, height / 3)
    global a    
    angle = radians(a)
    plot(angle)
    # if a <= 180:
    #     saveFrame("sketch###.png")
    #     print a
    #     a += 2.5
        

def generate(n):
    global stroke_len, sentence
    for c in range(n):
        stroke_len *= 0.5
        nextSentence = ""
        for c in sentence:
            found = False
            for c_a, c_b in rules:
                if c == c_a:
                    found = True
                    nextSentence += c_b
                    break
            if not found:
                nextSentence += c
        sentence = nextSentence

def plot(angle):
    for c in sentence:
        if c == "F":
            stroke(200, 0, 0)
            rect(0, 0, stroke_len/2, -stroke_len)
            translate(0, -stroke_len)
         # ellipse(0, 0, 10, 10)
        elif c == "G":
            stroke(0, 0, 200)
            rect(0, 0, stroke_len/2, -stroke_len)
            translate(0, -stroke_len)
        elif c == "H":
            stroke(0, 200, 0)
            rect(0, 0, stroke_len/2, -stroke_len)
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
    if keyCode == LEFT:
        a -= 5
    if keyCode == RIGHT:
        a += 5        
    if key == 's':
        saveFrame("####.png")
                      
                                          
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
