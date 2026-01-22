esp = 10 # espaçamento

glifos = [
' ',
'-',
'+',
'XY',
'UT*',
'MXY',
'MXYUT+-',    
]

def setup():
    global img
    size(800, 800) 
    img = load_image('ada.jpg')
    no_stroke()
    text_align(CENTER, CENTER)

def draw():
    background(220)
    text_size(esp + 1)
    num_colunas = int(width / esp)
    num_filas = int(height / esp)
    for fila in range(num_filas):
        yt = esp * fila + esp / 2
        for coluna in range(num_colunas):
            xt = esp * coluna + esp / 2
            xi = int(remap(xt, 0, width, 0, img.width))
            yi = int(remap(yt, 0, height, 0, img.height))
            cor = img.get_pixels(xi, yi)
            b = brightness(cor) # 0 a 255
            peso = int(remap(b, 255, 0, 0, 6)) 
            fill(0)
            for glifo in glifos[peso]:
                text(glifo, xt, yt)

def key_pressed():
    global esp    
    if key == 'a':
        esp = esp + 1
    elif key == 'z':
        esp = esp - 1
    elif key == 's':
        save_frame('###.png')
        

