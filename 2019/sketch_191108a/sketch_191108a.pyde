# Baseado no L-System apresentado pela Tatasz na
# Noite de Processing

iterations = 6 
stroke_len = 300
angle_deg = 90
axiom = "HGF"
sentence = axiom
rules = (
         ("F", "F-F++F-F"),
         ("G", "[HG]HGF"),
         ("H", "F[-GH]+GH"),
         )

def setup():
    size(700, 700)
    strokeWeight(1)
    noFill()
    generate(iterations)
    
def draw():
    background(0)    
    translate(width / 2, 250)
    plot(radians(angle_deg))

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
        stroke_len *= 0.5
        next_sentence = ""
        for c in sentence:
            found = False
            for c_a, c_b in rules:
                if c == c_a:
                    found = True
                    next_sentence += c_b
                    break
            if not found:
                next_sentence += c
        sentence = next_sentence

def plot(angle):
    for c in sentence:
        stroke(255)
        if c == "F":
            line(0, 0, stroke_len/2, -stroke_len)
            translate(0, -stroke_len)
         # ellipse(0, 0, 10, 10)
        elif c == "G":
            line(0, 0, stroke_len/2, -stroke_len)
            translate(0, -stroke_len)
        elif c == "H":
            line(0, 0, stroke_len/2, -stroke_len)
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
    print(angle_deg)
    global angle_deg
    if keyCode == LEFT:
        angle_deg -= 5
    if keyCode == RIGHT:
        angle_deg += 5        
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
