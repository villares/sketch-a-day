def setup():
    global img
    size(720, 1034)
    img = loadImage("ada.jpg")
    colorMode(HSB)
    
def draw():
    background(0)
    espaco = 8
    for x in range(0, width, espaco):
       for y in range(0, height, espaco):
           cor = img.get(x // 2, y // 2)
           bri = brightness(cor)
           siz = map(bri, 0, 255, 0, espaco)
           sat = color(hue(cor), 255, 255)
           fill(sat)
           circle(espaco / 2 + x,
                  espaco / 2 + y, siz)
           
def keyPressed():
    if key == 's':
        saveFrame('sketch_2021_05_05_ada.png')
