num_colunas = num_filas = 100

def setup():
    size(800, 800)
    img = load_image("https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg")
    # img = load_image("Adalovelace.jpg")
    esp = width / num_colunas
    background(255)  # fundo branco
    for m in range(num_filas):
        y = m * esp + esp / 2
        for n in range(num_colunas):  # 0, 1, 2, 3, 4, 5
            x = n * esp + esp / 2
            # remap(v, inicial_origem, final_origem, inicaial_algo, final_alvo)
            xi = int(remap(x, 0, width, 0, img.width))
            yi = int(remap(y, 0, height, 0, img.height))
            cor = img.get_pixels(xi, yi)
            b = brightness(cor)
            fill(0)
            #fill(cor)
            d = remap(b, 0, 255, esp + 3, 0) 
            no_stroke()
            circle(x, y, d)
            
    save(__file__[:-2] + 'png')
          
