
r, g, b = 85, 130, 240

def setup():
    size(600, 600)
    textAlign(CENTER)
    textSize(18)
   
def draw():
    background(0)
    fill(r, g, b)
    circle(300, 400, 300)
    
    fill(255, 0, 0)
    rect(0, 20, 200, r)
    fill(255)
    text("{} : {:.2%}".format(r, r / 255.0), 100, 15)
    
    fill(0, 255, 0)
    rect(200, 20, 200, g)
    fill(255)
    text("{} : {:.2%}".format(g, g / 255.0), 300, 15)
    
    fill(0, 0, 255)
    rect(400, 20, 200, b)
    fill(255)
    text("{} : {:.2%}".format(b, b / 255.0), 500, 15)

def keyPressed():
    global r, g, b
    if key == 's':
        saveFrame("sketch_2021_02_13a_cores.png")
    if key == 'r' and r > 0:
        r -= 1 
    elif key == 'R' and r < 255:
        r += 1
    if key == 'g' and g > 0:
        g -= 1
    elif key == 'G' and g < 255:
        g += 1
    if key == 'b' and b > 0:
        b -= 5
    elif key == 'B' and b < 255:
        b += 1        
