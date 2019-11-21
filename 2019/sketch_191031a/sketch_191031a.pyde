# Baseado no L-System apresentado pela Tatasz na
# Noite de Processing hoje!

axiom = "FHG"
sentence = axiom
stroke_len = 250
angle = radians(-60)
rules = (("F", "H[+G-F]-G+F"),
         ("G", "GFG"),
         ("H", "HH")
         )

def setup():
    size(600, 600)
    background(220, 220, 200)
    scale(.25)
    translate(800, height + 1600)
    strokeWeight(2)
    generate(5)
    plot()
    saveFrame("sketch_191030a.png")

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
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

def plot():
    for c in sentence:
        if c == "F":
            stroke(0)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
         # ellipse(0, 0, 10, 10)
        elif c == "G":
            stroke(0, 0, 255)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
        elif c == "H":
            stroke(255, 0, 255)
            line(0, 0, 0, -stroke_len)
            translate(0, -stroke_len)
            noFill()
            circle(0, 0, stroke_len * 2)
        elif c == "+":
            rotate(angle)
        elif c == "-":
            rotate(-angle)
        elif c == "[":
            pushMatrix()
        elif c == "]":
            popMatrix()
