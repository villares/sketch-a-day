passo = 12

def setup():
    size(780, 500)
    global img
    img = loadImage("gato.jpg")
    noStroke() 
    fill(0)
    rectMode(CENTER)
      
def draw():
    background(255)
    for x in range(0, width, passo):  # range(inicio, limite, passo)
        for y in range(0, height, passo):
            xc, yc = passo / 2 + x, passo / 2 + y
            cor = img.get(xc, yc)
            dark = 255 - brightness(cor)  # 0 a 255
            tam = dark / 255.0 * passo
            if tam > passo * 0.37:
                square(xc, yc, tam * 0.8) 
