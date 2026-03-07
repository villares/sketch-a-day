import py5

def setup():
    global imgA, imgB, mascara
    py5.size(800, 800)
    py5.background(0)
    # https://commons.wikimedia.org/wiki/File:09272008_BrightonUT.JPG
    imgA = py5.load_image('plantaA.jpg')
    # https://commons.wikimedia.org/wiki/File:Aerial_view_overhead_Zwischenbergen_18.02.2009_12-57-42.JPG
    imgB = py5.load_image('plantaB.jpg')
    #imgA.copy(imgA, 0, 0, imgA.width, imgA.height, 0, 0, 800, 800)
    mascara = py5.create_graphics(200, 200)
    mascara.begin_draw()
    mascara.stroke(255)
    d = 6
    mascara.stroke_weight(d)
    mascara.stroke_join(py5.ROUND)
    mascara.rect(d / 2, d / 2, 200 - d, 100 - d)
    mascara.triangle(50, 100, 100, 100, 150, 200 - d)
    mascara.end_draw()
    py5.no_loop()
    
def draw():
    for x in range(50, 800, 250):
        for y in range(50, 800, 250):
            img = py5.random_choice((imgA, imgB))
            xr = py5.random(0, img.width - 200)
            yr = py5.random(0, img.height - 200)   
            recorte = recorte_com_mascara(img, mascara, xr, yr)
            py5.image(recorte, x, y)
    #py5.image(mascara, 0, 0)
    
def recorte_com_mascara(img, mascara, x, y):    
    w, h = mascara.width, mascara.height
    resultado = py5.create_image(mascara.width, mascara.height, py5.ARGB)
    resultado.copy(img, int(x), int(y), w, h, 0, 0, w, h)
    resultado.mask(mascara)
    return resultado


def key_pressed():
    if py5.key == ' ':
        py5.redraw()
    elif py5.key == 's':
        py5.save_frame('###.png')
    
py5.run_sketch(block=False)  # não funciona no MacOS

