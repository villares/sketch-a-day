passo = 1

def setup():
    size(960, 960)
    global img
    img = loadImage("a.jpg")
    noFill() 
    colorMode(HSB)
    rectMode(CENTER)
    background(255)
    for x in range(0, width // 10, passo):  # range(inicio, limite, passo)
        for y in range(0, height // 10, passo):
            xc, yc = passo / 2 + x, passo / 2 + y
            cor = img.get(xc, yc)
            dark = 255 - brightness(cor)  # 0 a 255
            tam = dark / 255.0 * passo * 25
            stroke(hue(cor) + random(128, 255), 200, 100)
            if tam > passo * 0.37:
                strokeWeight(1)
                circle(xc * 10, yc * 10, tam) 
                strokeWeight(1)
                circle(xc * 10, yc * 10, tam / 2) 

    saveFrame('hmmm.png')
