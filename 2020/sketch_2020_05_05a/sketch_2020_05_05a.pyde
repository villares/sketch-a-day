
def setup():
    size(400, 400)
    background(0)
    noStroke()
    colorMode(HSB)  # Matiz Saturação Brilho
        
def draw():
    translate(width / 2, height / 2)
    for i in range (12):
        rotate(TWO_PI / 12)
        fill(i * 16, 255, 255)
        if mousePressed:
            ellipse(mouseX - width / 2,
                    mouseY- height / 2, 10, 10)
        
def keyPressed():
    if key == ' ':
        background(0)
