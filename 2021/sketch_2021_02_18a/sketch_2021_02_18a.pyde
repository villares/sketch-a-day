def setup():
    size(512, 512)
    background (0, 0, 0)
    blendMode(ADD)

def draw():
    if mousePressed and mouseButton == LEFT:
        fill(mouseX / 2, mouseY / 2, 0)
        circle(mouseX, mouseY, 10) # x, y, diâmetro
        
    if keyPressed and key =='a':
            clear()
