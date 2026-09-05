def setup():
    global img
    size(800, 800)
    # copiar ao lado do sketch .py
    # imagem local... 
    # https://upload.wikimedia.org/wikipedia/commons/d/dd/Adalovelace.jpg
    img = load_image("Adalovelace.jpg")
    no_stroke()

def draw():
    if is_mouse_pressed:
        for _ in range(20):
            x = mouse_x + random(-20, 20)
            y = mouse_y + random(-20, 20)
            xi = int(remap(x, 0, width, 0, img.width))
            yi = int(remap(y, 0, height, 0, img.height))
            cor = img.get_pixels(xi, yi)
            fill(cor, 20)
            circle(x, y, 10)
