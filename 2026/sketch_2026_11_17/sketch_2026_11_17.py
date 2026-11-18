# Based on a crop from the image
# https://en.wikipedia.org/wiki/File:Margaret_Hamilton_-_restoration.jpg

salvar_pdf = False

def setup():
    global img
    size(800, 800)
    no_smooth()
    img = load_image('hamilton.png')
    img.resize(800, 800)
    #image(img, 0, 0)
    
def draw():
    global salvar_pdf
    if salvar_pdf:
        begin_record(PDF, '###.pdf')
    rect_mode(CENTER) # desenhe quadrados pelo centro
    background(0)  # fundo 
    fill(255)  # preenchimento
    no_stroke()
    n = 80
    d = width / n
    for j in range(n):
        y = j * d + d / 2
        for i in range(n):
            x = i * d + d / 2
            cor = img.get_pixels(int(x), int(y))         
            lado = remap(brightness(cor), 0, 255, 0, d-2) 
            square(x, y, lado)  # x, y, diâmetro
    if salvar_pdf:
        end_record()
        salvar_pdf = False

def key_pressed():
    global salvar_pdf
    if key == 'p':
        salvar_pdf = True
    elif key == 's':
        save_frame('out.png')

