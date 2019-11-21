# Baseado no L-System apresentado pela Tatasz na
# Noite de Processing hoje!

axiom = "F+G+G"
sentence = axiom
stroke_len = 300
angle = radians(-120)
rule_a = ("F",           "G")
rule_b = ("F+G-F-G++FF", "GFG")

def setup():
    size (600, 600)
    background(220, 220, 200)
    scale(.35)
    translate(width - 400, height - 400)
    strokeWeight(2)
    generate(5)
    plot()

def generate(n):
    global stroke_len, sentence
    for _ in range(n):
        stroke_len *= 0.5
        nextSentence = ""
        for c in sentence:
            found = False
            for c_a, c_b in zip(rule_a, rule_b):
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
        elif c == "+":
            rotate(angle)
        elif c == "-":
            rotate(-angle)
        elif c == "[":
            pushMatrix()
        elif c == "]":
            popMatrix()
