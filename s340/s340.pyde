from java.awt import Toolkit

xo, yo = 100, 100
xio, yio = 0, 0
grid_size = 50
s = 10

def setup():
    size(500, 500)
    global img
    img = loadImage("unifont-11.0.02.bmp")

def draw():
    # KeyEvent.VK_CAPS_LOCK is 20
    capsLocked =  Toolkit.getDefaultToolkit().getLockingKeyState(20)
    if capsLocked:
        image(img, xio, yio)
        noFill()
        rect(xio + xo, yio + yo, grid_size, grid_size)
    else:
        for x in range(grid_size):
            for y in range(grid_size):
                c = img.get(xo + x, yo + y)
                fill(c)
                rect(x * s, y * s, s, s)
    
def keyPressed():
    global xo, yo, xio, yio
    if keyCode == RIGHT and xo < img.width - 11:
        xo += 10
    if keyCode == LEFT and xo > 10:
        xo -= 10
    if keyCode == DOWN and yo < img.height - 11:
        yo += 10
    if keyCode == UP and yo > 10:
        yo -= 10
    if xo > width - grid_size:
        xio = width - grid_size - xo
    if yo > height - grid_size:
        yio = height - grid_size - yo    
    if key == "s" or key == "S":
        saveFrame("###.png")
