
def setup():
    size(640, 360)
    # The image file must be in the data folder of
    # the current sketch to load successfully.
    global img
    img = loadImage("moonwalk.jpg")    # Load the image into the programr
        
def draw():
    background(255, 0, 0)
    image(img, 0, 0)

    
def reduce_image(img, factor):    
    rimg = createGraphics(int(img.width * factor), int(img.height * factor))
    rimg.beginDraw()
    rimg.image(img, 0, 0, img.width * factor, img.height * factor)
    rimg.endDraw()
    return rimg

def keyPressed():
    global img
    if key == 'r':
        img = reduce_image(img, .9)
