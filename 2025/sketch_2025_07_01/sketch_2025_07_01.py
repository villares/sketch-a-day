def setup():
    global img
    size(712, 949)
    img = load_image("https://upload.wikimedia.org/wikipedia/commons/6/66/Alan_Turing_%281951%29_%28crop%29.jpg")
    no_stroke()
    rect_mode(CENTER)
    
def draw():
    background(0) 
    num_filas = 96
    esp = height / num_filas
    num_colunas = int(width / esp)
    if img:
        for m in range(num_filas):
            y = m * esp + esp / 2
            for n in range(num_colunas):  # 0, 1, 2, 3, 4, 5
                x = n * esp + esp / 2
                xi = int(remap(x, 0, width, 0, img.width))
                yi = int(remap(y, 0, height, 0, img.height))
                cor = img.get_pixels(xi, yi)
                b = brightness(cor)
                h = int(remap(y, 0, height, 0, 255))
                fill(128, 255 - h, b)
                if is_mouse_pressed:
                    square(x, y, esp * b / 255)
                else:
                    square(x, y, esp * b // 255)

def key_pressed():
    save_frame('out##.png')