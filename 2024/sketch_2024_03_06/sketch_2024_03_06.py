num_colunas = num_filas = 80

def setup():
    size(800, 800)
    img = load_image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg")
    background(0) # fundo preto
    #image(img, 0, 0, 800, 800)
    no_stroke() # sem contorno nos elementos
    esp = width / num_colunas  # calcula o espaçamento
    for fila in range(num_filas):
        y = esp / 2 + esp * fila
        for coluna in range(num_colunas):
            x = esp / 2 + esp * coluna
            xi = remap(x, 0, width, 0, img.width)
            yi = remap(y, 0, height, 0, img.height)
            cor = img.get_pixels(int(xi), int(yi))
            #fill(cor)
            fill(255)
            diametro = brightness(cor) / 255 * esp
            circle(x, y, diametro)    

    save(__file__[:-2] + 'png')