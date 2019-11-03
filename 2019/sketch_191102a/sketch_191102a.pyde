# Baseado no L-System apresentado pela Tatasz na
# Noite de Processing

iterations = 7
axiom = "F"
sentence = axiom
stroke_len = 500
rules = (("F", "[+G-F]-G+F"),
         ("G", "GHG"),
         ("H", "H-FH")
         )
a = 0

def setup():
    size(700, 700)
    strokeWeight(1)
    generate(iterations)
    
def draw():
    global a
    background(220, 220, 200)    
    translate(width / 2, height / 2)
    global a    
    angle = radians(a)
    plot(angle)
    if a <= 180:
        saveFrame("sketch###.png")
        print a
        a += 2.5
        

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
            stroke(255, 0, 0)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
         # ellipse(0, 0, 10, 10)
        elif c == "G":
            stroke(0, 0, 200)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
        elif c == "H":
            stroke(0, 200, 0)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
        elif c == "+":
            rotate(angle)
        elif c == "-":
            rotate(-angle)
        elif c == "[":
            pushMatrix()
        elif c == "]":
            popMatrix()
